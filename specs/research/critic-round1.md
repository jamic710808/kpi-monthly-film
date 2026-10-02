# Critic round 1: kpi-monthly-film/out.mp4

## 1. Verdict: REVISE

The story and numbers hold up. The craft does not: every scene boundary is a crossfade that stacks two live layouts, and the last 3.5s are frozen. A finance manager gets the conclusion on mute, so the information bar is met. The motion bar is not.

Number check, all correct:
- 1.28 / 1.14 = 1.1228, shown as +12.3%.
- Revenue gap +0.14億 is correct.
- 37.8 - 34.2 = 3.6pp.
- 37.8 - 25.7 = 12.1.
- 12.1 - 9.8 = 2.3pp.
- 89 - 68 = 21 days.
- AR bar ends at 68% and 89% of the 0-100 axis, which is correct.
- Waterfall bar heights are proportional once settled.
- FCF is -2,300萬.

## 2. Per scene

| Scene | Time | On screen | Empty | Ranked problems |
|---|---|---|---|---|
| Hook | 0-2.3 | Headline, 5-dot legend row, left rail | ~45% (right half and bottom) | (1) Right half is dead. (2) Legend row drifts as the whole frame pushes in. By ~2.0s "自由現金流" sits ~15px from the right edge and is clipped at ~2.5s. (3) Frame 0 is clean but sparse; the legend row is tiny. |
| Revenue | 2.3-5.2 | 1.28億 count-up, YoY pill, 2 bars | ~25% | (1) The 0→1.28 count-up reads as data (0.58, 0.79, 0.95, 1.16). (2) Bar captions "去年同期 1.14 億 / 本月 1.28 億" are tiny and low priority. |
| Gross margin | 5.2-8.4 | Half-gauge, +3.6pp, vs 34.2% | ~35% (lower third) | (1) Gauge counts 12.6 → 32.2 → 37.6 → 37.8, so wrong values show for ~1s. (2) Gauge scale is unlabelled. 37.8% fills ~65-70% of the arc, which implies a max of about 55%. (3) "成因：示範（待實際資料）" is tiny. |
| Waterfall | 8.4-12.0 | 37.8 → -25.7 → 12.1, +2.3pp pill, 9.8% line | ~25% | (1) "−25.7" has no unit; add "pp" or "%". (2) The +2.3pp pill floats ~150px above the 12.1 bar. (3) The 9.8% label is tiny and far right. (4) At 12.0 a ghost grey "8" sits behind the bars. |
| AR days | 12.0-15.8 | 68 → 89 count, +21 day pill, 0-100 bar, amber glow | ~35% | (1) 68, 75, 88 show for ~1.5s with no "prior year" label, so 68 reads as current. (2) The footnote "去年同期 68 天…" sits ~17px above the footer and is cramped. (3) The orange glow blob is off-brand decoration. |
| FCF | 15.8-19.6 | -2,300萬 count-up, lone red bar, caption | ~30% | (1) The 萬 glyph is jammed against the last digit with no gap (in 1,754 and 2,259 it overlaps). The summary tile writes "−2,300 萬" with a gap, so it is inconsistent. (2) "capex 衝高" and "轉負" are causal or trend claims with no data behind them. The gross-margin scene hedges its cause as "待實際資料"; this one does not. (3) The bar has no scale or label. |
| Summary | 19.6-24.4 | 6 tiles, then 3 teal tiles fade, 2 tiles remain | ~45% from 22.0s | (1) The survivors do not move. The top half sits empty for ~2.4s with ghost tiles at ~10% opacity. (2) The collapse should be an object moving, not a fade. (3) Tile text is small. |
| Actions | 24.4-30 | "先追這兩件事" and 2 rows | 75% at 25.0s; ~40% later | (1) Title alone with an empty body at 25.0s. (2) From ~27.5s to 30.0s the frame is nearly static (~2.5s). (3) Rows carry no verb, owner or date. (4) The sub-line is tiny against the headline. |

## 3. Layout and transition defects

- **2.2-2.6s:** "0.00億 / 0.11億" is stacked on the red headline line. "2026 年 9 月" collides with "01 營收". The legend is clipped at the right edge at 2.5s.
- **5.2-5.7s:** The ghost "1.28" sits behind "10.6%/12.6%". The YoY pill ghosts over the gauge. "NT$" ghosts too.
- **8.4-8.7s:** "37.8%" appears twice, the gauge over the bar. "02 毛利率" overlaps "03 營業利益率" in the header. The bar-chart axis labels appear under the gauge.
- **12.0-12.4s:** A giant grey "8" glyph sits behind the waterfall. The "04" header ghosts. The rail dot turns amber mid-chart.
- **15.8-16.2s:** Worst frame. "89" overprints "−1,160", "天" and "萬" collide, the bar and pill ghost, and the "04" and "05" headers overlap.
- **~20.0s:** The blurred -2,300 ghost shows behind tile 1 and tile 2.
- **24.4-24.7s:** "月報總覽" overlaps "下月追蹤". "先追這兩件事" is printed over faded tile numbers.
- **Frozen time:** about 27.5-30.0s is a near-static hold. The quality bar allows one hold of up to ~1.5-2s on the CTA.
- **Footer and top-right label:** very small and low-contrast. This is likely below WCAG AA; sample it to confirm.
- **Rail:** dots light correctly. It is the only carried object across scenes.

## 4. Top 6 changes, by impact

1. **Replace crossfades with sequenced exit then enter.**
   - Outgoing scene: 0.18s, translate -40px, opacity to 0, `blur(6px)`, `pointer-events:none`.
   - Incoming scene: starts at +0.12s with a stagger.
   - Enforce "one scene's text layer visible at a time" so no two titles or numbers overlap.
   - Use the same hold-and-exit pattern at all 7 boundaries.
2. **Fix text collisions.**
   - Header: swap the section header with a vertical slide, never a crossfade.
   - Count-ups: start at the settled position and animate only the digit text, not the whole block. Do not run two count-ups at once.
   - Hook legend: contain the push-in on the headline only (`transform` on the headline wrapper, not the legend). Clamp the legend inside the 96px margins.
3. **Turn the summary into a real collapse.**
   - At 22.0s, FLIP-animate the 2 survivors (and the dark tile) from their positions to a centred row at 1.3x scale over 0.5s.
   - Remove the 3 teal tiles with scale 0.9 and opacity 0.
   - The title "先追這兩件事" then rises above them. The same two tiles morph into the action rows, a carried object into the final scene.
4. **Rework the end hold.**
   - Rows enter staggered at 25.2s and 25.6s, with no empty-body frame.
   - Hold the final frame about 1.8s.
   - Make the rows action phrases: "追 應收帳款 +21 天：客戶結構、帳齡分布", with sub-line at about 28px or larger.
   - Add a slow 3-4% scale push through 30s.
5. **Fix number-format and unit consistency.**
   - Use one rule: number, 8px gap, unit "萬/億/天" (e.g. "−2,300 萬").
   - Add "pp" to "−25.7".
   - Add a prior-year chip to AR at 12.5s ("去年 68 天").
   - Change the gross-margin gauge to a labelled 0-100% scale, or replace it with a horizontal bar.
   - Hedge "capex 衝高" and "轉負" with "（待實際資料）", or remove them.
6. **Use the empty space and raise small text.**
   - Scale lead subjects to 60-85% of the frame (gauge about 1.6x, hook headline about 1.2x).
   - Move the +2.3pp pill next to the 12.1% bar.
   - Raise the footer, top-right label and chart captions to at least 22px at 1080p, with contrast at least 4.5:1.
   - Remove or tone down the orange glow blob; keep the brand teal/amber/red palette.
