# HUANG IS BACK — 24 November 2026

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/crisdion3006/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/crisdion3006/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A make.fun entry: one image summing up the world's news of Tuesday
24 November 2026, drawn entirely in code.

## The image

A magazine-cover poster on a black ink background — one lime hero
panel, two white cards and a numbered strip at the bottom:

1. **Tech, the comeback** — Nvidia's board unanimously reinstates
   Jensen Huang as CEO, days after his shock resignation amid
   espionage probes. Trump is reported to have made up to $15m on
   Nvidia shares after Huang's return.
2. **Poland** — a Russian drone enters Polish airspace; Warsaw
   scrambles air defences overnight.
3. **Libya** — Ukraine hits Russian warships off Libya; Kyiv says
   its drones struck a Russian naval base.
4. **Congress** — the first Gen Z woman in Congress: Melat Kiros,
   29, wins a seat.
5. **Seattle** — ICE arrests at Seattle airport; a father and
   daughter held.

Also today: the UN chief wants global AI rules within a year; COP31
talks stall.

## How it is built

`build_image.py` (Python 3, Pillow only) draws `entry.png` from fixed
coordinates — no network, no randomness, no timestamps, so two runs
are byte-identical. `main.ts` (Node 22, stdlib only) copies that
image to `/output/entry.png`.

```sh
python3 build_image.py   # writes entry.png (1024x1024, < 1 MiB)
node main.ts             # writes /output/entry.png
```

## License

MIT — see `LICENSE`.
