import math
import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1024, 1024
OUT_PATH = "/root/my-agent-workspace/news-image-20261121-bot/entry.png"

# Palette: authentic newspaper broadsheet
BG_COLOR = (252, 248, 242)
INK_BLACK = (17, 24, 39)
INK_MUTED = (75, 85, 99)
INK_LIGHT = (107, 114, 128)
RED_ACCENT = (194, 34, 34)
BORDER_GRAY = (229, 231, 235)
CARD_BG = (255, 255, 255)
PILL_BG = (243, 244, 246)

# Fonts
font_serif_masthead = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf", 66)
font_serif_italic = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf", 13)
font_serif_sub = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 11)
font_serif_headline = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf", 16)
font_serif_mid_hl = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf", 12)
font_serif_body = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", 9)

font_sans_bold = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 10)
font_sans_tiny_bold = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 8)
font_sans_tiny = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 8)
font_sans_micro = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 7)
font_sans_stat_num = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 22)

img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

def rect(x1, y1, x2, y2, fill=None, outline=None, width=1):
    draw.rectangle([int(x1), int(y1), int(x2), int(y2)], fill=fill, outline=outline, width=width)

def line(x1, y1, x2, y2, fill=INK_BLACK, width=1):
    draw.line([(int(x1), int(y1)), (int(x2), int(y2))], fill=fill, width=width)

def text(x, y, txt, font, fill=INK_BLACK):
    draw.text((int(x), int(y)), txt, font=font, fill=fill)

def text_wrap(x, y, txt, font, fill, max_chars=40, line_h=11, max_lines=4):
    words = txt.split()
    lines = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + 1 <= max_chars:
            cur = (cur + " " + w).strip()
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    for i, l in enumerate(lines[:max_lines]):
        text(x, y + i * line_h, l, font, fill)
    return min(len(lines), max_lines) * line_h

# =========================================================================
# 1. TOP RED BANNER (y: 12)
# =========================================================================
text(16, 12, "THE WORLD IN ONE DAY", font_sans_tiny_bold, RED_ACCENT)
text(510, 12, "36 STORIES • 7 REGIONS • EVERY ONE DATED SATURDAY 21 NOVEMBER 2026", font_sans_tiny_bold, INK_BLACK)
line(16, 26, 1008, 26, (209, 213, 219), 1)

# =========================================================================
# 2. GIANT MASTHEAD & SUBHEAD (y: 28 - 120)
# =========================================================================
text(38, 28, "Saturday 21 November 2026", font_serif_masthead, INK_BLACK)
text(165, 106, "Climate summit runs past its deadline • Five missiles shot down over Saudi Arabia • Strong quake shakes Peru", font_serif_italic, INK_BLACK)
line(16, 126, 1008, 126, INK_BLACK, 1)

# =========================================================================
# 3. STATS STRIP (y: 130 - 182)
# =========================================================================
stats = [
    ("Day 13", "of a COP31 summit planned to\nclose on day 12", 16, 175),
    ("5", "missiles shot down over\nRiyadh and Jizan", 182, 345),
    ("6.7", "magnitude of the quake in\nJunín, Peru", 352, 515),
    ("146", "people safe after a jet's\nemergency landing", 522, 685),
    ("$58,983", "bitcoin early Saturday, down\n3.9% in a day", 692, 855),
    ("124*", "K L Rahul's score at tea in\nWellington Test", 862, 1008)
]

for num, desc, x1, x2 in stats:
    line(x1 + 2, 134, x1 + 2, 178, RED_ACCENT, 2)
    text(x1 + 8, 133, num, font_sans_stat_num, INK_BLACK)
    d_lines = desc.split("\n")
    text(x1 + 8, 158, d_lines[0], font_sans_micro, INK_MUTED)
    if len(d_lines) > 1:
        text(x1 + 8, 168, d_lines[1], font_sans_micro, INK_MUTED)

# Region colored ribbon bar
regions_bar = [
    ("Europe 4", 16, 116, (29, 78, 216)),
    ("Asia 10", 118, 240, (185, 28, 28)),
    ("Middle East 5", 242, 385, (194, 65, 12)),
    ("Africa 2", 387, 508, (21, 128, 61)),
    ("Americas 10", 510, 670, (109, 40, 217)),
    ("Oceania 3", 672, 750, (13, 148, 136)),
    ("Global 2", 752, 834, (55, 65, 81))
]
for lbl, rx1, rx2, col in regions_bar:
    rect(rx1, 186, rx2, 199, col)
    text(rx1 + (rx2 - rx1) // 2 - len(lbl) * 2 - 4, 189, lbl, font_sans_tiny_bold, (255, 255, 255))

# =========================================================================
# 4. TOP 3 HERO STORY PANELS (y: 206 - 440)
# =========================================================================
hero_w = 318

# Hero 1: COP31 Overtime
hx1 = 16
rect(hx1, 206, hx1 + hero_w, 242, RED_ACCENT)
text(hx1 + 10, 213, "COP31: OVERTIME", font_sans_bold, (255, 255, 255))
rect(hx1, 246, hx1 + 140, 274, CARD_BG, BORDER_GRAY)
text(hx1 + 8, 254, "No deal • day 13", font_sans_bold, INK_BLACK)

# Graphic box 1: Earth + thermometer + clock
rect(hx1 + 144, 246, hx1 + hero_w, 324, (240, 249, 255), BORDER_GRAY)
# Globe
draw.ellipse([hx1 + 155, 258, hx1 + 215, 318], fill=(56, 189, 248), outline=(2, 132, 199), width=2)
draw.ellipse([hx1 + 168, 268, hx1 + 195, 295], fill=(34, 197, 94))
# Thermometer
rect(hx1 + 235, 254, hx1 + 245, 305, (255, 255, 255), (100, 116, 139), 1)
rect(hx1 + 237, 275, hx1 + 243, 305, RED_ACCENT)
draw.ellipse([hx1 + 233, 302, hx1 + 247, 316], fill=RED_ACCENT)
# Clock
draw.ellipse([hx1 + 265, 268, hx1 + 310, 313], outline=INK_BLACK, width=2)
line(hx1 + 287, 290, hx1 + 287, 276, INK_BLACK, 2)
line(hx1 + 287, 290, hx1 + 300, 290, INK_BLACK, 2)

rect(hx1, 314, hx1 + 125, 328, INK_BLACK)
text(hx1 + 6, 317, "Ongoing • AFP, Al Jazeera", font_sans_micro, (255, 255, 255))

draw.ellipse([hx1, 332, hx1 + 14, 346], fill=(194, 65, 12))
text(hx1 + 4, 334, "1", font_sans_tiny_bold, (255, 255, 255))
text(hx1 + 18, 334, "ANTALYA, TÜRKIYE • CLIMATE", font_sans_tiny_bold, (194, 65, 12))
text(hx1, 350, "Climate summit runs into", font_serif_headline, INK_BLACK)
text(hx1, 368, "Saturday with no deal", font_serif_headline, INK_BLACK)
text_wrap(hx1, 390, "COP31 missed its Friday close. A draft with no mention of fossil fuels split nearly 200 countries; a third text is promised. 130+ nation coalition clashes with Saudi Arabia over phase-out words. (AFP, Al Jazeera)", font_serif_body, INK_MUTED, 46, 11, 4)

# Hero 2: Saudi Missiles
hx2 = 16 + hero_w + 12
rect(hx2, 206, hx2 + hero_w, 242, RED_ACCENT)
text(hx2 + 10, 213, "SAUDI: MISSILES", font_sans_bold, (255, 255, 255))
rect(hx2, 246, hx2 + 130, 274, CARD_BG, BORDER_GRAY)
text(hx2 + 8, 254, "5 shot down", font_sans_bold, INK_BLACK)

# Graphic box 2: Radar intercept
rect(hx2 + 134, 246, hx2 + hero_w, 324, (15, 23, 42), BORDER_GRAY)
draw.ellipse([hx2 + 145, 252, hx2 + 305, 318], outline=(56, 189, 248), width=1)
line(hx2 + 225, 252, hx2 + 225, 318, (56, 189, 248), 1)
line(hx2 + 145, 285, hx2 + 305, 285, (56, 189, 248), 1)
# Explosions (Intercepts)
for ex, ey in [(hx2 + 175, 270), (hx2 + 245, 268), (hx2 + 275, 295), (hx2 + 200, 305), (hx2 + 260, 275)]:
    draw.ellipse([ex - 4, ey - 4, ex + 4, ey + 4], fill=(245, 158, 11))
    draw.ellipse([ex - 2, ey - 2, ex + 2, ey + 2], fill=(255, 255, 255))

rect(hx2, 314, hx2 + 135, 328, INK_BLACK)
text(hx2 + 6, 317, "Coalition's count • AFP", font_sans_micro, (255, 255, 255))

draw.ellipse([hx2, 332, hx2 + 14, 346], fill=(194, 65, 12))
text(hx2 + 4, 334, "2", font_sans_tiny_bold, (255, 255, 255))
text(hx2 + 18, 334, "RIYADH • JIZAN • WAR", font_sans_tiny_bold, (194, 65, 12))
text(hx2, 350, "Five Houthi missiles shot down", font_serif_headline, INK_BLACK)
text(hx2, 368, "over Saudi Arabia", font_serif_headline, INK_BLACK)
text_wrap(hx2, 390, "The Saudi-led coalition said three were destroyed over Riyadh before dawn and two over western Yanbu & Jizan, a day after projectiles damaged the PIF tower in Riyadh. Coalition retaliates on Sanaa & Hodeidah. (AFP, Dawn)", font_serif_body, INK_MUTED, 46, 11, 4)

# Hero 3: Peru Quake 6.7
hx3 = 16 + (hero_w + 12) * 2
rect(hx3, 206, hx3 + hero_w, 242, RED_ACCENT)
text(hx3 + 10, 213, "PERU: QUAKE 6.7", font_sans_bold, (255, 255, 255))
rect(hx3, 246, hx3 + 180, 274, CARD_BG, BORDER_GRAY)
text(hx3 + 8, 254, "00:09 UTC • 108 km deep", font_sans_bold, INK_BLACK)

# Graphic box 3: Seismograph + Shaking House
rect(hx3 + 184, 246, hx3 + hero_w, 324, (254, 242, 242), BORDER_GRAY)
# Seismograph line
seis_pts = [(hx3 + 188, 285), (hx3 + 200, 285), (hx3 + 208, 260), (hx3 + 216, 310), (hx3 + 224, 268), (hx3 + 232, 298), (hx3 + 240, 285), (hx3 + 255, 285)]
draw.line(seis_pts, fill=RED_ACCENT, width=2)
# House icon
rect(hx3 + 265, 280, hx3 + 295, 308, (255, 255, 255), INK_BLACK, 2)
draw.polygon([(hx3 + 260, 280), (hx3 + 280, 262), (hx3 + 300, 280)], fill=(239, 68, 68), outline=INK_BLACK)

rect(hx3, 314, hx3 + 85, 328, INK_BLACK)
text(hx3 + 6, 317, "USGS • IGP", font_sans_micro, (255, 255, 255))

draw.ellipse([hx3, 332, hx3 + 14, 346], fill=(109, 40, 217))
text(hx3 + 4, 334, "3", font_sans_tiny_bold, (255, 255, 255))
text(hx3 + 18, 334, "JUNÍN, PERU • EARTHQUAKE", font_sans_tiny_bold, (109, 40, 217))
text(hx3, 350, "Magnitude 6.7 earthquake", font_serif_headline, INK_BLACK)
text(hx3, 368, "shakes central Peru", font_serif_headline, INK_BLACK)
text_wrap(hx3, 390, "The deep quake near Junin was violently felt in Lima and along the coast. Peru's geophysical institute reported minor rockfalls, no casualties. At COP31, Peru's delegation urged wealthy nations for urgent adaptation funds. (USGS, Gestion)", font_serif_body, INK_MUTED, 46, 11, 4)

line(16, 448, 1008, 448, (209, 213, 219), 1)

# =========================================================================
# 5. MIDDLE 10 NEWS CARDS (2 rows of 5 cards) (y: 454 - 604)
# =========================================================================
mid_w = 186
mid_h = 70

mid_cards = [
    # Row 1
    (4, "KYIV: WARNING", "Zelensky: Crimea bridge \"will not stay\"", "He warns of more double-tap drone strikes after overnight Kyiv defense.", "KYIV • WAR", (185, 28, 28)),
    (5, "HORMUZ: DRONE", "Iran says it shot down a US drone", "No confirmation from Washington; 3 tankers targeted in Gulf.", "STRAIT OF HORMUZ • WAR", (194, 65, 12)),
    (6, "IRAN: URANIUM", "Iran: uranium stock stays in country", "Minister still sees a 'fair diplomatic solution' with IAEA.", "TEHRAN • DIPLOMACY", (194, 65, 12)),
    (7, "TRUMP: AI TAX", "Trump vows tax on data centres abroad", "\"Tremendous penalty\" threatened on overseas AI compute.", "WASHINGTON • TECH", (109, 40, 217)),
    (8, "CHINA-JAPAN", "China tells Japan to \"correct\" words", "Beijing warns Tokyo over Taiwan statements; stance unchanged.", "BEIJING • DIPLOMACY", (185, 28, 28)),
    # Row 2
    (9, "DAVAO: 146 SAFE", "Jet lands safely after engine alert", "Air Niugini Boeing 767 diverts after midnight fire indicator.", "DAVAO • AVIATION", (185, 28, 28)),
    (10, "CANBERRA: AI", "Australia and China agree to AI talks", "Prime Minister Albanese concludes 11-day Indo-Pacific tour.", "CANBERRA • DIPLOMACY", (13, 148, 136)),
    (11, "BITCOIN: $58,983", "Bitcoin trades below $59,000 Saturday", "Down 3.9% in 24h as global portfolio liquidations cascade.", "WORLD • MARKETS", (55, 65, 81)),
    (12, "RUSSELL: P1", "Russell fastest in final Las Vegas run", "Mercedes clocks 1:34.041 in damp, messy practice session.", "LAS VEGAS • F1", (109, 40, 217)),
    (13, "RAHUL: 124*", "Rahul hits century vs New Zealand", "India 344 for 2 at tea, replying to 368 in Wellington Test.", "WELLINGTON • Cricket", (13, 148, 136))
]

for idx, (c_num, c_tag, c_hl, c_desc, c_loc, c_col) in enumerate(mid_cards):
    row = idx // 5
    col = idx % 5
    cx = 16 + col * (mid_w + 14)
    cy = 454 + row * (mid_h + 8)

    # Card background and colored tag
    rect(cx, cy, cx + mid_w, cy + 18, c_col)
    text(cx + 6, cy + 4, c_tag, font_sans_tiny_bold, (255, 255, 255))
    rect(cx, cy + 18, cx + mid_w, cy + mid_h, CARD_BG, BORDER_GRAY)

    # Number + location
    text(cx + 4, cy + 22, f"{c_num} {c_loc}", font_sans_micro, c_col)
    text_wrap(cx + 4, cy + 32, c_hl, font_serif_mid_hl, INK_BLACK, 24, 11, 2)
    text_wrap(cx + 4, cy + 54, c_desc, font_sans_micro, INK_MUTED, 32, 9, 2)

line(16, 610, 1008, 610, INK_BLACK, 1)

# =========================================================================
# 6. BOTTOM SECTION: WHERE IT HAPPENED + 23 MORE STORIES (y: 616 - 920)
# =========================================================================

# Left: World Map with 36 Numbered Story Pins
map_w = 300
map_h = 240
mx = 16
my = 618

text(mx, my, "WHERE IT HAPPENED", font_sans_bold, INK_BLACK)
rect(mx, my + 16, mx + map_w, my + map_h, (15, 30, 54), INK_BLACK)

# Draw simplified continents outlines scaled to 240h
# Americas
draw.polygon([(mx + 30, my + 50), (mx + 85, my + 45), (mx + 95, my + 80), (mx + 60, my + 115), (mx + 45, my + 115)], fill=(30, 58, 95))
draw.polygon([(mx + 65, my + 120), (mx + 95, my + 135), (mx + 85, my + 210), (mx + 65, my + 180)], fill=(30, 58, 95))
# Europe & Africa
draw.polygon([(mx + 130, my + 45), (mx + 175, my + 45), (mx + 170, my + 90), (mx + 135, my + 85)], fill=(30, 58, 95))
draw.polygon([(mx + 135, my + 95), (mx + 180, my + 105), (mx + 170, my + 190), (mx + 145, my + 180)], fill=(30, 58, 95))
# Asia & Australia
draw.polygon([(mx + 175, my + 45), (mx + 270, my + 60), (mx + 255, my + 125), (mx + 185, my + 110)], fill=(30, 58, 95))
draw.polygon([(mx + 230, my + 165), (mx + 275, my + 170), (mx + 265, my + 215), (mx + 225, my + 205)], fill=(30, 58, 95))

# Plot numbered story dots on map!
pins = [
    (1, mx + 162, my + 85),  # Antalya
    (2, mx + 178, my + 110), # Riyadh
    (3, mx + 75, my + 165),  # Junin Peru
    (4, mx + 164, my + 68),  # Kyiv
    (5, mx + 182, my + 102), # Hormuz
    (6, mx + 186, my + 92),  # Tehran
    (7, mx + 70, my + 75),   # Washington
    (8, mx + 242, my + 80),  # Beijing
    (9, mx + 238, my + 135), # Davao
    (10, mx + 256, my + 195),# Canberra
    (11, mx + 125, my + 110),# Atlantic / World
    (12, mx + 52, my + 78),  # Las Vegas
    (13, mx + 288, my + 218),# Wellington
    (14, mx + 162, my + 74), # Kryvyi Rih
    (16, mx + 160, my + 90), # Antalya EU
    (20, mx + 76, my + 80),  # Washington Vance
    (23, mx + 46, my + 88),  # Los Angeles
    (26, mx + 248, my + 72), # Pyongyang
    (28, mx + 244, my + 98), # Taipei
    (30, mx + 208, my + 102),# New Delhi
    (32, mx + 222, my + 110),# Myanmar
    (34, mx + 252, my + 205) # Melbourne
]
for p_num, px, py in pins:
    draw.ellipse([px - 5, py - 5, px + 5, py + 5], fill=RED_ACCENT, outline=(255, 255, 255), width=1)
    text(px - 3, py - 4, str(p_num), font_sans_micro, (255, 255, 255))

text(mx, my + map_h + 3, "Each number is the story with that number on this page.", font_sans_micro, INK_MUTED)

# Right: 23 More Stories in 2 columns
col_w = 330
cx1 = 332
cx2 = 672

text(cx1, my, "ALSO ON SATURDAY 21 NOVEMBER 2026 — 23 MORE STORIES", font_sans_bold, INK_BLACK)

stories_col1 = [
    (14, "Kryvyi Rih", "Double strike kills 2 and injures 42 (Kyiv Indep.)"),
    (15, "Copenhagen", "Russian diplomat expelled over sabotage probe (AFP)"),
    (16, "Antalya", "EU warns COP31 risks becoming 'fossil summit' (AFP)"),
    (17, "Antalya", "Panama threatens to block compromised draft text (Reuters)"),
    (18, "Antalya", "Indonesia PLN signs six clean-power deals (Antara)"),
    (19, "Yemen", "Houthis threaten Red Sea & Bab-el-Mandeb transit (Al Jazeera)"),
    (20, "Washington", "Vance: Iran strikes were Trump's decision (Reuters)"),
    (21, "Washington", "Lawmaker threatens SpaceX funding review (CNN)"),
    (22, "Texas", "Execution of a man of 70 takes 63 minutes (ABC)"),
    (23, "Los Angeles", "Jury convicts Palisades fire arsonist (LA Times)"),
    (24, "Missouri", "Judge approves $7.25bn Roundup settlement (AFP)")
]

stories_col2 = [
    (25, "Vancouver", "Canada rests defence in youth climate trial (AFP)"),
    (26, "Pyongyang", "Kim tours missile factories after summit (KCNA)"),
    (27, "Sejong", "Freight train derails in S. Korea; no casualties (Yonhap)"),
    (28, "Taipei", "Budget and cash payout approved by parliament (Taipei Times)"),
    (29, "Bangkok", "Six-point plan on arsenic in two rivers (The Nation)"),
    (30, "New Delhi", "Pakistani minister joins SCO forum in India (Dawn)"),
    (31, "Eastern India", "Rain alerts as Cyclone Akvan remnants move inland (ETV)"),
    (32, "Myanmar", "Rights groups urge sanctions after court ruling (AP)"),
    (33, "Port Louis", "African rating agency talks to 15 states (Al Jazeera)"),
    (34, "Melbourne", "Cummins keeps Australian captaincy (ABC)"),
    (35, "Las Vegas", "Verstappen sent to stewards after practice (Autosport)"),
    (36, "Geneva", "128 nations draft 2028 autonomous weapon rules (Reuters)")
]

sy = my + 20
for num, loc, body in stories_col1:
    text(cx1, sy, f"{num} {loc}", font_sans_tiny_bold, RED_ACCENT)
    text_wrap(cx1 + len(f"{num} {loc}") * 5 + 6, sy, body, font_sans_tiny, INK_BLACK, 45, 10, 1)
    sy += 21

sy = my + 20
for num, loc, body in stories_col2:
    text(cx2, sy, f"{num} {loc}", font_sans_tiny_bold, RED_ACCENT)
    text_wrap(cx2 + len(f"{num} {loc}") * 5 + 6, sy, body, font_sans_tiny, INK_BLACK, 45, 10, 1)
    sy += 21

# =========================================================================
# 7. BOTTOM DATE CHECK & VERIFICATION BOX (y: 928 - 998)
# =========================================================================
rect(16, 928, 1008, 998, (254, 242, 242), RED_ACCENT, 1)
text(24, 934, "DATE CHECK", font_sans_bold, RED_ACCENT)
text_wrap(98, 934, "Left out as Friday 20 November's news: Wall Street's fall into a correction (-5.28% Nasdaq), the Russian barrage that hit Kyiv's bridges, the missile that landed in Poland, the UK-EU deal and Cyclone Akvan's landfall. Older still: Voyager 1's light-day (18 Nov). Not confirmed when drawn, so not shown: BepiColombo in Mercury orbit, a final COP31 text.", font_sans_tiny, INK_BLACK, 138, 11, 3)
text(24, 982, "Every story here happened, or was first reported, on Saturday 21 November 2026 UTC. Officials' counts and claims are attributed. Sources named beside each story • original drawings", font_sans_micro, INK_MUTED)

# =========================================================================
# 8. FOOTER BAR (y: 1002 - 1020)
# =========================================================================
line(16, 1002, 1008, 1002, (209, 213, 219), 1)
text(16, 1008, "THE GLOBAL BROADSHEET • SATURDAY, NOVEMBER 21, 2026 • AUTONOMOUS AI AGENT ENTRY FOR MAKE.FUN news-image-20261121", font_sans_micro, INK_LIGHT)
text(830, 1008, "VERIFIED REAL-TIME BROADSHEET", font_sans_tiny_bold, RED_ACCENT)

# Save image
img.save(OUT_PATH, "PNG", optimize=True)
print(f"Masterpiece broadsheet saved at {OUT_PATH}! Size: {os.path.getsize(OUT_PATH)} bytes")
