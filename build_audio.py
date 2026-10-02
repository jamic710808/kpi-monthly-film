"""混音：旁白(Gemini TTS) + 配樂(test-guizang-video/assets/music.wav) + 轉場/強調音效
用法：python build_audio.py [--no-vo]   → audio/mix.wav（含旁白）或 audio/mix_music_only.wav
設計重點：
  * 旁白起點跟場景邊界綁定（B 與 stage.html 的 B 同步），不是憑感覺對
  * 配樂用旁白當 sidechain 做 ducking，旁白講話時音樂自動退 ~6dB
  * 音效只放在真實轉場（whoosh，高通 180Hz 去低頻轟隆）和 4 個 chip pop，其餘不加（audio.md：乾淨 > 密集）
"""
import re, subprocess, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
SFX = 'K:/antigravity/test-guizang-video/assets/sfx'
MUSIC = 'K:/antigravity/test-guizang-video/assets/music.wav'
TOTAL = 30.0
B = [3.8, 7.9, 12.15, 15.35, 19.15, 22.15, 25.5]       # 與 stage.html 一致

VO = [(0.10, 'L0'), (3.90, 'L1'), (8.00, 'L2'), (12.25, 'L3'),
      (15.45, 'L4'), (19.25, 'L5'), (22.25, 'L6'), (25.60, 'L7')]
WHOOSH = [(b - 0.20, a) for b, a in zip(B, [0, -2, -1, -5, 0, 0, 0])]   # 逐事件微調：量測 1–6kHz 帶內提升後，把偏高者壓到 ≈ +4–6 dB
POPS = [(4.78, 0), (14.20, 0), (16.83, 0), (27.28, -7)]   # (時間, 該事件增益微調 dB)；最後一個因音樂床較空，單獨壓低                      # YoY chip / +2.3pp chip / +21天 chip / 結尾 pill

no_vo = '--no-vo' in sys.argv
no_sfx = '--no-sfx' in sys.argv
WH_PK, PP_PK = -21, -11        # 音樂床峰值約 −11.5 dBFS；音效要略高於音樂才聽得到，但仍比旁白(−3)低很多


def peak_db(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', path, '-af', 'volumedetect', '-f', 'null', '-'],
                       capture_output=True, text=True)
    return float(re.search(r'max_volume: (-?[\d.]+) dB', r.stderr).group(1))


def dur(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


wh = f'{SFX}/whoosh.wav'
pp = f'{SFX}/pop.wav'
# 目標峰值：whoosh −20 dBFS、pop −22 dBFS（旁白峰值約 −3，音樂床約 −20，音效在音樂之上、旁白之下）
g_wh = WH_PK - peak_db(wh)
g_pp = PP_PK - peak_db(pp)

inputs = ['-i', MUSIC]
fc = []
idx = 1
vo_labels = []
if not no_vo:
    for t, name in VO:
        f = f'{ROOT}/audio/vo/trim/{name}.wav'
        d = dur(f)
        inputs += ['-i', f]
        ms = int(t * 1000)
        fc.append(f'[{idx}]aresample=48000,aformat=channel_layouts=stereo,loudnorm=I=-17:TP=-2:LRA=7,'
                  f'afade=t=in:d=0.02,afade=t=out:st={max(d-0.05,0):.3f}:d=0.05,adelay={ms}|{ms}[v{idx}]')
        vo_labels.append(f'[v{idx}]')
        idx += 1
    fc.append(''.join(vo_labels) + f'amix=inputs={len(vo_labels)}:normalize=0:dropout_transition=0,asplit=2[vo][vokey0];[vokey0]apad=whole_dur={TOTAL}[vokey]')

# 配樂：取前 30s，淡出 2s，音量壓低當床；有旁白時以旁白為 key 做 ducking
fc.append(f'[0]atrim=0:{TOTAL},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={TOTAL-2.0}:d=2.0,volume=-9dB[mus]')
if no_vo:
    fc.append('[mus]acopy[musd]')
else:
    fc.append('[mus][vokey]sidechaincompress=threshold=0.02:ratio=5:attack=20:release=500:makeup=1[musd]')

sfx_labels = []
for t, adj in ([] if no_sfx else WHOOSH):
    inputs += ['-i', wh]
    ms = int(max(t, 0) * 1000)
    fc.append(f'[{idx}]aresample=48000,aformat=channel_layouts=stereo,highpass=f=180,lowpass=f=10000,'
              f'volume={g_wh+adj:.1f}dB,afade=t=in:d=0.01,adelay={ms}|{ms}[s{idx}]')
    sfx_labels.append(f'[s{idx}]'); idx += 1
for t, adj in ([] if no_sfx else POPS):
    inputs += ['-i', pp]
    ms = int(t * 1000)
    fc.append(f'[{idx}]aresample=48000,aformat=channel_layouts=stereo,highpass=f=220,lowpass=f=10000,'
              f'volume={g_pp+adj:.1f}dB,adelay={ms}|{ms}[s{idx}]')
    sfx_labels.append(f'[s{idx}]'); idx += 1

mix_in = ['[musd]'] + ([] if no_vo else ['[vo]']) + sfx_labels
fc.append(''.join(mix_in) + f'amix=inputs={len(mix_in)}:normalize=0:dropout_transition=0,'
          f'atrim=0:{TOTAL}[out]')

tag = ('_nosfx' if no_sfx else '')
raw = f'{ROOT}/audio/' + ('raw_music_only' if no_vo else 'raw_mix') + tag + '.wav'
out = f'{ROOT}/audio/' + ('mix_music_only' if no_vo else 'mix') + tag + '.wav'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[out]', '-ar', '48000', raw], check=True)
gfile = f'{ROOT}/audio/gain.txt'
if not no_vo and not no_sfx:
    # 以含旁白版本為準量 integrated，算出到 −16 LUFS 所需增益；music-only 套同一增益，才能公平比較
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', raw, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True)
    I = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r.stderr)[-1])
    gain = -16 - I
    open(gfile, 'w').write(str(gain))
else:
    gain = float(open(gfile).read())
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', raw, '-af', f'volume={gain:.2f}dB,alimiter=limit=0.84:level=disabled', '-ar', '48000', out], check=True)
print('wrote', out, f'dur={dur(out):.2f}s', f'gain={gain:.2f}dB', f'g_whoosh={g_wh:.1f}dB g_pop={g_pp:.1f}dB')
