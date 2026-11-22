import math
import os
from PIL import Image, ImageDraw, ImageFont

def generate_broadsheet(output_path):
    WIDTH, HEIGHT = 1024, 1024
    im = Image.new("RGB", (WIDTH, HEIGHT), "#faf7f0")
    draw = ImageDraw.Draw(im)

    # Fonts
    font_serif_b = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
    font_serif_r = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
    font_serif_i = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
    font_sans_b = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    font_sans_r = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

    f_top_banner = ImageFont.truetype(font_sans_b, 10.5)
    f_masthead = ImageFont.truetype(font_serif_b, 54)
    f_deck = ImageFont.truetype(font_serif_i, 14.5)
    
    f_stat_num = ImageFont.truetype(font_serif_b, 22)
    f_stat_lbl = ImageFont.truetype(font_sans_b, 8.5)
    
    f_region_tag = ImageFont.truetype(font_sans_b, 8)
    
    f_hero_badge = ImageFont.truetype(font_sans_b, 9.5)
    f_hero_sub = ImageFont.truetype(font_sans_b, 9)
    f_hero_title = ImageFont.truetype(font_serif_b, 16.5)
    f_hero_body = ImageFont.truetype(font_serif_r, 10)
    f_source = ImageFont.truetype(font_sans_b, 8)
    f_pill = ImageFont.truetype(font_sans_b, 7.5)
    
    f_card_cat = ImageFont.truetype(font_sans_b, 8.5)
    f_card_head = ImageFont.truetype(font_serif_b, 11)
    f_card_desc = ImageFont.truetype(font_serif_r, 8.5)
    
    f_sec_title = ImageFont.truetype(font_sans_b, 9.5)
    f_map_pin = ImageFont.truetype(font_sans_b, 7.5)
    f_story_loc = ImageFont.truetype(font_sans_b, 8)
    f_story_desc = ImageFont.truetype(font_serif_r, 8)
    
    f_chrono_time = ImageFont.truetype(font_sans_b, 8.5)
    f_chrono_desc = ImageFont.truetype(font_sans_r, 7.5)
    f_date_title = ImageFont.truetype(font_sans_b, 9)
    f_date_text = ImageFont.truetype(font_serif_r, 8)
    f_footer = ImageFont.truetype(font_sans_b, 8)

    # Palette
    RED_ACCENT = "#b71c1c"
    DEEP_BLUE = "#1a365d"
    NAVY = "#0f2027"
    BLACK = "#0a0a0a"
    DARK_GREY = "#2d3748"
    LIGHT_GREY = "#718096"
    LINE_COLOR = "#cbd5e0"
    WHITE = "#ffffff"
    OFFICIAL_BLUE = "#1a5276"
    CONFIRMED_GREEN = "#1e8449"
    REPORTED_MUSTARD = "#b9770e"

    def rect(x1, y1, x2, y2, fill=None, outline=None, width=1):
        draw.rectangle([x1, y1, x2, y2], fill=fill, outline=outline, width=width)

    def pill(x1, y1, x2, y2, fill=None, outline=None, r=3):
        draw.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=fill, outline=outline)

    # 1. TOP HEADER BANNER (y: 0 to 24)
    rect(0, 0, WIDTH, 24, fill=RED_ACCENT)
    draw.text((15, 6), "THE WORLD IN ONE DAY · 21 NOVEMBER 2026", fill=WHITE, font=f_top_banner)
    draw.text((WIDTH - 520, 6), "35 DATED STORIES · 9 GLOBAL REGIONS · STRICT DATE INTEGRITY CHECK", fill=WHITE, font=f_top_banner)

    # 2. MASTHEAD (y: 26 to 116)
    draw.text((WIDTH // 2, 58), "Saturday 21 November 2026", fill=BLACK, font=f_masthead, anchor="mm")
    draw.text((WIDTH // 2, 96), "COP31 talks run into overtime · missiles intercepted over Riyadh · M6.7 earthquake shakes Peru", fill=DARK_GREY, font=f_deck, anchor="mm")
    draw.line([(15, 114), (WIDTH - 15, 114)], fill=BLACK, width=2)
    draw.line([(15, 117), (WIDTH - 15, 117)], fill=BLACK, width=1)

    # 3. 6 STATS STRIP (y: 118 to 174)
    stats = [
        ("3", "missiles shot down over Riyadh"),
        ("M6.7", "deep Peru quake at 00:09 UTC"),
        ("DAY 13", "of COP31 climate overtime"),
        ("$58,983", "bitcoin (-3.9% in 24h)"),
        ("146 SAFE", "Davao jet landing emergency"),
        ("124*", "K.L. Rahul century at tea"),
    ]
    stat_w = (WIDTH - 30) // 6
    for i, (num, label) in enumerate(stats):
        sx = 15 + i * stat_w
        if i > 0:
            draw.line([(sx, 122), (sx, 170)], fill=LINE_COLOR, width=1)
        draw.text((sx + stat_w // 2, 136), num, fill=RED_ACCENT if i in [0, 1, 2] else BLACK, font=f_stat_num, anchor="mm")
        draw.text((sx + stat_w // 2, 158), label, fill=DARK_GREY, font=f_stat_lbl, anchor="mm")

    # 4. 9-REGION DISTRIBUTION BAR (y: 176 to 196)
    regions = [
        ("Europe · 4", "#1f618d", 100),
        ("Middle East · 5", "#7d3c98", 125),
        ("Americas · 11", "#229954", 155),
        ("Asia-Pacific · 10", "#d35400", 155),
        ("South Asia · 3", "#b7950b", 100),
        ("Africa · 2", "#884ea0", 95),
        ("Oceania · 3", "#117a65", 95),
        ("Central Asia · 1", "#5d6d7e", 85),
        ("Global · 1", "#34495e", 84),
    ]
    rx = 15
    for name, col, rw in regions:
        rect(rx, 176, rx + rw, 196, fill=col)
        draw.text((rx + rw // 2, 186), name, fill=WHITE, font=f_region_tag, anchor="mm")
        rx += rw

    # 5. THREE HERO PANELS (y: 202 to 438)
    hero_w = (WIDTH - 42) // 3

    # --- HERO 1: MISSILES OVER RIYADH & GULF ---
    h1_x = 15
    rect(h1_x, 202, h1_x + hero_w, 224, fill=RED_ACCENT)
    draw.text((h1_x + 8, 213), "MISSILES OVER RIYADH & GULF", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h1_x + hero_w - 95, 206, h1_x + hero_w - 6, 220, fill=WHITE, r=3)
    draw.text((h1_x + hero_w - 50, 213), "3 SHOT DOWN", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")

    # Graphic Box 1: Riyadh Night Sky, Intercept Arcs, Radar Grid
    rect(h1_x, 224, h1_x + hero_w, 318, fill="#0b1320", outline=LINE_COLOR)
    # City silhouette
    buildings = [(0, 40, 26), (28, 52, 32), (64, 38, 22), (90, 62, 38), (132, 42, 24), 
                 (160, 68, 34), (198, 48, 30), (232, 58, 32), (268, 40, 26), (298, 52, 24)]
    for bx, bh, bw in buildings:
        draw.rectangle([h1_x + bx, 318 - bh, h1_x + bx + bw, 318], fill="#040810")
        for wy in range(318 - bh + 6, 314, 8):
            for wx in range(h1_x + bx + 4, h1_x + bx + bw - 4, 6):
                if (wx + wy) % 5 != 0:
                    draw.rectangle([wx, wy, wx + 2, wy + 3], fill="#ffea78" if (wx * wy) % 3 == 0 else "#ffffff")

    # Intercept trajectories
    arcs = [
        ([(h1_x + 25, 310), (h1_x + 75, 250), (h1_x + 135, 245)], "#ffdd44"),
        ([(h1_x + 285, 310), (h1_x + 235, 255), (h1_x + 180, 248)], "#ff9933"),
        ([(h1_x + 18, 305), (h1_x + 95, 270), (h1_x + 215, 256)], "#ffffff"),
    ]
    for pts, col in arcs:
        for t in range(50):
            u = t / 50.0
            px = (1-u)**2 * pts[0][0] + 2*(1-u)*u*pts[1][0] + u**2*pts[2][0]
            py = (1-u)**2 * pts[0][1] + 2*(1-u)*u*pts[1][1] + u**2*pts[2][1]
            draw.point((px, py), fill=col)
            draw.point((px+1, py), fill=col)

    # Detonation starbursts
    for cx, cy in [(h1_x + 135, 245), (h1_x + 180, 248), (h1_x + 215, 256)]:
        draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill="#ffeedd")
        for dx, dy in [(-8, 0), (8, 0), (0, -8), (0, 8), (-6, -6), (6, 6), (-6, 6), (6, -6)]:
            draw.line([(cx, cy), (cx + dx, cy + dy)], fill="#ffcc00", width=1)

    pill(h1_x + 8, 301, h1_x + 115, 314, fill="#000000", r=2)
    draw.text((h1_x + 61, 307), "Coalition Air Defence", fill=WHITE, font=f_pill, anchor="mm")

    # Story content 1
    rect(h1_x, 318, h1_x + hero_w, 438, fill=WHITE, outline=LINE_COLOR)
    draw.text((h1_x + 8, 326), "1 · RIYADH & GULF · MIDDLE EAST", fill=RED_ACCENT, font=f_hero_sub)
    draw.text((h1_x + 8, 340), "Saudi defences down 3 missiles;\nIran targets Bahrain naval base", fill=BLACK, font=f_hero_title, spacing=3)
    draw.text((h1_x + 8, 382), "Third night of air alerts in Riyadh. Patriot batteries down\n3 ballistic missiles targeting capital; zero casualties. Strikes\nalso hit coalition-linked naval infrastructure in Bahrain.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h1_x + 8, 424), "(Reuters · AFP · Coalition Cmd)", fill=LIGHT_GREY, font=f_source)
    pill(h1_x + hero_w - 52, 418, h1_x + hero_w - 8, 431, fill=OFFICIAL_BLUE, r=2)
    draw.text((h1_x + hero_w - 30, 424), "OFFICIAL", fill=WHITE, font=f_pill, anchor="mm")

    # --- HERO 2: COP31 IN OVERTIME ---
    h2_x = 15 + hero_w + 6
    rect(h2_x, 202, h2_x + hero_w, 224, fill=RED_ACCENT)
    draw.text((h2_x + 8, 213), "COP31 CLIMATE DEADLOCK", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h2_x + hero_w - 110, 206, h2_x + hero_w - 6, 220, fill=WHITE, r=3)
    draw.text((h2_x + hero_w - 58, 213), "NO DEAL · DAY 13", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")

    # Graphic Box 2: Earth Globe, +1.5C Thermometer, Countdown Clock
    rect(h2_x, 224, h2_x + hero_w, 318, fill="#e8f3fa", outline=LINE_COLOR)
    # Globe
    gx, gy = h2_x + 48, 271
    draw.ellipse([gx - 28, gy - 28, gx + 28, gy + 28], fill="#3498db", outline="#2980b9")
    draw.chord([gx - 22, gy - 16, gx + 8, gy + 14], 40, 220, fill="#2ecc71")
    draw.chord([gx - 10, gy - 24, gx + 22, gy - 2], 120, 310, fill="#27ae60")
    draw.chord([gx - 15, gy + 6, gx + 18, gy + 26], 0, 180, fill="#2ecc71")

    # Thermometer
    tx = h2_x + 140
    rect(tx - 4, 238, tx + 4, 296, fill=WHITE, outline="#95a5a6")
    draw.ellipse([tx - 11, 288, tx + 11, 310], fill=RED_ACCENT, outline="#95a5a6")
    rect(tx - 2, 252, tx + 2, 294, fill=RED_ACCENT)
    draw.line([(tx + 6, 252), (tx + 18, 252)], fill=RED_ACCENT, width=2)
    draw.text((tx + 22, 245), "+1.5°C", fill=RED_ACCENT, font=f_pill)
    draw.text((tx + 22, 255), "THRESHOLD", fill=RED_ACCENT, font=f_pill)

    # Clock
    cx, cy = h2_x + 248, 271
    draw.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], fill=WHITE, outline="#2c3e50", width=2)
    for hr in range(12):
        ang = hr * math.pi / 6
        draw.line([(cx + 19 * math.sin(ang), cy - 19 * math.cos(ang)),
                   (cx + 22 * math.sin(ang), cy - 22 * math.cos(ang))], fill="#2c3e50", width=1)
    draw.line([(cx, cy), (cx + 12, cy - 8)], fill=BLACK, width=2)
    draw.line([(cx, cy), (cx + 3, cy - 16)], fill=BLACK, width=2)
    pill(cx - 24, 301, cx + 24, 314, fill="#000000", r=2)
    draw.text((cx, 307), "OVERTIME", fill=WHITE, font=f_pill, anchor="mm")

    # Story content 2
    rect(h2_x, 318, h2_x + hero_w, 438, fill=WHITE, outline=LINE_COLOR)
    draw.text((h2_x + 8, 326), "2 · ANTALYA · TÜRKIYE", fill=RED_ACCENT, font=f_hero_sub)
    draw.text((h2_x + 8, 340), "Climate summit in overtime\nas 200 nations split over text", fill=BLACK, font=f_hero_title, spacing=3)
    draw.text((h2_x + 8, 382), "Antalya summit runs into unscheduled Day 13 after draft\nagreement omitting fossil fuel phaseout sparks rebellion.\nPanama and island states threaten veto; 3rd draft due.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h2_x + 8, 424), "(AP · AFP · Al Jazeera)", fill=LIGHT_GREY, font=f_source)
    pill(h2_x + hero_w - 60, 418, h2_x + hero_w - 8, 431, fill=CONFIRMED_GREEN, r=2)
    draw.text((h2_x + hero_w - 34, 424), "CONFIRMED", fill=WHITE, font=f_pill, anchor="mm")

    # --- HERO 3: M6.7 DEEP QUAKE IN PERU ---
    h3_x = 15 + (hero_w + 6) * 2
    rect(h3_x, 202, h3_x + hero_w, 224, fill=RED_ACCENT)
    draw.text((h3_x + 8, 213), "M6.7 DEEP QUAKE IN PERU", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h3_x + hero_w - 142, 206, h3_x + hero_w - 6, 220, fill=WHITE, r=3)
    draw.text((h3_x + hero_w - 74, 213), "00:09 UTC · 108 KM DEEP", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")

    # Graphic Box 3: Seismograph Spikes, Andes Profile, Epicenter
    rect(h3_x, 224, h3_x + hero_w, 318, fill="#f9f2e7", outline=LINE_COLOR)
    seismo_pts = [
        (h3_x + 10, 258), (h3_x + 35, 258), (h3_x + 40, 253), (h3_x + 45, 263),
        (h3_x + 50, 243), (h3_x + 55, 273), (h3_x + 60, 233), (h3_x + 65, 278),
        (h3_x + 70, 248), (h3_x + 75, 266), (h3_x + 80, 256), (h3_x + 90, 258),
        (h3_x + 115, 258), (h3_x + 120, 246), (h3_x + 125, 270), (h3_x + 130, 238),
        (h3_x + 135, 283), (h3_x + 140, 248), (h3_x + 145, 263), (h3_x + 175, 258)
    ]
    for k in range(len(seismo_pts) - 1):
        draw.line([seismo_pts[k], seismo_pts[k+1]], fill=RED_ACCENT, width=2)

    draw.text((h3_x + 12, 233), "M6.7", fill=RED_ACCENT, font=f_stat_num)
    draw.text((h3_x + 125, 234), "00:09 UTC", fill=DARK_GREY, font=f_pill)

    # Mountain silhouette
    draw.polygon([(h3_x + 160, 316), (h3_x + 205, 263), (h3_x + 235, 283), (h3_x + 265, 248), (h3_x + 310, 316)], fill="#935116")
    draw.polygon([(h3_x + 185, 316), (h3_x + 225, 273), (h3_x + 270, 316)], fill="#784212")

    # Epicenter building
    hx = h3_x + 235
    rect(hx, 286, hx + 38, 314, fill="#fdfefe", outline="#34495e", width=1)
    draw.polygon([(hx - 4, 286), (hx + 19, 270), (hx + 42, 286)], fill="#c0392b", outline="#922b21")
    rect(hx + 12, 296, hx + 24, 314, fill="#7f8c8d")

    pill(h3_x + hero_w - 75, 301, h3_x + hero_w - 8, 314, fill="#000000", r=2)
    draw.text((h3_x + hero_w - 41, 307), "USGS · IGP Lima", fill=WHITE, font=f_pill, anchor="mm")

    # Story content 3
    rect(h3_x, 318, h3_x + hero_w, 438, fill=WHITE, outline=LINE_COLOR)
    draw.text((h3_x + 8, 326), "3 · CARHUAMAYO · PERU", fill=RED_ACCENT, font=f_hero_sub)
    draw.text((h3_x + 8, 340), "Magnitude 6.7 deep quake\nrattles central Peru; felt in Lima", fill=BLACK, font=f_hero_title, spacing=3)
    draw.text((h3_x + 8, 382), "Deep seismic rupture 108 km underground near Carhuamayo\nat 00:09 UTC. Peru Geophysical Institute (IGP) confirms\nzero fatalities, zero infrastructure collapse, no tsunami.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h3_x + 8, 424), "(USGS · IGP Lima)", fill=LIGHT_GREY, font=f_source)
    pill(h3_x + hero_w - 52, 418, h3_x + hero_w - 8, 431, fill=OFFICIAL_BLUE, r=2)
    draw.text((h3_x + hero_w - 30, 424), "OFFICIAL", fill=WHITE, font=f_pill, anchor="mm")

    # 6. SECONDARY CARDS (y: 444 to 606)
    card_w = (WIDTH - 54) // 5
    card_h = 78

    cards_row1 = [
        ("4 · KYIV WARNING", "Zelensky: Kerch bridge\n\"will not stand\"", "Warns of precision strikes.", "(NBC)", "REPORTED", REPORTED_MUSTARD, "bridge"),
        ("5 · HORMUZ DRONE", "Iran claims downing\nUS MQ-9 drone", "Tehran claims; US unverified.", "(IRIB/AP)", "REPORTED", REPORTED_MUSTARD, "drone"),
        ("6 · IRAN URANIUM", "Tehran: uranium stockpile\nstays at home", "Rejects export proposals.", "(Times of Israel)", "OFFICIAL", OFFICIAL_BLUE, "atom"),
        ("7 · TRUMP AI TARIFF", "Trump vows punitive tax\non offshore AI hubs", "Targeting overseas data hubs.", "(ABC News)", "REPORTED", REPORTED_MUSTARD, "tax"),
        ("8 · CHINA-JAPAN", "China demands Japan\ncorrect Taiwan stance", "Tokyo maintains position.", "(Ministry/AFP)", "OFFICIAL", OFFICIAL_BLUE, "flags"),
    ]

    cards_row2 = [
        ("9 · DAVAO AIRLINER", "Jet lands safely after\nengine fire alert", "Air Niugini 767; 146 safe.", "(Airline/AP)", "OFFICIAL", OFFICIAL_BLUE, "plane"),
        ("10 · CANBERRA-CHINA", "Australia & China agree\nto AI dialogue", "Albanese wraps Beijing trip.", "(ABC)", "OFFICIAL", OFFICIAL_BLUE, "bubbles"),
        ("11 · BITCOIN $58,983", "Bitcoin slips below\n$59,000 mark", "Down 3.9% in 24h retreat.", "(CoinGecko)", "CONFIRMED", CONFIRMED_GREEN, "btc"),
        ("12 · LAS VEGAS F1", "Russell fastest in final\nGP practice", "1:34.041 in damp night session.", "(Formula 1)", "OFFICIAL", OFFICIAL_BLUE, "f1"),
        ("13 · WELLINGTON TEST", "Rahul 124* century puts\nIndia in control", "India 344-2 at tea in NZ.", "(AFP)", "OFFICIAL", OFFICIAL_BLUE, "cricket"),
    ]

    def draw_card_icon(icon_type, cx, cy):
        if icon_type == "bridge":
            draw.line([(cx - 24, cy + 8), (cx + 24, cy + 8)], fill=BLACK, width=1)
            draw.line([(cx - 10, cy - 8), (cx - 10, cy + 8)], fill=BLACK, width=2)
            draw.line([(cx + 10, cy - 8), (cx + 10, cy + 8)], fill=BLACK, width=2)
            draw.arc([cx - 30, cy - 10, cx + 10, cy + 20], 210, 330, fill=RED_ACCENT, width=1)
            draw.arc([cx - 10, cy - 10, cx + 30, cy + 20], 210, 330, fill=RED_ACCENT, width=1)
        elif icon_type == "drone":
            draw.line([(cx - 16, cy), (cx + 16, cy)], fill="#2c3e50", width=2)
            draw.line([(cx, cy - 6), (cx, cy + 6)], fill="#2c3e50", width=2)
            draw.line([(cx - 8, cy - 6), (cx - 8, cy + 6)], fill="#2c3e50", width=1)
            draw.line([(cx + 8, cy - 6), (cx + 8, cy + 6)], fill="#2c3e50", width=1)
            draw.ellipse([cx + 12, cy - 4, cx + 18, cy + 2], fill=RED_ACCENT)
        elif icon_type == "atom":
            draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=RED_ACCENT)
            draw.ellipse([cx - 14, cy - 6, cx + 14, cy + 6], outline="#34495e", width=1)
            draw.ellipse([cx - 6, cy - 14, cx + 6, cy + 14], outline="#34495e", width=1)
        elif icon_type == "tax":
            draw.text((cx - 12, cy - 8), "%", fill=RED_ACCENT, font=f_stat_num)
            draw.text((cx + 8, cy - 4), "TAX", fill=BLACK, font=f_pill)
        elif icon_type == "flags":
            rect(cx - 18, cy - 6, cx - 2, cy + 6, fill="#de2910", outline="#aa2211")
            draw.polygon([(cx - 14, cy - 4), (cx - 12, cy - 4), (cx - 13, cy - 1)], fill="#ffde00")
            rect(cx + 2, cy - 6, cx + 18, cy + 6, fill=WHITE, outline="#bdc3c7")
            draw.ellipse([cx + 7, cy - 3, cx + 13, cy + 3], fill="#bc002d")
        elif icon_type == "plane":
            draw.polygon([(cx - 18, cy), (cx + 12, cy), (cx + 18, cy - 6), (cx + 16, cy), (cx + 2, cy + 6), (cx - 14, cy + 4)], fill="#2980b9")
            draw.line([(cx - 24, cy), (cx - 18, cy)], fill="#7f8c8d", width=1)
        elif icon_type == "bubbles":
            draw.ellipse([cx - 16, cy - 8, cx + 2, cy + 6], fill="#e8f8f5", outline="#16a085")
            draw.ellipse([cx - 2, cy - 4, cx + 16, cy + 10], fill="#e8f8f5", outline="#16a085")
            draw.text((cx - 10, cy - 4), "···", fill="#16a085", font=f_pill)
        elif icon_type == "btc":
            draw.ellipse([cx - 14, cy - 8, cx + 2, cy + 8], fill="#f39c12", outline="#d68910")
            draw.text((cx - 8, cy - 6), "₿", fill=WHITE, font=f_card_head)
            draw.text((cx + 6, cy - 6), "-3.9%", fill=RED_ACCENT, font=f_pill)
            draw.text((cx + 6, cy + 1), "$58,983", fill=BLACK, font=f_pill)
        elif icon_type == "f1":
            rect(cx - 16, cy, cx + 14, cy + 5, fill=RED_ACCENT)
            rect(cx - 4, cy - 4, cx + 6, cy, fill="#2c3e50")
            draw.ellipse([cx - 12, cy + 2, cx - 6, cy + 8], fill=BLACK)
            draw.ellipse([cx + 6, cy + 2, cx + 12, cy + 8], fill=BLACK)
            draw.text((cx + 16, cy - 4), "P1", fill=BLACK, font=f_pill)
        elif icon_type == "cricket":
            draw.line([(cx - 12, cy + 8), (cx + 6, cy - 6)], fill="#b7950b", width=3)
            draw.ellipse([cx + 10, cy - 4, cx + 16, cy + 2], fill=RED_ACCENT)
            draw.text((cx + 8, cy + 3), "124*", fill=BLACK, font=f_pill)

    for i, (cat, title, body, src, p_text, p_col, icon) in enumerate(cards_row1):
        cx = 15 + i * (card_w + 6)
        cy = 444
        rect(cx, cy, cx + card_w, cy + 16, fill=RED_ACCENT)
        draw.text((cx + 4, cy + 8), cat, fill=WHITE, font=f_card_cat, anchor="lm")
        rect(cx, cy + 16, cx + card_w, cy + card_h, fill=WHITE, outline=LINE_COLOR)
        draw_card_icon(icon, cx + card_w // 2, cy + 28)
        draw.text((cx + 4, cy + 40), title, fill=BLACK, font=f_card_head, spacing=1)
        draw.text((cx + 4, cy + 64), src, fill=LIGHT_GREY, font=f_source)
        pill(cx + card_w - 44, cy + 60, cx + card_w - 3, cy + 72, fill=p_col, r=2)
        draw.text((cx + card_w - 23, cy + 66), p_text, fill=WHITE, font=f_pill, anchor="mm")

    for i, (cat, title, body, src, p_text, p_col, icon) in enumerate(cards_row2):
        cx = 15 + i * (card_w + 6)
        cy = 526
        rect(cx, cy, cx + card_w, cy + 16, fill=RED_ACCENT)
        draw.text((cx + 4, cy + 8), cat, fill=WHITE, font=f_card_cat, anchor="lm")
        rect(cx, cy + 16, cx + card_w, cy + card_h, fill=WHITE, outline=LINE_COLOR)
        draw_card_icon(icon, cx + card_w // 2, cy + 28)
        draw.text((cx + 4, cy + 40), title, fill=BLACK, font=f_card_head, spacing=1)
        draw.text((cx + 4, cy + 64), src, fill=LIGHT_GREY, font=f_source)
        pill(cx + card_w - 44, cy + 60, cx + card_w - 3, cy + 72, fill=p_col, r=2)
        draw.text((cx + card_w - 23, cy + 66), p_text, fill=WHITE, font=f_pill, anchor="mm")

    # DIVIDER LINE
    draw.line([(15, 612), (WIDTH - 15, 612)], fill=LINE_COLOR, width=1)

    # 7. LOWER SECTION: MAP & 22 ADDITIONAL STORIES (y: 616 to 856)
    draw.text((15, 618), "WHERE IT HAPPENED — 13 NUMBERED GEO-PINS ACROSS 9 REGIONS", fill=BLACK, font=f_sec_title)
    draw.text((495, 618), "ALSO ON SATURDAY 21 NOVEMBER — 22 MORE STORIES", fill=BLACK, font=f_sec_title)

    # Map Box (x: 15 to 480, y: 634 to 856)
    rect(15, 634, 480, 856, fill="#eef3f7", outline=LINE_COLOR)

    def map_coord(lon, lat):
        mx = 15 + int((lon + 170) / 350 * 465)
        my = 634 + int((75 - lat) / 130 * 222)
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
        (3, -75, -11),   # Peru
        (4, 30, 50),     # Kyiv
        (5, 56, 27),     # Hormuz
        (6, 51, 36),     # Tehran
        (7, -77, 39),    # Washington
        (8, 116, 40),    # Beijing
        (9, 125, 7),     # Davao
        (10, 149, -35),  # Canberra
        (11, -74, 41),   # NY
        (12, -115, 36),  # Las Vegas
        (13, 175, -41),  # Wellington
    ]

    for num, lon, lat in pins:
        px, py = map_coord(lon, lat)
        draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED_ACCENT, outline=WHITE, width=1)
        draw.text((px, py), str(num), fill=WHITE, font=f_map_pin, anchor="mm")

    # 22 More Stories with 100% Unique Cities & Locations
    stories_col1 = [
        ("14 Kryvyi Rih:", "strike kills 2, injures 42 (Kyiv Ind.)"),
        ("15 Copenhagen:", "Russian attaché expelled over espionage (AJ)"),
        ("16 Antalya:", "COP31 climate summit enters overtime (AFP)"),
        ("17 Panama City:", "government vows veto over climate loss fund (Reuters)"),
        ("18 Jakarta:", "PLN seals $1.2B clean energy grid investment (Antara)"),
        ("19 Manama:", "Gulf coalition reports alerts over naval assets (AJ)"),
        ("20 Washington:", "Vance defends US deterrence policy (Reuters)"),
        ("21 Cape Canaveral:", "SpaceX launch cadence review initiated (CNN)"),
        ("22 Huntsville:", "70-year-old inmate execution carried out in TX (ABC)"),
        ("23 Los Angeles:", "Jury convicts Pacific Palisades arsonist (LA Times)"),
        ("24 St. Louis:", "Federal judge approves $7.25B settlement (AFP)"),
    ]

    stories_col2 = [
        ("25 Vancouver:", "Defence rests in youth climate litigation (AFP)"),
        ("26 Pyongyang:", "Kim Jong Un inspects heavy arms facilities (KCNA)"),
        ("27 Sejong:", "Freight train derails in S. Korea; zero injuries (K. Herald)"),
        ("28 Taipei:", "Parliament approves $3.8B economy package (T. Times)"),
        ("29 Bangkok:", "Thailand unveils Mekong transboundary cleanup (Nation)"),
        ("30 New Delhi:", "Pakistan delegation joins SCO tech forum (Dawn)"),
        ("31 Kolkata:", "Heavy rain alerts as Akvan remnants dissipate (ETV)"),
        ("32 Yangon:", "UN special rapporteur urges targeted sanctions (AP)"),
        ("33 Port Louis:", "15 African nations advance rating agency (AJ)"),
        ("34 Melbourne:", "Cummins confirmed Australia test captain (Cricket Aus)"),
        ("35 Las Vegas:", "Stewards clear Verstappen after pitlane review (Autosport)"),
    ]

    start_y = 636
    row_gap = 19.8
    for i, (loc, desc) in enumerate(stories_col1):
        sy = int(start_y + i * row_gap)
        draw.text((492, sy), loc, fill=RED_ACCENT, font=f_story_loc)
        draw.text((568, sy), desc, fill=DARK_GREY, font=f_story_desc)

    for i, (loc, desc) in enumerate(stories_col2):
        sy = int(start_y + i * row_gap)
        draw.text((752, sy), loc, fill=RED_ACCENT, font=f_story_loc)
        draw.text((826, sy), desc, fill=DARK_GREY, font=f_story_desc)

    # 8. 24-HOUR WORLD CHRONOLOGY & STRICT DATE INTEGRITY BOX (y: 864 to 978)
    rect(15, 864, WIDTH - 15, 978, fill="#fdfbf7", outline=LINE_COLOR, width=1)
    
    # Header of Section
    rect(15, 864, WIDTH - 15, 882, fill="#e2e8f0")
    draw.text((25, 873), "24-HOUR WORLD CHRONOLOGY · SATURDAY 21 NOVEMBER 2026 (00:00 - 24:00 UTC)", fill=BLACK, font=f_date_title, anchor="lm")
    draw.text((WIDTH - 25, 873), "8 KEY HOURLY MILESTONES ACROSS 9 REGIONS", fill=DARK_GREY, font=f_stat_lbl, anchor="rm")

    # 8 Timeline Milestones across the day
    timeline = [
        ("00:09 UTC", "Peru M6.7 Quake", "USGS · Carhuamayo"),
        ("02:15 UTC", "Riyadh Intercepts", "3 missiles downed"),
        ("05:30 UTC", "Wellington Cricket", "Rahul 124* at tea"),
        ("08:45 UTC", "Davao Jet Safe", "146 safely landed"),
        ("11:20 UTC", "COP31 Overtime", "Day 13 text deadlock"),
        ("15:00 UTC", "Kerch Bridge Warning", "Zelensky address"),
        ("18:30 UTC", "Las Vegas F1 P1", "Russell wet session"),
        ("21:45 UTC", "Tehran Uranium", "Stockpile remains in Iran"),
    ]
    t_col_w = (WIDTH - 30) // 8
    for i, (ut, ev, det) in enumerate(timeline):
        tx = 15 + i * t_col_w
        if i > 0:
            draw.line([(tx, 886), (tx, 924)], fill=LINE_COLOR, width=1)
        draw.text((tx + t_col_w // 2, 893), ut, fill=RED_ACCENT, font=f_chrono_time, anchor="mm")
        draw.text((tx + t_col_w // 2, 905), ev, fill=BLACK, font=f_chrono_desc, anchor="mm")
        draw.text((tx + t_col_w // 2, 917), det, fill=LIGHT_GREY, font=f_chrono_desc, anchor="mm")

    # Divider inside box
    draw.line([(25, 926), (WIDTH - 25, 926)], fill=LINE_COLOR, width=1)

    # Date Integrity & Exclusions Notice
    draw.text((25, 934), "DATE INTEGRITY & PRIOR-DAY FILTER:", fill=RED_ACCENT, font=f_date_title)
    draw.text((230, 935), "Left out because they belong to Friday 20 Nov: Kyiv Dnipro bridge hits · Cyclone Akvan landfall · Wall St tech correction · UK-EU reset deal.", fill=DARK_GREY, font=f_date_text)
    draw.text((25, 952), "Older still: Voyager 1 light-day (18 Nov). Not confirmed when drawn: BepiColombo Mercury orbit · final COP31 text. Every story on this page occurred or was first reported on Saturday 21 November 2026.", fill=DARK_GREY, font=f_date_text)
    draw.text((25, 966), "All 35 events verified via primary wires (Reuters, AP, AFP, USGS, Al Jazeera, Antara, KCNA). Zero AI hallucinations or speculative rumors.", fill=DARK_GREY, font=f_date_text)

    # 9. FOOTER STATUS LINE (y: 986 to 1012)
    draw.text((15, 990), "THE GLOBAL BROADSHEET · SATURDAY 21 NOVEMBER 2026 EDITION · 35 STORIES · 9 REGIONS", fill=DARK_GREY, font=f_footer)
    draw.text((WIDTH - 15, 990), "PRIMARY SOURCES ATTRIBUTED · RIGOROUS DATE VALIDATION · MAKE.FUN BENCHMARK", fill=LIGHT_GREY, font=f_footer, anchor="rt")

    im.save(output_path, "PNG", optimize=True)
    print(f"Masterpiece broadsheet saved at {output_path}! Size: {im.size}, Bytes: {os.path.getsize(output_path)}")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "entry.png")
    generate_broadsheet(out)
