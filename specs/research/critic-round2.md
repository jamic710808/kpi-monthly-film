# Critic round 2: kpi-monthly-film/out.mp4

Method: 60 half-second frames, plus native 0.1s frames from -0.3s to +0.6s around all 7 boundaries. Numbers are all still correct.

## Round-1 top-6 and defect status

1. **Sequential transitions: FIXED (collisions), PARTLY (feel).**
   - No overlap of two text layers at any of the 7 boundaries. The ghost "8", doubled 37.8%, "89" over "-1,160" and header stacks are all gone.
   - Cost: a near-blank frame at each boundary. The outgoing scene is blurred and gone by the boundary (frame at -0.1s). The incoming scene is first visible about +0.1s later. Each boundary shows 1-3 empty frames (about 0.1s), with only the rail and grid visible.
   - Worst empties:
     - 15.8s: the amber glow with no content.
     - 24.4s: a title-only frame.
2. **Text collisions: FIXED.**
   - 2.2-2.6s hook and count-up no longer collide.
   - The legend is no longer clipped at the right edge.
   - Header stacks and the "04/05" overlap are gone.
3. **Summary collapse: PARTLY.**
   - 21.5-22.5s is now a real move: the teal tiles fade and the three survivors slide into a centred row.
   - The row then sits dead from about 22.5s to 24.4s (about 2s) with about 50% of the frame empty above it.
   - At 20.0s only a 10% ghost tile is visible (near-empty frame).
   - The survivors do not carry into the action rows.
4. **End hold: PARTLY.**
   - Rows enter earlier.
   - The title-alone frame persists at about 25.0s, with an empty body.
   - From 26.0s to 30.0s the frame is near-static for about 4s. The sequential glow barely reads. This is double the allowed final hold.
   - Rows still have no owner, date or verb.
   - The sub-line is still small.
5. **Number format and units:**
   - Units sit with the digits: FIXED (萬, 億 and 天 are consistent).
   - "−25.7pp": FIXED.
   - "去年同期 68 天" label before the count-up: FIXED.
   - Gauge 0%/50% labels: PARTLY. They are about 12px, tiny. The gauge still counts through wrong values 0→37.8 for about 1s.
   - FCF "capex 衝高" is labelled "成因為示範假設，待實際資料確認": FIXED.
6. **Space and small text:**
   - Hook headline enlarged: FIXED.
   - +2.3pp pill is next to the 12.1 bar: FIXED.
   - Footer and top-right contrast: FIXED. Sampled about 7:1.
   - Amber glow: PARTLY. Reduced, but still a big blob on the AR and FCF scenes.
   - Lead subjects at 60-85% of the frame: STILL PRESENT.
     - The gauge is about 40% of the frame width, with the right half empty during 6.0-7.0s.
     - The FCF scene has a dead bottom half from 17.0s to 19.6s.
   - Chart captions ("去年同期 1.14 億", "去年同期 9.8%") are STILL PRESENT and small.

## Defect timestamps

- AR footnote "去年同期 68 天 / 客戶結構變化？" sits about 10px above the footer: STILL PRESENT (14.0-15.8s).
- Frozen time: about 2.4s of FCF hold (17.0-19.6s), plus about 2s on the summary, plus about 4s at the end. That is far beyond the quality bar of at most 1s per 30s. STILL PRESENT and now the biggest issue.

## New defects

- Boundary blanks: about 0.1-0.2s of rail-and-glow-only frames at 7 boundaries. On the AR to FCF boundary the amber glow is the only content.
- Count-up value flashes: the FCF count-up reads -97, -542, -923. This is acceptable as a count-up, but the gauge's wrong values on a labelled scale remain.
- Final scene: a lone title at 25.0s, where the "先追這兩件事" headline is larger than any other element. The rows then fill only about 62% of the width.

## Verdict on "fade out, then fade in"

It cleanly solves the overlap, and the blur-scale-out is polished. It fails the motion-grammar rules in two ways.

- It has no carried object. Between scenes only the rail persists. The rule asks for "a carried object or matched direction".
- It gives a rhythmic blank flash every 3-4s. That reads as slideshow, not premium.

Fix: overlap the exit tail with the incoming head by about 0.1s. Alternatively, keep the sequential rule for text only and let the background, glow and rail cross-travel.

## Recommendation

ONE MORE PASS. At most 3 fixes:

1. Cut the boundary dead time. Start each incoming scene at the boundary, with exit and enter overlapping about 0.1s and no shared text. Give the summary tiles and action rows a morph, so the survivors move into the action rows.
2. Kill the three static holds: FCF 17.0-19.6s, summary 22.5-24.4s, final 26-30s.
   - Add a staged second beat in each.
   - Keep only one final hold of about 1.8s.
   - Make the action rows verb, owner and date phrases.
3. Scale the leads: gauge 1.5x and FCF bar and number larger. Raise the 12px captions and the gauge labels to at least 20px. Tone the glow down further.
