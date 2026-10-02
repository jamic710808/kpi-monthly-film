// 逐格渲染 stage.html → ffmpeg → MP4
//   node render.js --stills 0,3,7,10      輸出指定秒數的 JPG 到 ./qa（版面檢查用）
//   node render.js [--fps 30] [out.mp4]   全片
// 為什麼不螢幕錄影：每格都是 render(t) 算出來，同一秒永遠同一畫面，可重現、可局部重跑
const path = require('path'), fs = require('fs'), { spawn } = require('child_process');
const WD = __dirname;
const args = process.argv.slice(2);
const opt = n => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : null; };
const fps = Number(opt('--fps') || 30);
const stills = opt('--stills');
const out = args.find(a => a.endsWith('.mp4')) || path.join(WD, 'out.mp4');

let puppeteer;
for (const p of ['puppeteer-core', 'C:/nvm4w/nodejs/node_modules/hyperframes/node_modules/puppeteer-core']) {
  try { puppeteer = require(p); break; } catch {}
}
if (!puppeteer) throw new Error('找不到 puppeteer-core');
const chrome = ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'].find(fs.existsSync);

(async () => {
  const browser = await puppeteer.launch({ executablePath: chrome, headless: 'new', args: ['--allow-file-access-from-files', '--force-device-scale-factor=1', '--hide-scrollbars'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  let bad = false;
  page.on('pageerror', e => { bad = true; console.error('[pageerror]', e.message); });
  await page.goto('file:///' + path.join(WD, 'stage.html').replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const { total } = await page.evaluate(() => window.init());

  if (stills) {
    const dir = path.join(WD, 'qa'); fs.mkdirSync(dir, { recursive: true });
    for (const t of stills.split(',').map(Number)) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: path.join(dir, `f_${t.toFixed(2).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 85 });
    }
    await browser.close(); console.log('stills ->', dir); if (bad) process.exit(2); return;
  }

  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', String(fps), '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const n = Math.round(total * fps);
  for (let f = 0; f < n; f++) {
    await page.evaluate(t => window.render(t), f / fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) console.log(`frame ${f}/${n}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('done ->', out, bad ? '(有 pageerror)' : '');
  if (bad) process.exit(2);
})();
