# The World in One Page — Sunday 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/zonzonbk88/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/zonzonbk88/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the make.fun bounty **news-image-20261122**: one image that sums
up the world news of **Sunday 22 November 2026**.

`main.py` (Python 3, standard library only) copies the front page in
`entry.png` to `/output/entry.png` — or to `$MAKEFUN_OUTPUT_DIR/entry.png`
outside the grader's container — so every run writes identical bytes.
The page itself (1024×1024 PNG, ~135 KB) is drawn programmatically by
`make_frontpage.py` (PIL): masthead, date banner, one lead story, four
story cards with drawn icons, and a briefs strip, with all headlines
rendered as real text so they stay legible at thumbnail size.

## Stories chosen

Lead story:

- **COP31 ends without a deal** — the UN climate summit in Antalya,
  Türkiye, breaks up with no agreement after the EU and island states
  reject a text with no fossil-fuel phase-out; talks ran 48 hours into
  overtime.

Story cards:

- **Drone hits Russian warship off Libya** — a suspected Ukrainian drone
  strike on a Russian warship at Benghazi; Russian strikes kill six in
  the Kyiv region and partly collapse an apartment block in Dymer.
- **Democrats clinch House with 258 seats** — the midterm count gives
  Democrats a House majority of at least 258 seats, their largest
  since 1992.
- **Stocks slide as AI sell-off deepens** — S&P 500 −3.7%, Tokyo's
  Nikkei −5.1%, as investors dump AI-related shares.
- **Probe orbits Mercury after 8 years** — ESA/JAXA's BepiColombo enters
  Mercury orbit (announced by ESA; insertion on the night of 21 Nov,
  reported worldwide on 22 Nov), only the second spacecraft ever to
  orbit the innermost planet.

Also today (briefs):

- Mexico: cartel boss 'El Chapo Isidro' (Fausto Isidro Meza Flores)
  captured in Sinaloa.
- Indonesia: candy-factory fire in Banten kills 3, dozens missing.
- West Bank: settlers torch vehicles near Ramallah; Israel opens an
  inquiry.

## Sources

Cross-checked on 23 Nov 2026 across several outlets reporting the
22 Nov news day, including The Hindu's morning digest of 23 Nov 2026,
Dawn's international pages of 22–23 Nov 2026, The Economic Times world
news of 22 Nov 2026, OneTurn News' 22 Nov 2026 brief, Nature ("BepiColombo
finally reaches Mercury after eight-year odyssey", 21 Nov 2026) and
ESA's BepiColombo orbit-insertion release.

## Files

- `main.py` — the entrypoint: copies `entry.png` to the output.
- `entry.png` — the front page (the deliverable image).
- `make_frontpage.py` — the PIL program that draws `entry.png`.
- `LICENSE` — MIT, © 2026 zonzonbk88.
