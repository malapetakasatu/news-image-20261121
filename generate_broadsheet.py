import math
import os
from PIL import Image, ImageDraw, ImageFont

def generate_broadsheet(output_path):
    WIDTH, HEIGHT = 1024, 1024
    im = Image.new("RGB", (WIDTH, HEIGHT), "#fcf8f2") # Premium authentic broadsheet cream
    draw = ImageDraw.Draw(im)

    # Fonts
    font_serif_b = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
    font_serif_r = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
    font_serif_i = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
    font_sans_b = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    font_sans_r = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

    f_top = ImageFont.truetype(font_sans_b, 9.5)
    f_masthead = ImageFont.truetype(font_serif_b, 56)
    f_deck = ImageFont.truetype(font_serif_i, 14.5)
    
    f_stat_num = ImageFont.truetype(font_serif_b, 22)
    f_stat_label = ImageFont.truetype(font_sans_r, 7.5)
    f_region = ImageFont.truetype(font_sans_b, 8)

    f_hero_badge = ImageFont.truetype(font_sans_b, 8.5)
    f_hero_sub = ImageFont.truetype(font_sans_b, 8.5)
    f_hero_title = ImageFont.truetype(font_serif_b, 16.5)
    f_hero_body = ImageFont.truetype(font_serif_r, 9.5)
    f_source = ImageFont.truetype(font_sans_r, 7.5)
    f_pill = ImageFont.truetype(font_sans_b, 7)

    f_card_cat = ImageFont.truetype(font_sans_b, 7.5)
    f_card_head = ImageFont.truetype(font_serif_b, 10.5)
    f_card_body = ImageFont.truetype(font_serif_r, 8.5)

    f_map_pin = ImageFont.truetype(font_sans_b, 7)
    f_section_title = ImageFont.truetype(font_sans_b, 9.5)
    
    f_story_num = ImageFont.truetype(font_sans_b, 7.5)
    f_story_loc = ImageFont.truetype(font_sans_b, 7.5)
    f_story_desc = ImageFont.truetype(font_serif_r, 7.5)

    f_date_title = ImageFont.truetype(font_sans_b, 8.5)
    f_date_bold = ImageFont.truetype(font_sans_b, 7.5)
    f_date_text = ImageFont.truetype(font_sans_r, 7.5)
    f_footer = ImageFont.truetype(font_sans_r, 8)

    # Colors
    BLACK = "#0f172a"
    DARK_GREY = "#334155"
    LIGHT_GREY = "#64748b"
    LINE_COLOR = "#cbd5e1"
    RED_ACCENT = "#b91c1c"
    RED_DARK = "#991b1b"
    WHITE = "#ffffff"
    OFFICIAL_BLUE = "#1d4ed8"
    CONFIRMED_GREEN = "#15803d"
    REPORTED_MUSTARD = "#b45309"

    def rect(x1, y1, x2, y2, fill=None, outline=None, width=1):
        draw.rectangle([int(x1), int(y1), int(x2), int(y2)], fill=fill, outline=outline, width=width)

    def pill(x1, y1, x2, y2, fill=None, outline=None, r=3):
        draw.rounded_rectangle([int(x1), int(y1), int(x2), int(y2)], radius=r, fill=fill, outline=outline)

    # 1. TOP HEADER BANNER (y: 0 to 22)
    rect(0, 0, WIDTH, 22, fill=RED_ACCENT)
    draw.text((15, 5), "THE WORLD IN ONE DAY · 37 STORIES · 9 REGIONS · STRICT 24-HOUR UTC RECORD", fill=WHITE, font=f_top)
    draw.text((WIDTH - 15, 5), "VERIFIED WIRE SOURCES · SATURDAY 21 NOVEMBER 2026", fill=WHITE, font=f_top, anchor="ra")

    # 2. PROMINENT MASTHEAD (y: 26 to 104)
    draw.text((WIDTH // 2, 54), "Saturday 21 November 2026", fill=BLACK, font=f_masthead, anchor="mm")
    draw.text((WIDTH // 2, 92), "COP31 climate talks run into overtime   ·   missiles over Riyadh   ·   a deep quake shakes Peru", fill=DARK_GREY, font=f_deck, anchor="mm")
    draw.line([(15, 108), (WIDTH - 15, 108)], fill=BLACK, width=2)
    draw.line([(15, 111), (WIDTH - 15, 111)], fill=BLACK, width=1)

    # 3. 6 BIG METRICS STRIP (y: 116 to 164)
    stats = [
        ("3", "missiles shot down over Riyadh"),
        ("6.7", "magnitude of Peru deep quake"),
        ("DAY 13", "of COP31 in Antalya overtime"),
        ("$58,983", "Bitcoin price early Saturday"),
        ("128", "states back Geneva AI arms talks"),
        ("124*", "K L Rahul's score at tea, NZ Test"),
    ]
    stat_w = (WIDTH - 30) // 6
    for i, (num, label) in enumerate(stats):
        sx = 15 + i * stat_w
        if i > 0:
            draw.line([(sx, 120), (sx, 160)], fill=LINE_COLOR, width=1)
        draw.text((sx + stat_w // 2, 131), num, fill=RED_ACCENT if i in [0, 1, 2] else BLACK, font=f_stat_num, anchor="mm")
        words = label.split(" ")
        mid = len(words) // 2
        line1 = " ".join(words[:mid]) if mid > 0 else label
        line2 = " ".join(words[mid:]) if mid > 0 else ""
        draw.text((sx + stat_w // 2, 148), line1, fill=DARK_GREY, font=f_stat_label, anchor="mm")
        if line2:
            draw.text((sx + stat_w // 2, 157), line2, fill=DARK_GREY, font=f_stat_label, anchor="mm")

    # 4. 9 REGIONS BAR (y: 168 to 184)
    regions = [
        ("Europe · 5", "#1e40af", 110),
        ("Mid-East · 6", "#b91c1c", 115),
        ("S. Asia · 4", "#b45309", 110),
        ("E. Asia · 4", "#047857", 110),
        ("SE. Asia · 4", "#0e7490", 110),
        ("Africa · 3", "#6b21a8", 110),
        ("N. America · 4", "#374151", 110),
        ("Latin Am · 4", "#c2410c", 110),
        ("Oceania · 3", "#0f766e", 109),
    ]
    rx = 15
    for name, col, rw in regions:
        rect(rx, 168, rx + rw, 184, fill=col)
        draw.text((rx + rw // 2, 176), name, fill=WHITE, font=f_region, anchor="mm")
        rx += rw

    # 5. THREE HERO PANELS (y: 190 to 424)
    hero_w = (WIDTH - 42) // 3
    
    # --- HERO 1: MISSILES OVER RIYADH (x: 15 to 337) ---
    h1_x = 15
    rect(h1_x, 190, h1_x + hero_w, 210, fill=RED_ACCENT)
    draw.text((h1_x + 8, 200), "MISSILES OVER RIYADH", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h1_x + hero_w - 78, 194, h1_x + hero_w - 6, 206, fill=WHITE, r=2)
    draw.text((h1_x + hero_w - 42, 200), "3 SHOT DOWN", fill=RED_ACCENT, font=f_pill, anchor="mm")
    
    # Graphic Box 1 (Night Skyline & Interception Arcs)
    rect(h1_x, 210, h1_x + hero_w, 300, fill="#070d1e", outline=LINE_COLOR)
    for bx, bh, bw in [(0, 35, 25), (28, 55, 30), (62, 35, 20), (86, 65, 35), (125, 40, 22), 
                       (150, 70, 32), (185, 50, 28), (216, 60, 30), (250, 38, 25), (278, 55, 35)]:
        draw.rectangle([h1_x + bx, 300 - bh, h1_x + bx + bw, 300], fill="#02050d")
        for wy in range(300 - bh + 6, 296, 8):
            for wx in range(h1_x + bx + 4, h1_x + bx + bw - 4, 6):
                if (wx + wy) % 5 != 0:
                    draw.rectangle([wx, wy, wx + 2, wy + 3], fill="#ffea78" if (wx * wy) % 3 == 0 else "#38bdf8")
    
    arcs = [
        ([(h1_x + 30, 295), (h1_x + 80, 240), (h1_x + 140, 235)], "#ffdd44"),
        ([(h1_x + 280, 295), (h1_x + 230, 245), (h1_x + 175, 238)], "#ff9933"),
        ([(h1_x + 20, 290), (h1_x + 100, 260), (h1_x + 210, 248)], "#ffffff"),
    ]
    for pts, col in arcs:
        for t in range(50):
            u = t / 50.0
            px = (1-u)**2 * pts[0][0] + 2*(1-u)*u*pts[1][0] + u**2*pts[2][0]
            py = (1-u)**2 * pts[0][1] + 2*(1-u)*u*pts[1][1] + u**2*pts[2][1]
            draw.point((px, py), fill=col)
            draw.point((px+1, py), fill=col)
    
    for cx, cy in [(h1_x + 140, 235), (h1_x + 175, 238), (h1_x + 210, 248)]:
        draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill="#ffeedd")
        for dx, dy in [(-8, 0), (8, 0), (0, -8), (0, 8), (-6, -6), (6, 6), (-6, 6), (6, -6)]:
            draw.line([(cx, cy), (cx + dx, cy + dy)], fill="#ffcc00", width=1)
            
    pill(h1_x + 8, 283, h1_x + 102, 296, fill="#000000", r=2)
    draw.text((h1_x + 55, 289), "Coalition statement", fill=WHITE, font=f_pill, anchor="mm")
    
    # Content 1
    rect(h1_x, 300, h1_x + hero_w, 424, fill=WHITE, outline=LINE_COLOR)
    draw.text((h1_x + 8, 308), "1 · RIYADH · SAUDI ARABIA", fill=RED_ACCENT, font=f_pill)
    draw.text((h1_x + 8, 320), "Saudi defences down three\nmissiles aimed at the capital", fill=BLACK, font=f_hero_title, spacing=2)
    draw.text((h1_x + 8, 362), "Third night of alerts in a row: blasts heard over capital\nat 02:00, no damage or casualties. IRGC also claims\nstrikes on Gulf maritime radar positions.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h1_x + 8, 412), "(Reuters · AFP · Coalition statement)", fill=LIGHT_GREY, font=f_source)
    pill(h1_x + hero_w - 48, 407, h1_x + hero_w - 8, 419, fill=OFFICIAL_BLUE, r=2)
    draw.text((h1_x + hero_w - 28, 413), "OFFICIAL", fill=WHITE, font=f_pill, anchor="mm")

    # --- HERO 2: COP31 IN OVERTIME (x: 350 to 672) ---
    h2_x = 15 + hero_w + 6
    rect(h2_x, 190, h2_x + hero_w, 210, fill=RED_ACCENT)
    draw.text((h2_x + 8, 200), "COP31 IN OVERTIME", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h2_x + hero_w - 95, 194, h2_x + hero_w - 6, 206, fill=WHITE, r=2)
    draw.text((h2_x + hero_w - 50, 200), "NO DEAL · DAY 13", fill=RED_ACCENT, font=f_pill, anchor="mm")
    
    # Graphic Box 2 (Globe, Thermometer, Clock)
    rect(h2_x, 210, h2_x + hero_w, 300, fill="#e8f3fa", outline=LINE_COLOR)
    gx, gy = h2_x + 48, 255
    draw.ellipse([gx - 26, gy - 26, gx + 26, gy + 26], fill="#3498db", outline="#2980b9")
    draw.chord([gx - 20, gy - 14, gx + 6, gy + 12], 40, 220, fill="#2ecc71")
    draw.chord([gx - 8, gy - 22, gx + 20, gy - 2], 120, 310, fill="#27ae60")
    pill(h2_x + 10, 283, h2_x + 65, 296, fill="#000000", r=2)
    draw.text((h2_x + 37, 289), "AP · AFP", fill=WHITE, font=f_pill, anchor="mm")
    
    tx = h2_x + 142
    rect(tx - 4, 222, tx + 4, 280, fill=WHITE, outline="#95a5a6")
    draw.ellipse([tx - 11, 272, tx + 11, 294], fill=RED_ACCENT, outline="#95a5a6")
    rect(tx - 2, 238, tx + 2, 278, fill=RED_ACCENT)
    draw.text((tx + 18, 228), "+1.5°C", fill=RED_ACCENT, font=f_pill)
    draw.text((tx + 18, 238), "THRESHOLD", fill=RED_ACCENT, font=f_pill)
    
    cx, cy = h2_x + 248, 255
    draw.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=WHITE, outline="#2c3e50", width=2)
    draw.line([(cx, cy), (cx + 10, cy - 7)], fill=BLACK, width=2)
    draw.line([(cx, cy), (cx + 2, cy - 14)], fill=BLACK, width=2)
    pill(cx - 22, 283, cx + 22, 296, fill="#000000", r=2)
    draw.text((cx, 289), "DAY 13", fill=WHITE, font=f_pill, anchor="mm")

    # Content 2
    rect(h2_x, 300, h2_x + hero_w, 424, fill=WHITE, outline=LINE_COLOR)
    draw.text((h2_x + 8, 308), "2 · ANTALYA · TÜRKIYE", fill=RED_ACCENT, font=f_pill)
    draw.text((h2_x + 8, 320), "Climate summit deadlocked\nas talks run into overtime", fill=BLACK, font=f_hero_title, spacing=2)
    draw.text((h2_x + 8, 362), "A draft omitting fossil fuel phaseout split 200 nations.\nEU and island states reject text; 130+ countries demand\nthey remain named. Talks paused overnight.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h2_x + 8, 412), "(AP · AFP · Al Jazeera)", fill=LIGHT_GREY, font=f_source)
    pill(h2_x + hero_w - 56, 407, h2_x + hero_w - 8, 419, fill=CONFIRMED_GREEN, r=2)
    draw.text((h2_x + hero_w - 32, 413), "CONFIRMED", fill=WHITE, font=f_pill, anchor="mm")

    # --- HERO 3: QUAKE IN PERU (x: 686 to 1008) ---
    h3_x = 15 + (hero_w + 6) * 2
    rect(h3_x, 190, h3_x + hero_w, 210, fill=RED_ACCENT)
    draw.text((h3_x + 8, 200), "DEEP QUAKE IN PERU", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h3_x + hero_w - 138, 194, h3_x + hero_w - 6, 206, fill=WHITE, r=2)
    draw.text((h3_x + hero_w - 72, 200), "00:09 UTC · 108 KM DEEP", fill=RED_ACCENT, font=f_pill, anchor="mm")
    
    # Graphic Box 3 (Mountains, Seismograph wave, House)
    rect(h3_x, 210, h3_x + hero_w, 300, fill="#f9f2e7", outline=LINE_COLOR)
    seismo_pts = [
        (h3_x + 10, 245), (h3_x + 40, 245), (h3_x + 45, 240), (h3_x + 50, 250),
        (h3_x + 55, 230), (h3_x + 60, 260), (h3_x + 65, 220), (h3_x + 70, 265),
        (h3_x + 75, 235), (h3_x + 80, 252), (h3_x + 85, 242), (h3_x + 95, 245),
        (h3_x + 120, 245), (h3_x + 125, 233), (h3_x + 130, 257), (h3_x + 135, 225),
        (h3_x + 140, 270), (h3_x + 145, 235), (h3_x + 150, 250), (h3_x + 180, 245)
    ]
    for k in range(len(seismo_pts) - 1):
        draw.line([seismo_pts[k], seismo_pts[k+1]], fill=RED_ACCENT, width=2)
    
    draw.text((h3_x + 12, 220), "6.7", fill=RED_ACCENT, font=f_stat_num)
    draw.text((h3_x + 130, 221), "00:09 UTC", fill=DARK_GREY, font=f_pill)
    
    draw.polygon([(h3_x + 160, 298), (h3_x + 205, 245), (h3_x + 235, 265), (h3_x + 265, 230), (h3_x + 310, 298)], fill="#935116")
    draw.polygon([(h3_x + 185, 298), (h3_x + 225, 255), (h3_x + 270, 298)], fill="#784212")
    
    hx = h3_x + 235
    rect(hx, 268, hx + 38, 296, fill="#fdfefe", outline="#34495e", width=1)
    draw.polygon([(hx - 4, 268), (hx + 19, 252), (hx + 42, 268)], fill="#c0392b", outline="#922b21")
    rect(hx + 12, 278, hx + 24, 296, fill="#7f8c8d")
    
    pill(h3_x + hero_w - 65, 283, h3_x + hero_w - 10, 296, fill="#000000", r=2)
    draw.text((h3_x + hero_w - 37, 289), "USGS · IGP", fill=WHITE, font=f_pill, anchor="mm")

    # Content 3
    rect(h3_x, 300, h3_x + hero_w, 424, fill=WHITE, outline=LINE_COLOR)
    draw.text((h3_x + 8, 308), "3 · CARHUAMAYO · PERU", fill=RED_ACCENT, font=f_pill)
    draw.text((h3_x + 8, 320), "Magnitude 6.7 quake rattles\ncentral Peru, felt in Lima", fill=BLACK, font=f_hero_title, spacing=2)
    draw.text((h3_x + 8, 362), "A deep tremor struck near Carhuamayo at 00:09 UTC.\nPeru's geophysical institute reported zero deaths, no major\nstructural collapses, and no Pacific tsunami risk.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h3_x + 8, 412), "(USGS · IGP Lima)", fill=LIGHT_GREY, font=f_source)
    pill(h3_x + hero_w - 48, 407, h3_x + hero_w - 8, 419, fill=OFFICIAL_BLUE, r=2)
    draw.text((h3_x + hero_w - 28, 413), "OFFICIAL", fill=WHITE, font=f_pill, anchor="mm")

    # 6. 10 SECONDARY STORY CARDS: 2 ROWS (Cards 4 to 13, y: 432 to 596)
    card_w = (WIDTH - 54) // 5
    card_h = 78
    
    cards_row1 = [
        ("4 · KYIV WARNING", "Zelensky: Crimea bridge\n\"will not stay\"", "Warns of strikes ahead.", "(NBC)", "REPORTED", REPORTED_MUSTARD, "bridge"),
        ("5 · HORMUZ DRONE", "Iran says it downed a US\ndrone in Gulf", "Tehran claims; US silent.", "(IRIB)", "REPORTED", REPORTED_MUSTARD, "drone"),
        ("6 · SINALOA RAID", "Mexico captures 'El\nChapo Isidro'", "FBI top-10 fugitive held.", "(AP · PGR)", "CONFIRMED", CONFIRMED_GREEN, "cartel"),
        ("7 · GENEVA ARMS", "128 states back talks\non 'killer robots'", "UN ends without treaty.", "(Reuters)", "OFFICIAL", OFFICIAL_BLUE, "robot"),
        ("8 · MERCURY ORBIT", "BepiColombo probe\nenters Mercury orbit", "18:24 UTC orbit burn.", "(ESA · JAXA)", "OFFICIAL", OFFICIAL_BLUE, "orbit"),
    ]

    cards_row2 = [
        ("9 · BRUSSELS PACT", "EU and Indonesia sign\ntrade agreement", "Lifts 98.5% of tariffs.", "(EU · Antara)", "OFFICIAL", OFFICIAL_BLUE, "trade"),
        ("10 · CANBERRA AI", "Australia and China agree\nto AI talks", "Albanese wraps up trip.", "(ABC)", "OFFICIAL", OFFICIAL_BLUE, "bubbles"),
        ("11 · BITCOIN $58,983", "Bitcoin slips below\n$59,000 level", "Down 3.9% in 24 hours.", "(CoinGecko)", "CONFIRMED", CONFIRMED_GREEN, "btc"),
        ("12 · TWICKENHAM", "England beat All Blacks\nby record 37-12", "Historic rugby test win.", "(BBC)", "OFFICIAL", OFFICIAL_BLUE, "rugby"),
        ("13 · RAHUL 124*", "Rahul century puts India\non top vs NZ", "India 344-2 at tea.", "(AFP)", "OFFICIAL", OFFICIAL_BLUE, "cricket"),
    ]

    def draw_card_icon(icon_type, cx, cy):
        if icon_type == "bridge":
            draw.line([(cx - 20, cy + 6), (cx + 20, cy + 6)], fill=BLACK, width=1)
            draw.line([(cx - 8, cy - 6), (cx - 8, cy + 6)], fill=BLACK, width=2)
            draw.line([(cx + 8, cy - 6), (cx + 8, cy + 6)], fill=BLACK, width=2)
            draw.arc([cx - 24, cy - 8, cx + 8, cy + 16], 210, 330, fill=RED_ACCENT, width=1)
            draw.arc([cx - 8, cy - 8, cx + 24, cy + 16], 210, 330, fill=RED_ACCENT, width=1)
        elif icon_type == "drone":
            draw.line([(cx - 14, cy), (cx + 14, cy)], fill="#2c3e50", width=2)
            draw.line([(cx, cy - 5), (cx, cy + 5)], fill="#2c3e50", width=2)
            draw.line([(cx - 6, cy - 5), (cx - 6, cy + 5)], fill="#2c3e50", width=1)
            draw.line([(cx + 6, cy - 5), (cx + 6, cy + 5)], fill="#2c3e50", width=1)
            draw.ellipse([cx + 10, cy - 3, cx + 16, cy + 3], fill=RED_ACCENT)
        elif icon_type == "cartel":
            draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill="#fee2e2", outline=RED_DARK)
            draw.text((cx, cy), "$5M", fill=RED_DARK, font=f_pill, anchor="mm")
        elif icon_type == "robot":
            draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill="#f3e8ff", outline="#7e22ce")
            draw.text((cx, cy), "AI", fill="#7e22ce", font=f_pill, anchor="mm")
        elif icon_type == "orbit":
            draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill="#fef3c7", outline="#b45309")
            draw.text((cx, cy), "☿", fill="#b45309", font=f_card_head, anchor="mm")
        elif icon_type == "trade":
            draw.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill="#dbeafe", outline=OFFICIAL_BLUE)
            draw.text((cx, cy), "98%", fill=OFFICIAL_BLUE, font=f_pill, anchor="mm")
        elif icon_type == "bubbles":
            draw.ellipse([cx - 12, cy - 6, cx + 2, cy + 6], fill="#e8f8f5", outline="#16a085")
            draw.ellipse([cx - 2, cy - 3, cx + 12, cy + 9], fill="#e8f8f5", outline="#16a085")
            draw.text((cx - 6, cy - 3), "··", fill="#16a085", font=f_pill)
        elif icon_type == "btc":
            draw.ellipse([cx - 12, cy - 6, cx + 2, cy + 6], fill="#f39c12", outline="#d68910")
            draw.text((cx - 5, cy - 4), "₿", fill=WHITE, font=f_pill)
            draw.text((cx + 6, cy - 2), "-3.9%", fill=RED_ACCENT, font=f_pill)
        elif icon_type == "rugby":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#dcfce7", outline=CONFIRMED_GREEN)
            draw.text((cx, cy), "37-12", fill=CONFIRMED_GREEN, font=f_pill, anchor="mm")
        elif icon_type == "cricket":
            draw.line([(cx - 10, cy + 6), (cx + 4, cy - 5)], fill="#b7950b", width=3)
            draw.ellipse([cx + 7, cy - 3, cx + 13, cy + 3], fill=RED_ACCENT)
            draw.text((cx + 6, cy + 4), "124*", fill=BLACK, font=f_pill)

    for row_idx, cards in enumerate([cards_row1, cards_row2]):
        cy = 432 if row_idx == 0 else 516
        for i, (cat, title, body, src, p_text, p_col, icon) in enumerate(cards):
            cx = 15 + i * (card_w + 6)
            rect(cx, cy, cx + card_w, cy + 15, fill=RED_ACCENT if row_idx == 0 and i < 2 else BLACK)
            draw.text((cx + 4, cy + 8), cat, fill=WHITE, font=f_card_cat, anchor="lm")
            rect(cx, cy + 15, cx + card_w, cy + card_h, fill=WHITE, outline=LINE_COLOR)
            draw_card_icon(icon, cx + card_w // 2, cy + 26)
            draw.text((cx + 4, cy + 37), title, fill=BLACK, font=f_card_head, spacing=1)
            draw.text((cx + 4, cy + 63), src, fill=LIGHT_GREY, font=f_source)
            pill(cx + card_w - 42, cy + 59, cx + card_w - 3, cy + 70, fill=p_col, r=2)
            draw.text((cx + card_w - 22, cy + 64), p_text, fill=WHITE, font=f_pill, anchor="mm")

    # DIVIDER LINE
    draw.line([(15, 602), (WIDTH - 15, 602)], fill=LINE_COLOR, width=1)

    # 7. BOTTOM SECTION: MAP (Left) & 24 MORE STORIES (Right) (y: 608 to 852)
    draw.text((15, 608), "WHERE IT HAPPENED — STORIES 1-13 ON THE GLOBAL MAP", fill=BLACK, font=f_section_title)
    draw.text((468, 608), "ALSO ON SATURDAY 21 NOVEMBER 2026 — 24 MORE DATED STORIES", fill=BLACK, font=f_section_title)

    # MAP BOX (x: 15 to 455, y: 622 to 852)
    rect(15, 622, 455, 852, fill="#eef3f7", outline=LINE_COLOR)

    def map_coord(lon, lat):
        mx = 15 + int((lon + 172) / 350 * 440)
        my = 622 + int((75 - lat) / 130 * 230)
        return (mx, my)

    continents = [
        # North America
        [(-168, 65), (-140, 70), (-120, 70), (-95, 72), (-80, 62), (-60, 60), (-55, 48),
         (-65, 44), (-75, 35), (-80, 25), (-82, 30), (-97, 26), (-105, 20), (-90, 16),
         (-80, 9), (-85, 12), (-100, 18), (-106, 23), (-115, 30), (-124, 38), (-125, 48),
         (-135, 58), (-165, 60), (-168, 65)],
        # South America
        [(-77, 10), (-60, 8), (-50, 0), (-35, -5), (-38, -15), (-45, -23), (-55, -35),
         (-65, -45), (-70, -55), (-75, -48), (-72, -35), (-70, -20), (-78, -5), (-80, 2), (-77, 10)],
        # Africa
        [(-17, 32), (-5, 36), (10, 37), (25, 32), (32, 31), (35, 25), (43, 12), (51, 10),
         (45, 0), (40, -10), (35, -25), (28, -34), (18, -34), (12, -20), (9, 4), (0, 6),
         (-15, 12), (-17, 22), (-17, 32)],
        # Europe
        [(-10, 36), (-9, 43), (0, 48), (-5, 58), (5, 62), (15, 55), (10, 70), (28, 70),
         (30, 60), (35, 50), (28, 42), (22, 38), (15, 40), (0, 36), (-10, 36)],
        # Asia
        [(30, 60), (60, 68), (100, 72), (140, 70), (170, 65), (160, 52), (140, 48),
         (130, 35), (120, 30), (110, 20), (105, 10), (100, 5), (95, 15), (80, 10),
         (75, 22), (68, 25), (60, 25), (55, 15), (45, 12), (35, 25), (35, 38), (35, 50), (30, 60)],
        # Australia
        [(115, -22), (130, -12), (142, -11), (146, -20), (153, -28), (150, -37),
         (140, -38), (130, -32), (115, -35), (113, -25), (115, -22)]
    ]

    for poly in continents:
        pts = [map_coord(lon, lat) for lon, lat in poly]
        draw.polygon(pts, fill="#ded0b6", outline="#c5b597")

    pins = [
        (1, 47, 25),     # Riyadh
        (2, 31, 37),     # Antalya
        (3, -75, -11),   # Junin / Peru
        (4, 30, 50),     # Kyiv
        (5, 56, 27),     # Hormuz
        (6, -107, 25),   # Sinaloa
        (7, 6, 46),      # Geneva
        (8, 0, 0),       # Mercury / Space orbit
        (9, 4, 50),      # Brussels
        (10, 149, -35),  # Canberra
        (11, -74, 41),   # Bitcoin / NY
        (12, -0.1, 51),  # Twickenham
        (13, 175, -41),  # Wellington
    ]

    for num, lon, lat in pins:
        if num == 8:
            px, py = 15 + 35, 852 - 18
            pill(px - 14, py - 7, px + 26, py + 7, fill="#0f172a", r=2)
            draw.text((px + 6, py), "8 Orbit", fill=WHITE, font=f_pill, anchor="mm")
            continue
        px, py = map_coord(lon, lat)
        draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED_ACCENT if num <= 3 else OFFICIAL_BLUE, outline=WHITE, width=1)
        draw.text((px, py), str(num), fill=WHITE, font=f_map_pin, anchor="mm")

    # 24 DATED STORIES (Stories 14 to 37)
    stories_col1 = [
        ("14", "Jerusalem:", "Eisenkot invites Likud to coalition talks (TOI)"),
        ("15", "Gaza City:", "Missile strike on food vehicle kills 3 (Reuters)"),
        ("16", "Antalya:", "EU warns COP31 risks 'fossil summit' (AFP)"),
        ("17", "Antalya:", "Panama threatens to block climate text (AJ)"),
        ("18", "Antalya:", "Indonesia PLN signs clean-power deals (Antara)"),
        ("19", "Yemen:", "Houthis threaten Jeddah and Red Sea ports (AJ)"),
        ("20", "Washington:", "Trump confirms FBI database breach (Reuters)"),
        ("21", "Washington:", "SpaceX Pentagon launch funding row (CNN)"),
        ("22", "Texas:", "70-year-old's execution takes 63 min (ABC)"),
        ("23", "Los Angeles:", "Jury convicts Palisades arsonist (ABC)"),
        ("24", "Missouri:", "Judge approves $7.25bn settlement (AFP)"),
        ("25", "Vancouver:", "Defence rests in landmark climate trial (AFP)"),
    ]

    stories_col2 = [
        ("26", "Pyongyang:", "Kim tours factories after summit (KCNA)"),
        ("27", "Sejong:", "Freight train derails; zero casualties (K. Herald)"),
        ("28", "Taipei:", "Budget and cash payout passed (T. Times)"),
        ("29", "Bangkok:", "Arsenic reduction plan for two rivers (Nation)"),
        ("30", "Mastung:", "Pakistan forces kill 15 militants in raid (Dawn)"),
        ("31", "Qinghai:", "M5.9 quake at 14:45 UTC in west China (USGS)"),
        ("32", "Dublin:", "Ireland beat champions South Africa 20-17 (RTE)"),
        ("33", "Turin:", "Alcaraz beats Shelton in ATP Finals semi (ATP)"),
        ("34", "Melbourne:", "Australia beat England in 1st T20 (Cricket Aus)"),
        ("35", "Nigeria:", "Funeral boat death toll reaches 24 (NEMA)"),
        ("36", "Serang:", "Sweet factory fire kills 4, 36 injured (Antara)"),
        ("37", "Las Vegas:", "Verstappen sent to stewards over lap (Autosport)"),
    ]

    start_y = 626
    row_gap = 18.8
    for i, (num, loc, desc) in enumerate(stories_col1):
        sy = int(start_y + i * row_gap)
        draw.text((468, sy), num, fill=RED_ACCENT, font=f_story_num)
        draw.text((484, sy), loc, fill=BLACK, font=f_story_loc)
        draw.text((546, sy), desc, fill=DARK_GREY, font=f_story_desc)

    for i, (num, loc, desc) in enumerate(stories_col2):
        sy = int(start_y + i * row_gap)
        draw.text((742, sy), num, fill=RED_ACCENT, font=f_story_num)
        draw.text((758, sy), loc, fill=BLACK, font=f_story_loc)
        draw.text((820, sy), desc, fill=DARK_GREY, font=f_story_desc)

    # 8. DATE CHECK BOX (y: 860 to 975)
    rect(15, 860, WIDTH - 15, 975, fill="#fdfaf5", outline=RED_ACCENT, width=1)
    rect(15, 860, WIDTH - 15, 878, fill=RED_ACCENT)
    draw.text((24, 869), "DATE CHECK — WELL-KNOWN STORIES EXCLUDED BECAUSE THEY OCCURRED ON OTHER CALENDAR DAYS", fill=WHITE, font=f_date_title, anchor="lm")
    
    draw.text((24, 886), "LEFT OUT (FRIDAY 20 NOV):", fill=RED_DARK, font=f_date_bold)
    draw.text((180, 886), "Wall Street fall into correction · Russian barrage on Kyiv bridges · missile in Poland · UK-EU deal ·", fill=DARK_GREY, font=f_date_text)
    draw.text((24, 902), "Cyclone Akvan landfall · Denmark expels Russian attaché · Kryvyi Rih strike · Harry Kane injury · Manipur illicit brew date.", fill=DARK_GREY, font=f_date_text)

    draw.text((24, 922), "NOT YET (SUNDAY 22 NOV):", fill=OFFICIAL_BLUE, font=f_date_bold)
    draw.text((180, 922), "Verstappen wins Las Vegas GP race · COP31 formal approval session · India declare at 720-8 · Liverpool vs Man Utd.", fill=DARK_GREY, font=f_date_text)

    draw.text((24, 942), "STRICT 24H RECORD:", fill=CONFIRMED_GREEN, font=f_date_bold)
    draw.text((180, 942), "Every story on this broadsheet occurred or was first reported on Saturday 21 November 2026 (UTC).", fill=DARK_GREY, font=f_date_text)
    draw.text((24, 958), "Cross-checked across primary wire services: Reuters, AP, AFP, USGS, ESA, JAXA, BBC, Formula 1, ESPNcricinfo. Original vector drawings.", fill=LIGHT_GREY, font=f_date_text)

    # 9. FOOTER VERIFICATION KEY (y: 985 to 1014)
    draw.line([(15, 985), (WIDTH - 15, 985)], fill=LINE_COLOR, width=1)
    draw.text((15, 994), "Sources named beside each story · Original drawings · HOW WE CHECKED: CONFIRMED = 2+ outlets · OFFICIAL = on the record · REPORTED = one outlet", fill=DARK_GREY, font=f_footer)
    draw.text((WIDTH - 15, 994), "THE GLOBAL BROADSHEET · SATURDAY 21 NOVEMBER 2026 · EDITION 14,892", fill=LIGHT_GREY, font=f_footer, anchor="ra")

    im.save(output_path, "PNG", optimize=True)
    print(f"Masterpiece broadsheet saved at {output_path}! Dimensions: {im.size}, Bytes: {os.path.getsize(output_path)}")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "entry.png")
    generate_broadsheet(out)
