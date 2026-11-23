#!/usr/bin/env python3
"""Draw the front page for Sunday 22 November 2026 -> entry.png.

A one-page newspaper composed with PIL: masthead + date, one lead story
(COP31 collapses in Antalya), four story cards (Ukraine/Libya strike,
US House, markets, BepiColombo at Mercury) and a briefs strip.
All text is rendered here in code so the headlines stay crisp.

Stories (22 Nov 2026, cross-checked across The Hindu, Dawn, Economic
Times and OneTurn News):
  * COP31 in Antalya ends with no agreement: EU + island states reject
    a text with no fossil-fuel phase-out; talks run 48h into overtime.
  * Suspected Ukrainian drone hits a Russian warship at Benghazi,
    Libya; Russian strikes kill six in the Kyiv region.
  * Democrats clinch a US House majority of at least 258 seats,
    their largest since 1992.
  * Global stocks slide as the AI sell-off deepens (S&P 500 -3.7%,
    Nikkei -5.1%).
  * ESA/JAXA BepiColombo enters Mercury orbit after an 8-year voyage.
  * Briefs: Mexico captures cartel boss 'El Chapo Isidro'; Indonesia
    candy-factory fire (3 dead, dozens missing); West Bank settler
    arson, Israel opens inquiry.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 227)
INK = (24, 24, 24)
GREY = (84, 80, 70)
RED = (176, 42, 32)
BLUE = (29, 78, 137)
TEAL = (23, 107, 96)
GOLD = (176, 124, 32)
CARD = (255, 253, 246)
RULE = (24, 24, 24)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, max_w, leading=1.18):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def centered(draw, y, text, fnt, fill):
    w_ = draw.textlength(text, font=fnt)
    draw.text(((W - w_) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


# ---------------------------------------------------------------- icons
def icon_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=5)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], outline=BLUE, width=3)
    d.line([cx - r, cy, cx + r, cy], fill=BLUE, width=3)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55], 0, 180, fill=BLUE, width=3)
    d.arc([cx - r, cy - r * 1.45, cx + r, cy + r * 0.45], 0, 180, fill=BLUE, width=3)
    # red crack across the globe: the deal broke apart
    crack = [(cx - r * 0.7, cy - r * 0.45), (cx - r * 0.25, cy - r * 0.1),
             (cx - r * 0.45, cy + r * 0.25), (cx + r * 0.05, cy + r * 0.5),
             (cx - r * 0.1, cy + r * 0.85)]
    d.line(crack, fill=RED, width=5, joint="curve")


def icon_warship(d, x, y, s):
    # hull + superstructure, quadcopter drone above
    d.polygon([(x, y + 34 * s), (x + 92 * s, y + 34 * s),
               (x + 76 * s, y + 50 * s), (x + 14 * s, y + 50 * s)], fill=INK)
    d.rectangle([x + 30 * s, y + 20 * s, x + 62 * s, y + 34 * s], fill=INK)
    d.line([x + 46 * s, y + 4 * s, x + 46 * s, y + 20 * s], fill=INK, width=3)
    cx, cy = x + 20 * s, y - 2 * s
    d.ellipse([cx - 4 * s, cy - 4 * s, cx + 4 * s, cy + 4 * s], fill=RED)
    for (ox, oy) in ((-13, -8), (13, -8), (-13, 8), (13, 8)):
        d.line([cx, cy, cx + ox * s, cy + oy * s], fill=RED, width=2)
        d.ellipse([cx + ox * s - 4 * s, cy + oy * s - 2 * s,
                   cx + ox * s + 4 * s, cy + oy * s + 2 * s], outline=RED, width=2)


def icon_capitol(d, x, y, s):
    d.rectangle([x, y + 52 * s, x + 96 * s, y + 58 * s], fill=BLUE)
    for i in range(5):
        cx = x + (8 + i * 19) * s
        d.rectangle([cx, y + 34 * s, cx + 7 * s, y + 52 * s], fill=BLUE)
    d.rectangle([x, y + 30 * s, x + 96 * s, y + 35 * s], fill=BLUE)
    d.pieslice([x + 18 * s, y - 6 * s, x + 78 * s, y + 44 * s], 180, 360, fill=BLUE)
    d.line([x + 48 * s, y - 16 * s, x + 48 * s, y - 4 * s], fill=BLUE, width=3)
    d.ellipse([x + 45 * s, y - 20 * s, x + 51 * s, y - 14 * s], fill=BLUE)


def icon_chart(d, x, y, s):
    d.line([x, y + 6 * s, x, y + 56 * s], fill=INK, width=3)
    d.line([x, y + 56 * s, x + 94 * s, y + 56 * s], fill=INK, width=3)
    pts = [(x + 6 * s, y + 12 * s), (x + 30 * s, y + 22 * s),
           (x + 52 * s, y + 18 * s), (x + 86 * s, y + 46 * s)]
    d.line(pts, fill=RED, width=5)
    d.polygon([(x + 86 * s, y + 46 * s), (x + 74 * s, y + 44 * s),
               (x + 84 * s, y + 34 * s)], fill=RED)


def icon_mercury(d, x, y, s):
    cx, cy, r = x + 44 * s, y + 30 * s, 24 * s
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD)
    for (ox, oy, orr) in ((-9, -6, 5), (8, 4, 7), (-2, 11, 4), (11, -10, 4)):
        d.ellipse([cx + ox * s - orr * s, cy + oy * s - orr * s,
                   cx + ox * s + orr * s, cy + oy * s + orr * s],
                  fill=(150, 100, 22))
    d.ellipse([x - 4 * s, y + 2 * s, x + 100 * s, y + 58 * s], outline=TEAL, width=3)
    d.rectangle([x + 78 * s, y - 2 * s, x + 90 * s, y + 8 * s], fill=TEAL)


# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 40  # margin

    # masthead
    d.line([M, 26, W - M, 26], fill=RULE, width=3)
    centered(d, 38, "THE WORLD IN ONE PAGE", font(SERIF_B, 58), INK)
    d.line([M, 116, W - M, 116], fill=RULE, width=3)
    d.rectangle([M, 126, W - M, 178], fill=INK)
    centered(d, 136, "SUNDAY 22 NOVEMBER 2026", font(SANS_B, 34), (255, 255, 255))

    # lead story: COP31
    y = 196
    d.text((M, y), "CLIMATE  ·  ANTALYA, TÜRKIYE", font=font(SANS_B, 23), fill=RED)
    y += 33
    y = text_block(d, (M, y), "COP31 ENDS WITHOUT A DEAL",
                   font(SERIF_B, 52), INK, 660, leading=1.04)
    icon_globe(d, 842, 274, 80)
    y = text_block(d, (M, y + 4),
                   "Nearly 200 nations leave the UN climate summit with no "
                   "agreement, after the EU and island states reject a text "
                   "with no fossil-fuel phase-out — 48 hours into overtime.",
                   font(SANS, 23), (40, 40, 40), 700)
    y += 14
    d.line([M, y, W - M, y], fill=RULE, width=2)

    # story cards, 2 x 2
    cards = [
        ("WAR · UKRAINE & LIBYA", icon_warship,
         "DRONE HITS RUSSIAN WARSHIP OFF LIBYA",
         "Suspected Ukrainian strike at Benghazi. Russian missiles "
         "kill six in the Kyiv region."),
        ("POLITICS · WASHINGTON", icon_capitol,
         "DEMOCRATS CLINCH HOUSE WITH 258 SEATS",
         "The midterm count gives Democrats their largest House "
         "majority since 1992."),
        ("MARKETS · NEW YORK", icon_chart,
         "STOCKS SLIDE AS AI SELL-OFF DEEPENS",
         "The S&P 500 falls 3.7% and Tokyo's Nikkei 5.1% as investors "
         "dump AI shares."),
        ("SPACE · MERCURY", icon_mercury,
         "PROBE ORBITS MERCURY AFTER 8 YEARS",
         "BepiColombo is only the second craft ever to orbit "
         "the innermost planet."),
    ]
    cw = (W - 2 * M - 24) // 2
    ch = 196
    top = y + 16
    for i, (kicker, icon, head, body) in enumerate(cards):
        cx = M + (i % 2) * (cw + 24)
        cy = top + (i // 2) * (ch + 16)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=CARD, outline=(190, 182, 160), width=2)
        d.text((cx + 20, cy + 12), kicker, font=font(SANS_B, 18), fill=GREY)
        icon(d, cx + cw - 126, cy + 40, 1.0)
        yy = text_block(d, (cx + 20, cy + 40), head, font(SANS_B, 26), INK,
                        cw - 158, leading=1.1)
        text_block(d, (cx + 20, yy + 6), body, font(SANS, 20),
                   (40, 40, 40), cw - 40)

    # briefs strip
    by = top + 2 * ch + 32
    d.line([M, by, W - M, by], fill=RULE, width=2)
    by += 12
    d.text((M, by), "ALSO TODAY", font=font(SANS_B, 23), fill=RED)
    briefs = ("MEXICO: Cartel boss \u2018El Chapo Isidro\u2019 captured in Sinaloa   ·   "
              "INDONESIA: Candy-factory fire kills 3, dozens missing   ·   "
              "WEST BANK: Settlers torch vehicles; Israel opens inquiry")
    by = text_block(d, (M, by + 34), briefs, font(SANS, 22), (40, 40, 40), W - 2 * M)

    centered(d, by + 14, "Sunday 22 November 2026 — the day's world news on one page",
             font(SERIF, 20), GREY)
    assert by + 48 <= H, f"layout overflow: content ends at {by + 48}"
    img.save("entry.png", optimize=True)
    print("wrote entry.png, content ends at", by + 48)


if __name__ == "__main__":
    main()
