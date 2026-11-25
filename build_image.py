#!/usr/bin/env python3
"""news-image-20261124 -- magazine-cover poster, hero-dominant.

A single lime hero panel carries the day's biggest story (Nvidia /
Jensen Huang), two white cards carry the war stories, and a dark
strip at the bottom carries two more. Fixed text and fixed
coordinates only, so the output is byte-identical on every run.
Drawn with Pillow only; no network, no randomness.
"""

import textwrap

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
INK = (14, 15, 20)
PAPER = (246, 246, 238)
LIME = (198, 242, 78)
WHITE = (255, 255, 255)
GREY = (120, 122, 128)
DARKGREY = (58, 60, 68)
CARD = (255, 255, 255)
TEAL = (24, 120, 110)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    out = []
    for line in text.split("\n"):
        out.extend(textwrap.wrap(line, width=width) or [""])
    # Re-wrap by pixel width instead of character count.
    wrapped = []
    for line in out:
        words = line.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width or not cur:
                cur = trial
            else:
                wrapped.append(cur)
                cur = w
        if cur:
            wrapped.append(cur)
    return wrapped


def main():
    img = Image.new("RGB", (SIZE, SIZE), INK)
    d = ImageDraw.Draw(img)

    # Header bar.
    d.text((48, 34), "TUESDAY  24  NOVEMBER  2026", font=font(BOLD, 26), fill=LIME)
    d.text((48, 66), "THE WORLD IN ONE PICTURE", font=font(REG, 22), fill=GREY)
    d.ellipse((948, 36, 976, 64), fill=LIME)
    d.text((898, 38), "24", font=font(BOLD, 26), fill=WHITE)
    d.line((48, 104, 976, 104), fill=DARKGREY, width=2)

    # Hero: lime panel, black type.
    d.rounded_rectangle((48, 124, 976, 512), radius=28, fill=LIME)
    d.text((76, 148), "TECH  •  THE COMEBACK", font=font(BOLD, 24), fill=INK)
    d.text((76, 190), "HUANG", font=font(BOLD, 150), fill=INK)
    d.text((76, 330), "IS BACK", font=font(BOLD, 150), fill=INK)
    # Hero explainer sits below the lime panel, in white on ink.
    d.text((48, 528), "Nvidia's board unanimously reinstates Jensen Huang as CEO,",
           font=font(REG, 25), fill=WHITE)
    d.text((48, 560), "days after his shock resignation amid espionage probes.",
           font=font(REG, 25), fill=WHITE)
    d.text((48, 592), "Trump is reported to have made up to $15m on Nvidia shares",
           font=font(REG, 25), fill=GREY)
    d.text((48, 624), "after Huang's return.", font=font(REG, 25), fill=GREY)

    # Two white cards: the war stories.
    d.rounded_rectangle((48, 668, 502, 880), radius=20, fill=CARD)
    d.text((72, 688), "01  •  POLAND", font=font(BOLD, 22), fill=TEAL)
    for i, line in enumerate(wrap(d, "Russian drone enters Polish airspace", font(BOLD, 30), 410)):
        d.text((72, 724 + i * 36), line, font=font(BOLD, 30), fill=INK)
    for i, line in enumerate(wrap(d, "Warsaw scrambles air defences overnight.", font(REG, 23), 410)):
        d.text((72, 800 + i * 29), line, font=font(REG, 23), fill=DARKGREY)

    d.rounded_rectangle((522, 668, 976, 880), radius=20, fill=CARD)
    d.text((546, 688), "02  •  LIBYA", font=font(BOLD, 22), fill=TEAL)
    for i, line in enumerate(wrap(d, "Ukraine hits Russian warships off Libya", font(BOLD, 30), 410)):
        d.text((546, 724 + i * 36), line, font=font(BOLD, 30), fill=INK)
    for i, line in enumerate(wrap(d, "Kyiv says its drones struck a Russian naval base.", font(REG, 23), 410)):
        d.text((546, 800 + i * 29), line, font=font(REG, 23), fill=DARKGREY)

    # Bottom strip: two more stories, numbered in lime.
    d.text((48, 900), "03", font=font(BOLD, 30), fill=LIME)
    d.text((96, 902), "First Gen Z woman in Congress — Melat Kiros, 29, wins a seat.",
           font=font(BOLD, 24), fill=WHITE)
    d.text((48, 940), "04", font=font(BOLD, 30), fill=LIME)
    d.text((96, 942), "ICE arrests at Seattle airport — father and daughter held.",
           font=font(BOLD, 24), fill=WHITE)
    d.text((48, 984), "ALSO: UN chief wants global AI rules within a year  •  COP31 talks stall",
           font=font(REG, 20), fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
