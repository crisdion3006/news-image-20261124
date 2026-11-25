// news-image-20261124 — entrypoint (Node 22, stdlib only).
//
// The poster itself is drawn by build_image.py and kept in this
// repository as entry.png: a magazine-cover poster on a black ink
// background, one lime hero panel ("HUANG IS BACK" — Nvidia
// reinstates Jensen Huang as CEO), two white cards and a numbered
// strip at the bottom. This program's only job is to place that
// exact image at /output/entry.png, byte for byte, so the run is
// deterministic: every run writes the same bytes. Nothing here
// reads the network or the clock.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const target = "/output/entry.png";

mkdirSync(dirname(target), { recursive: true });
copyFileSync(source, target);
console.log(`wrote ${target}`);
