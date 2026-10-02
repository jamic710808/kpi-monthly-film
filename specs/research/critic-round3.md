# Critic round 3: kpi-monthly-film/out.mp4

Method: 60 half-second frames, plus 20fps strips (-0.3s to +0.45s) at 2.3, 8.4, 15.8, 23.2 boundaries. Numbers and units all correct (1.28億/+12.3%, 37.8%/+3.6pp, -25.7pp, 12.1%/+2.3pp, 89天/+21天, -2,300萬).

## Round-2 fixes
1. Boundary dead time: FIXED. Exit/enter now overlap; 0 empty frames at 15.8, about 2 frames (0.1s) at 8.4 (new chart has bars but no labels), about 5 frames (0.25s, 23.4-23.65s) at 23.2 with only the title visible (under 10% content). No slideshow blink.
2. Static holds:
   - FCF 17.0-19.6s: FIXED. Chips appear about 18.0s, footnote about 18.5s.
   - Summary 22.5-24.4s: FIXED. Gone by 23.2.
   - Final 26-30s: PARTLY. Pill lands about 26.1s and all rows are settled by about 26.5s. Then 3.5s of near-static frame (about 2x the allowed 1.8s final hold). The amber ring on rows only pulses faintly.
   - Summary-to-action morph: STILL PRESENT (cross-fade, not a morph). Acceptable for an internal film.
3. Scale and captions:
   - Gauge: FIXED. About 55% of frame width, end labels 0%/50% readable.
   - FCF bar: FIXED.
   - Chart captions ("去年同期 1.14億"): PARTLY. Larger but still about 14-16px at 1080p.
   - Glow: FIXED (subtle).

## Round-2 listed defects
- AR footnote near footer: PARTLY. At rest (15.5s) it sits clear. During exit blur (16.0s) it scales into the footer, transitional only.
- Gauge counting wrong values: STILL PRESENT but minor (0.3%, 27.3% at 6-7s).

## New defects
- Transitional collision at 15.8-16.0s: blurred "89" overlaid by the incoming "-0萬" (and "-97"). Looks like a text clash for about 0.15s. Same at 23.3s: the title overlaps ghost tiles, and 8.4s has the gauge ghost over the chart axis labels. These are blurred and short, but they break the "no text over text" rule.
- Count-up flashes on FCF (-0, -97, -401...) are acceptable.
- Frame 0 (t=0s) hook is complete. Footer text is tiny, about 9px, low priority, but not touching content.
- Final rows fill only about 50% of the frame width and the lower 35% is empty. This is under-using space, but it is readable.
- Claims: "成因待確認", "示範" and "capex 衝高" are all labelled as assumptions. The data backs everything.
  - Check: opex ratio 25.7pp + op margin 12.1% = 37.8%. OK.
  - Unit fine.

## Verdict
Core issues are resolved. Remaining items are polish, not blockers for an internal data film.

Optional polish (not required):
1. Trim the final hold to about 1.8s (end at about 28.3s, or add one more beat).
2. Shorten the ghost overlap at 15.8 and 23.2 so the incoming text does not sit over blurred outgoing text.
3. Bump the chart captions and the footer.

SHIP
