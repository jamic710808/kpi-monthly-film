# KPI 月報 30 秒動態影片

30 秒、1080p 的 KPI 月報動態影片（繁體中文旁白＋配樂）。**所有數字與公司皆為虛構示範數據**，不代表任何真實經營結果。

- 播放頁：https://jamic710808.github.io/kpi-monthly-film/
- 影片檔：[video.mp4](video.mp4)

## 內容
結論先行（獲利改善、現金流亮紅燈）→ 營收 → 毛利率 → 營益率瀑布 → 應收帳款天數 → 自由現金流 → 總覽收斂 → 下月追蹤。

## 檔案
| 檔案 | 用途 |
|---|---|
| `stage.html` | 全部畫面。`render(t)` 是時間的純函式，同一秒永遠同一畫面 |
| `render.js` | puppeteer-core 逐格截圖 → ffmpeg 合成 MP4（`node render.js --fps 30 out.mp4`） |
| `build_audio.py` | 混音：旁白＋配樂（旁白觸發 ducking）＋轉場音效 |
| `audio/vo/` | Gemini TTS 旁白原始音檔（L0–L7） |
| `specs/research/` | BRIEF、各輪評審報告與 Gauntlet 紀錄 |

## 製作方式與限制
- 流程依 `business-motion-film` skill：分鏡 → 建置 → 獨立評審迴圈（3 輪，最後判 SHIP）。
- 響度約 −16 LUFS、true peak −2.4 dBFS（量測值；未經人耳驗證）。
- 評審為同模型家族的 agent，抽樣檢視，非逐幀。
- 配樂與音效取自 test-guizang-video 專案的程式生成素材；該專案起步工程程式碼為 AGPL-3.0，本 repo 不含其程式碼。重用前請自行確認授權。
- `build_audio.py` 內的素材路徑是作者本機路徑，需自行調整。
