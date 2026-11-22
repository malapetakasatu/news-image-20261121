import math
from PIL import Image, ImageDraw, ImageFont

def generate_broadsheet(output_path):
    WIDTH, HEIGHT = 1024, 1024
    im = Image.new("RGB", (WIDTH, HEIGHT), "#fcf8f2")
    draw = ImageDraw.Draw(im)

    # Fonts
    font_serif = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
    font_serif_reg = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
    font_serif_italic = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
    font_sans = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    font_sans_reg = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

    f_top = ImageFont.truetype(font_sans, 10)
    f_masthead = ImageFont.truetype(font_serif, 58)
    f_deck = ImageFont.truetype(font_serif_italic, 15)
    f_stat_num = ImageFont.truetype(font_serif, 24)
    f_stat_label = ImageFont.truetype(font_sans_reg, 8)
    f_region = ImageFont.truetype(font_sans, 8)
    f_hero_badge = ImageFont.truetype(font_sans, 9)
    f_hero_sub = ImageFont.truetype(font_sans, 9)
    f_hero_title = ImageFont.truetype(font_serif, 17)
    f_hero_body = ImageFont.truetype(font_serif_reg, 10)
    f_source = ImageFont.truetype(font_sans_reg, 8)
    f_pill = ImageFont.truetype(font_sans, 7)
    f_card_cat = ImageFont.truetype(font_sans, 8)
    f_card_head = ImageFont.truetype(font_serif, 11)
    f_card_body = ImageFont.truetype(font_serif_reg, 9)
    f_map_pin = ImageFont.truetype(font_sans, 7)
    f_section_title = ImageFont.truetype(font_sans, 10)
    f_story_loc = ImageFont.truetype(font_sans, 8)
    f_story_desc = ImageFont.truetype(font_serif_reg, 8)
    f_date_title = ImageFont.truetype(font_sans, 9)
    f_date_text = ImageFont.truetype(font_serif_reg, 8)
    f_footer = ImageFont.truetype(font_sans_reg, 8)

    # Colors
    BLACK = "#111111"
    OFF_BLACK = "#222222"
    DARK_GREY = "#444444"
    LIGHT_GREY = "#777777"
    LINE_COLOR = "#d0c8b8"
    RED_ACCENT = "#b71c1c"
    CREAM = "#fcf8f2"
    WHITE = "#ffffff"
    OFFICIAL_BLUE = "#1a5276"
    CONFIRMED_GREEN = "#1e8449"
    REPORTED_MUSTARD = "#b9770e"

    # Helpers
    def rect(x1, y1, x2, y2, fill=None, outline=None, width=1):
        draw.rectangle([x1, y1, x2, y2], fill=fill, outline=outline, width=width)

    def pill(x1, y1, x2, y2, fill=None, outline=None, r=3):
        draw.rounded_rectangle([x1, y1, x2, y2], radius=r, fill=fill, outline=outline)

    # 1. TOP BANNER
    rect(0, 0, WIDTH, 24, fill=RED_ACCENT)
    draw.text((15, 6), "THE WORLD IN ONE DAY", fill=WHITE, font=f_top)
    draw.text((WIDTH - 440, 6), "35 STORIES • 7 REGIONS • EVERY ONE DATED SATURDAY 21 NOVEMBER 2026", fill=WHITE, font=f_top)

    # 2. MASTHEAD
    draw.text((WIDTH // 2, 60), "Saturday 21 November 2026", fill=BLACK, font=f_masthead, anchor="mm")
    draw.text((WIDTH // 2, 98), "COP31 talks run into overtime   ·   missiles over Riyadh   ·   a quake shakes Peru", fill="#333333", font=f_deck, anchor="mm")
    draw.line([(15, 115), (WIDTH - 15, 115)], fill=BLACK, width=2)
    draw.line([(15, 118), (WIDTH - 15, 118)], fill=BLACK, width=1)

    # 3. STATS STRIP
    stats = [
        ("3", "missiles shot down over Riyadh"),
        ("124*", "K L Rahul's score at tea, Wellington"),
        ("DAY 13", "of COP31 — meant to close on day 12"),
        ("$58,983", "bitcoin early Saturday, down 3.9% in a day"),
        ("6.7", "magnitude of the Peru quake"),
        ("146", "people safe after Davao landing"),
    ]
    stat_w = (WIDTH - 30) // 6
    for i, (num, label) in enumerate(stats):
        sx = 15 + i * stat_w
        if i > 0:
            draw.line([(sx, 124), (sx, 172)], fill=LINE_COLOR, width=1)
        draw.text((sx + stat_w // 2, 138), num, fill=RED_ACCENT if i == 0 or i == 2 else BLACK, font=f_stat_num, anchor="mm")
        
        words = label.split(" ")
        mid = len(words) // 2
        line1 = " ".join(words[:mid]) if mid > 0 else label
        line2 = " ".join(words[mid:]) if mid > 0 else ""
        draw.text((sx + stat_w // 2, 158), line1, fill=DARK_GREY, font=f_stat_label, anchor="mm")
        if line2:
            draw.text((sx + stat_w // 2, 168), line2, fill=DARK_GREY, font=f_stat_label, anchor="mm")

    # REGION BAR
    regions = [
        ("Europe · 4", "#2980b9", 110),
        ("Asia · 10", "#d35400", 160),
        ("Middle East · 5", "#8e44ad", 130),
        ("Africa · 1", "#b7950b", 90),
        ("Americas · 11", "#27ae60", 170),
        ("Oceania · 3", "#16a085", 130),
        ("Global · 1", "#5d6d7e", 204),
    ]
    rx = 15
    for name, col, rw in regions:
        rect(rx, 180, rx + rw, 196, fill=col)
        draw.text((rx + rw // 2, 188), name, fill=WHITE, font=f_region, anchor="mm")
        rx += rw

    # 4. THREE HERO PANELS (y: 205 to 435)
    hero_w = (WIDTH - 42) // 3
    
    # --- HERO 1: MISSILES OVER RIYADH ---
    h1_x = 15
    rect(h1_x, 205, h1_x + hero_w, 226, fill=RED_ACCENT)
    draw.text((h1_x + 8, 215), "MISSILES OVER RIYADH", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h1_x + hero_w - 85, 209, h1_x + hero_w - 6, 222, fill=WHITE, r=3)
    draw.text((h1_x + hero_w - 45, 215), "3 SHOT DOWN", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")
    
    # Graphic Box 1 (Night Skyline & Interceptions)
    rect(h1_x, 226, h1_x + hero_w, 320, fill="#0c1424", outline=LINE_COLOR)
    # City silhouette
    buildings = [(0, 45, 25), (28, 55, 30), (62, 35, 20), (86, 65, 35), (125, 40, 22), 
                 (150, 70, 32), (185, 50, 28), (216, 60, 30), (250, 38, 25), (278, 55, 35)]
    for bx, bh, bw in buildings:
        draw.rectangle([h1_x + bx, 320 - bh, h1_x + bx + bw, 320], fill="#050811")
        for wy in range(320 - bh + 6, 316, 8):
            for wx in range(h1_x + bx + 4, h1_x + bx + bw - 4, 6):
                if (wx + wy) % 5 != 0:
                    draw.rectangle([wx, wy, wx + 2, wy + 3], fill="#ffea78" if (wx * wy) % 3 == 0 else "#ffffff")
    
    # Missile arcs and bursts
    arcs = [
        ([(h1_x + 30, 310), (h1_x + 80, 250), (h1_x + 140, 245)], "#ffdd44"),
        ([(h1_x + 280, 310), (h1_x + 230, 255), (h1_x + 175, 248)], "#ff9933"),
        ([(h1_x + 20, 305), (h1_x + 100, 270), (h1_x + 210, 258)], "#ffffff"),
    ]
    for pts, col in arcs:
        for t in range(50):
            u = t / 50.0
            px = (1-u)**2 * pts[0][0] + 2*(1-u)*u*pts[1][0] + u**2*pts[2][0]
            py = (1-u)**2 * pts[0][1] + 2*(1-u)*u*pts[1][1] + u**2*pts[2][1]
            draw.point((px, py), fill=col)
            draw.point((px+1, py), fill=col)
    
    # Starbursts at interception points
    for cx, cy in [(h1_x + 140, 245), (h1_x + 175, 248), (h1_x + 210, 258)]:
        draw.ellipse([cx-4, cy-4, cx+4, cy+4], fill="#ffeedd")
        for dx, dy in [(-8, 0), (8, 0), (0, -8), (0, 8), (-6, -6), (6, 6), (-6, 6), (6, -6)]:
            draw.line([(cx, cy), (cx + dx, cy + dy)], fill="#ffcc00", width=1)
            
    pill(h1_x + 8, 303, h1_x + 98, 316, fill="#000000", r=2)
    draw.text((h1_x + 53, 309), "Coalition statement", fill=WHITE, font=f_pill, anchor="mm")
    
    # Content 1
    rect(h1_x, 320, h1_x + hero_w, 435, fill=WHITE, outline=LINE_COLOR)
    draw.text((h1_x + 8, 328), "1 · RIYADH · SAUDI ARABIA", fill=RED_ACCENT, font=f_hero_sub)
    draw.text((h1_x + 8, 342), "Saudi defences down three\nmissiles aimed at the capital", fill=BLACK, font=f_hero_title, spacing=3)
    draw.text((h1_x + 8, 384), "Third night of alerts in a row: two blasts heard about\n02:00, no damage or casualties. It follows a Houthi\nstrike on the PIF tower two days earlier.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h1_x + 8, 424), "(Reuters · AFP · coalition statement)", fill=LIGHT_GREY, font=f_source)
    pill(h1_x + hero_w - 48, 418, h1_x + hero_w - 8, 430, fill=OFFICIAL_BLUE, r=2)
    draw.text((h1_x + hero_w - 28, 424), "OFFICIAL", fill=WHITE, font=f_pill, anchor="mm")

    # --- HERO 2: COP31 IN OVERTIME ---
    h2_x = 15 + hero_w + 6
    rect(h2_x, 205, h2_x + hero_w, 226, fill=RED_ACCENT)
    draw.text((h2_x + 8, 215), "COP31 IN OVERTIME", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h2_x + hero_w - 105, 209, h2_x + hero_w - 6, 222, fill=WHITE, r=3)
    draw.text((h2_x + hero_w - 55, 215), "NO DEAL · DAY 13", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")
    
    # Graphic Box 2 (Globe, Thermometer, Clock)
    rect(h2_x, 226, h2_x + hero_w, 320, fill="#e8f3fa", outline=LINE_COLOR)
    # Globe
    gx, gy = h2_x + 48, 273
    draw.ellipse([gx - 28, gy - 28, gx + 28, gy + 28], fill="#3498db", outline="#2980b9")
    draw.chord([gx - 22, gy - 16, gx + 8, gy + 14], 40, 220, fill="#2ecc71")
    draw.chord([gx - 10, gy - 24, gx + 22, gy - 2], 120, 310, fill="#27ae60")
    draw.chord([gx - 15, gy + 6, gx + 18, gy + 26], 0, 180, fill="#2ecc71")
    pill(h2_x + 12, 303, h2_x + 65, 316, fill="#000000", r=2)
    draw.text((h2_x + 38, 309), "AP · AFP", fill=WHITE, font=f_pill, anchor="mm")
    
    # Thermometer
    tx = h2_x + 142
    rect(tx - 4, 240, tx + 4, 298, fill=WHITE, outline="#95a5a6")
    draw.ellipse([tx - 11, 290, tx + 11, 312], fill=RED_ACCENT, outline="#95a5a6")
    rect(tx - 2, 255, tx + 2, 296, fill=RED_ACCENT)
    draw.line([(tx + 6, 255), (tx + 18, 255)], fill=RED_ACCENT, width=2)
    draw.text((tx + 22, 248), "+1.5°C", fill=RED_ACCENT, font=f_pill)
    draw.text((tx + 22, 258), "LIMIT AT RISK", fill=RED_ACCENT, font=f_pill)
    
    # Clock
    cx, cy = h2_x + 248, 273
    draw.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], fill=WHITE, outline="#2c3e50", width=2)
    for hr in range(12):
        ang = hr * math.pi / 6
        draw.line([(cx + 19 * math.sin(ang), cy - 19 * math.cos(ang)),
                   (cx + 22 * math.sin(ang), cy - 22 * math.cos(ang))], fill="#2c3e50", width=1)
    draw.line([(cx, cy), (cx + 12, cy - 8)], fill=BLACK, width=2)
    draw.line([(cx, cy), (cx + 3, cy - 16)], fill=BLACK, width=2)
    pill(cx - 22, 303, cx + 22, 316, fill="#000000", r=2)
    draw.text((cx, 309), "DAY 13", fill=WHITE, font=f_pill, anchor="mm")

    # Content 2
    rect(h2_x, 320, h2_x + hero_w, 435, fill=WHITE, outline=LINE_COLOR)
    draw.text((h2_x + 8, 328), "2 · ANTALYA · TÜRKIYE", fill=RED_ACCENT, font=f_hero_sub)
    draw.text((h2_x + 8, 342), "Climate summit misses\ndeadline as talks run into day", fill=BLACK, font=f_hero_title, spacing=3)
    draw.text((h2_x + 8, 384), "A draft with no mention of fossil fuels split nearly 200\ncountries. A third text is promised for Saturday\nmorning; Panama threatens to block it.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h2_x + 8, 424), "(AP · AFP · Al Jazeera)", fill=LIGHT_GREY, font=f_source)
    pill(h2_x + hero_w - 56, 418, h2_x + hero_w - 8, 430, fill=CONFIRMED_GREEN, r=2)
    draw.text((h2_x + hero_w - 32, 424), "CONFIRMED", fill=WHITE, font=f_pill, anchor="mm")

    # --- HERO 3: QUAKE IN PERU ---
    h3_x = 15 + (hero_w + 6) * 2
    rect(h3_x, 205, h3_x + hero_w, 226, fill=RED_ACCENT)
    draw.text((h3_x + 8, 215), "QUAKE SHAKES PERU", fill=WHITE, font=f_hero_badge, anchor="lm")
    pill(h3_x + hero_w - 145, 209, h3_x + hero_w - 6, 222, fill=WHITE, r=3)
    draw.text((h3_x + hero_w - 75, 215), "00:09 UTC · 108 KM DEEP", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")
    
    # Graphic Box 3 (Mountains, Seismograph wave, House)
    rect(h3_x, 226, h3_x + hero_w, 320, fill="#f9f2e7", outline=LINE_COLOR)
    # Seismograph spike wave
    seismo_pts = [
        (h3_x + 10, 260), (h3_x + 40, 260), (h3_x + 45, 255), (h3_x + 50, 265),
        (h3_x + 55, 245), (h3_x + 60, 275), (h3_x + 65, 235), (h3_x + 70, 280),
        (h3_x + 75, 250), (h3_x + 80, 268), (h3_x + 85, 258), (h3_x + 95, 260),
        (h3_x + 120, 260), (h3_x + 125, 248), (h3_x + 130, 272), (h3_x + 135, 240),
        (h3_x + 140, 285), (h3_x + 145, 250), (h3_x + 150, 265), (h3_x + 180, 260)
    ]
    for k in range(len(seismo_pts) - 1):
        draw.line([seismo_pts[k], seismo_pts[k+1]], fill=RED_ACCENT, width=2)
    
    draw.text((h3_x + 12, 235), "6.7", fill=RED_ACCENT, font=f_stat_num)
    draw.text((h3_x + 130, 236), "00:09 UTC", fill=DARK_GREY, font=f_pill)
    
    # Mountain silhouette
    draw.polygon([(h3_x + 160, 318), (h3_x + 205, 265), (h3_x + 235, 285), (h3_x + 265, 250), (h3_x + 310, 318)], fill="#935116")
    draw.polygon([(h3_x + 185, 318), (h3_x + 225, 275), (h3_x + 270, 318)], fill="#784212")
    
    # Adobe House shaking
    hx = h3_x + 235
    rect(hx, 288, hx + 38, 316, fill="#fdfefe", outline="#34495e", width=1)
    draw.polygon([(hx - 4, 288), (hx + 19, 272), (hx + 42, 288)], fill="#c0392b", outline="#922b21")
    rect(hx + 12, 298, hx + 24, 316, fill="#7f8c8d")
    
    pill(h3_x + hero_w - 65, 303, h3_x + hero_w - 10, 316, fill="#000000", r=2)
    draw.text((h3_x + hero_w - 37, 309), "USGS · IGP", fill=WHITE, font=f_pill, anchor="mm")

    # Content 3
    rect(h3_x, 320, h3_x + hero_w, 435, fill=WHITE, outline=LINE_COLOR)
    draw.text((h3_x + 8, 328), "3 · CARHUAMAYO · PERU", fill=RED_ACCENT, font=f_hero_sub)
    draw.text((h3_x + 8, 342), "Magnitude 6.7 quake rattles\ncentral Peru, felt in Lima", fill=BLACK, font=f_hero_title, spacing=3)
    draw.text((h3_x + 8, 384), "A deep tremor struck near Carhuamayo just after\nmidnight UTC. Peru's institute reported no deaths, no\ndamage and no tsunami risk.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h3_x + 8, 424), "(USGS · IGP)", fill=LIGHT_GREY, font=f_source)
    pill(h3_x + hero_w - 48, 418, h3_x + hero_w - 8, 430, fill=OFFICIAL_BLUE, r=2)
    draw.text((h3_x + hero_w - 28, 424), "OFFICIAL", fill=WHITE, font=f_pill, anchor="mm")

    # 5. SECONDARY STORY CARDS: ROW 1 (Cards 4 to 8, y: 442 to 522)
    card_w = (WIDTH - 54) // 5
    card_h = 80
    
    cards_row1 = [
        ("4 · KYIV WARNING", "Zelensky: Crimea bridge\n\"will not stay\"", "Warns of double-tap strikes ahead.", "(NBC)", "REPORTED", REPORTED_MUSTARD, "bridge"),
        ("5 · HORMUZ DRONE", "Iran says it downed a US\ndrone", "Tehran claims; US unconfirmed.", "(IRIB)", "REPORTED", REPORTED_MUSTARD, "drone"),
        ("6 · IRAN URANIUM", "Iran: uranium stock stays\nat home", "Still seeks a \"fair solution\".", "(Times of Israel)", "OFFICIAL", OFFICIAL_BLUE, "atom"),
        ("7 · TRUMP AI TAX", "Trump vows tax on data\ncentres abroad", "\"Tremendous\" penalty threatened.", "(ABC)", "REPORTED", REPORTED_MUSTARD, "tax"),
        ("8 · CHINA-JAPAN", "China tells Japan to\n\"correct\" Taiwan words", "Japan says its stance unchanged.", "(Ministry · AFP)", "OFFICIAL", OFFICIAL_BLUE, "flags"),
    ]

    def draw_card_icon(icon_type, cx, cy):
        if icon_type == "bridge":
            # Suspension bridge
            draw.line([(cx - 24, cy + 8), (cx + 24, cy + 8)], fill=BLACK, width=1)
            draw.line([(cx - 10, cy - 8), (cx - 10, cy + 8)], fill=BLACK, width=2)
            draw.line([(cx + 10, cy - 8), (cx + 10, cy + 8)], fill=BLACK, width=2)
            draw.arc([cx - 30, cy - 10, cx + 10, cy + 20], 210, 330, fill=RED_ACCENT, width=1)
            draw.arc([cx - 10, cy - 10, cx + 30, cy + 20], 210, 330, fill=RED_ACCENT, width=1)
        elif icon_type == "drone":
            # Drone
            draw.line([(cx - 16, cy), (cx + 16, cy)], fill="#2c3e50", width=2)
            draw.line([(cx, cy - 6), (cx, cy + 6)], fill="#2c3e50", width=2)
            draw.line([(cx - 8, cy - 6), (cx - 8, cy + 6)], fill="#2c3e50", width=1)
            draw.line([(cx + 8, cy - 6), (cx + 8, cy + 6)], fill="#2c3e50", width=1)
            draw.ellipse([cx + 12, cy - 4, cx + 18, cy + 2], fill=RED_ACCENT)
        elif icon_type == "atom":
            # Atom
            draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=RED_ACCENT)
            draw.ellipse([cx - 14, cy - 6, cx + 14, cy + 6], outline="#34495e", width=1)
            draw.ellipse([cx - 6, cy - 14, cx + 6, cy + 14], outline="#34495e", width=1)
        elif icon_type == "tax":
            # % TAX ABROAD
            draw.text((cx - 12, cy - 8), "%", fill=RED_ACCENT, font=f_stat_num)
            draw.text((cx + 8, cy - 4), "TAX", fill=BLACK, font=f_pill)
        elif icon_type == "flags":
            # Two flags
            rect(cx - 18, cy - 6, cx - 2, cy + 6, fill="#de2910", outline="#aa2211")
            draw.polygon([(cx - 14, cy - 4), (cx - 12, cy - 4), (cx - 13, cy - 1)], fill="#ffde00")
            rect(cx + 2, cy - 6, cx + 18, cy + 6, fill=WHITE, outline="#bdc3c7")
            draw.ellipse([cx + 7, cy - 3, cx + 13, cy + 3], fill="#bc002d")
        elif icon_type == "plane":
            # Jet airliner
            draw.polygon([(cx - 18, cy), (cx + 12, cy), (cx + 18, cy - 6), (cx + 16, cy), (cx + 2, cy + 6), (cx - 14, cy + 4)], fill="#2980b9")
            draw.line([(cx - 24, cy), (cx - 18, cy)], fill="#7f8c8d", width=1)
        elif icon_type == "bubbles":
            # Speech bubbles
            draw.ellipse([cx - 16, cy - 8, cx + 2, cy + 6], fill="#e8f8f5", outline="#16a085")
            draw.ellipse([cx - 2, cy - 4, cx + 16, cy + 10], fill="#e8f8f5", outline="#16a085")
            draw.text((cx - 10, cy - 4), "···", fill="#16a085", font=f_pill)
        elif icon_type == "btc":
            # Bitcoin
            draw.ellipse([cx - 14, cy - 8, cx + 2, cy + 8], fill="#f39c12", outline="#d68910")
            draw.text((cx - 8, cy - 6), "₿", fill=WHITE, font=f_card_head)
            draw.text((cx + 6, cy - 6), "-3.9%", fill=RED_ACCENT, font=f_pill)
            draw.text((cx + 6, cy + 1), "$58,983", fill=BLACK, font=f_pill)
        elif icon_type == "f1":
            # F1 Car
            rect(cx - 16, cy, cx + 14, cy + 5, fill=RED_ACCENT)
            rect(cx - 4, cy - 4, cx + 6, cy, fill="#2c3e50")
            draw.ellipse([cx - 12, cy + 2, cx - 6, cy + 8], fill=BLACK)
            draw.ellipse([cx + 6, cy + 2, cx + 12, cy + 8], fill=BLACK)
            draw.text((cx + 16, cy - 4), "P1", fill=BLACK, font=f_pill)
        elif icon_type == "cricket":
            # Cricket bat & ball
            draw.line([(cx - 12, cy + 8), (cx + 6, cy - 6)], fill="#b7950b", width=3)
            draw.ellipse([cx + 10, cy - 4, cx + 16, cy + 2], fill=RED_ACCENT)
            draw.text((cx + 8, cy + 3), "124*", fill=BLACK, font=f_pill)

    for i, (cat, title, body, src, p_text, p_col, icon) in enumerate(cards_row1):
        cx = 15 + i * (card_w + 6)
        cy = 442
        rect(cx, cy, cx + card_w, cy + 16, fill=RED_ACCENT)
        draw.text((cx + 4, cy + 8), cat, fill=WHITE, font=f_card_cat, anchor="lm")
        rect(cx, cy + 16, cx + card_w, cy + card_h, fill=WHITE, outline=LINE_COLOR)
        draw_card_icon(icon, cx + card_w // 2, cy + 29)
        draw.text((cx + 4, cy + 42), title, fill=BLACK, font=f_card_head, spacing=1)
        draw.text((cx + 4, cy + 66), src, fill=LIGHT_GREY, font=f_source)
        pill(cx + card_w - 42, cy + 62, cx + card_w - 3, cy + 73, fill=p_col, r=2)
        draw.text((cx + card_w - 22, cy + 67), p_text, fill=WHITE, font=f_pill, anchor="mm")

    # 6. SECONDARY STORY CARDS: ROW 2 (Cards 9 to 13, y: 526 to 606)
    cards_row2 = [
        ("9 · DAVAO 146 SAFE", "Jet lands safely after\nengine fire alert", "Air Niugini 767 diverted; all safe.", "(Airline · AP)", "OFFICIAL", OFFICIAL_BLUE, "plane"),
        ("10 · CANBERRA AI", "Australia and China agree\nto AI talks", "Albanese wraps up 11-day trip.", "(ABC)", "OFFICIAL", OFFICIAL_BLUE, "bubbles"),
        ("11 · BITCOIN $58,983", "Bitcoin slips below\n$59,000", "Down 3.9% in 24 hours.", "(CoinGecko)", "CONFIRMED", CONFIRMED_GREEN, "btc"),
        ("12 · RUSSELL P1", "Russell fastest in final\nLas Vegas practice", "1:34.041 in damp final session.", "(Formula 1)", "OFFICIAL", OFFICIAL_BLUE, "f1"),
        ("13 · RAHUL 124*", "Rahul century puts India\non top", "India 344-2 at tea, Wellington.", "(AFP)", "OFFICIAL", OFFICIAL_BLUE, "cricket"),
    ]

    for i, (cat, title, body, src, p_text, p_col, icon) in enumerate(cards_row2):
        cx = 15 + i * (card_w + 6)
        cy = 526
        rect(cx, cy, cx + card_w, cy + 16, fill=RED_ACCENT)
        draw.text((cx + 4, cy + 8), cat, fill=WHITE, font=f_card_cat, anchor="lm")
        rect(cx, cy + 16, cx + card_w, cy + card_h, fill=WHITE, outline=LINE_COLOR)
        draw_card_icon(icon, cx + card_w // 2, cy + 29)
        draw.text((cx + 4, cy + 42), title, fill=BLACK, font=f_card_head, spacing=1)
        draw.text((cx + 4, cy + 66), src, fill=LIGHT_GREY, font=f_source)
        pill(cx + card_w - 42, cy + 62, cx + card_w - 3, cy + 73, fill=p_col, r=2)
        draw.text((cx + card_w - 22, cy + 67), p_text, fill=WHITE, font=f_pill, anchor="mm")

    # DIVIDER LINE
    draw.line([(15, 614), (WIDTH - 15, 614)], fill=LINE_COLOR, width=1)

    # 7. BOTTOM SECTION: WHERE IT HAPPENED (Left) & 22 MORE STORIES (Right)
    draw.text((15, 622), "WHERE IT HAPPENED — STORIES 1-13", fill=OFF_BLACK, font=f_section_title)
    draw.text((495, 622), "ALSO ON SATURDAY 21 NOVEMBER — 22 MORE STORIES", fill=OFF_BLACK, font=f_section_title)

    # MAP BOX (x: 15 to 480, y: 640 to 868)
    rect(15, 640, 480, 868, fill="#eef3f7", outline=LINE_COLOR)

    def map_coord(lon, lat):
        mx = 15 + int((lon + 170) / 350 * 465)
        my = 640 + int((75 - lat) / 130 * 228)
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

    # Pins 1 to 13
    pins = [
        (1, 47, 25),     # Riyadh
        (2, 31, 37),     # Antalya
        (3, -75, -11),   # Junin / Peru
        (4, 30, 50),     # Kyiv
        (5, 56, 27),     # Hormuz
        (6, 51, 36),     # Tehran
        (7, -77, 39),    # Washington
        (8, 116, 40),    # Beijing / Tokyo
        (9, 125, 7),     # Davao
        (10, 149, -35),  # Canberra
        (11, -74, 41),   # Bitcoin / NY
        (12, -115, 36),  # Las Vegas
        (13, 175, -41),  # Wellington
    ]

    for num, lon, lat in pins:
        px, py = map_coord(lon, lat)
        # Diamond / circle pin
        draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED_ACCENT, outline=WHITE, width=1)
        draw.text((px, py), str(num), fill=WHITE, font=f_map_pin, anchor="mm")

    # 22 MORE STORIES (Stories 14 to 35) - Compact format
    stories_col1 = [
        ("14 Kryvyi Rih:", "strike kills 2, injures 42 (Kyiv Ind.)"),
        ("15 Copenhagen:", "Russian attaché expelled over a plot (AJ)"),
        ("16 Antalya:", "EU warns COP31 risks 'fossil summit' (AFP)"),
        ("17 Antalya:", "Panama threatens to block climate text (AJ)"),
        ("18 Antalya:", "Indonesia PLN signs clean-power deals (Antara)"),
        ("19 Yemen:", "Houthis threaten Jeddah and Red Sea ports (AJ)"),
        ("20 Washington:", "Vance says strikes were Trump's call (Reuters)"),
        ("21 Washington:", "SpaceX funding threatened (CNN)"),
        ("22 Texas:", "70-year-old's execution takes 63 min (ABC)"),
        ("23 Los Angeles:", "Jury convicts Palisades arsonist (ABC)"),
        ("24 Missouri:", "Judge approves $7.25bn settlement (AFP)"),
    ]

    stories_col2 = [
        ("25 Vancouver:", "defence rests in climate trial (AFP)"),
        ("26 Pyongyang:", "Kim tours factories after summit (AFP)"),
        ("27 Sejong:", "Freight train derails; no one hurt (K. Herald)"),
        ("28 Taipei:", "budget and cash payout passed (T. Times)"),
        ("29 Bangkok:", "arsenic plan for two rivers (The Nation)"),
        ("30 New Delhi:", "Pakistani minister joins SCO forum (Dawn)"),
        ("31 E. India:", "rain alerts as Akvan remnants move inland (ETV)"),
        ("32 Myanmar:", "rights groups urge sanctions (AP)"),
        ("33 Port Louis:", "African rating agency talks to 15 states (AJ)"),
        ("34 Melbourne:", "Cummins keeps captaincy (ABC)"),
        ("35 Las Vegas:", "Verstappen sent to stewards (Autosport)"),
    ]

    start_y = 642
    row_gap = 20.2
    for i, (loc, desc) in enumerate(stories_col1):
        sy = int(start_y + i * row_gap)
        draw.text((492, sy), loc, fill=RED_ACCENT, font=f_story_loc)
        draw.text((568, sy), desc, fill=DARK_GREY, font=f_story_desc)

    for i, (loc, desc) in enumerate(stories_col2):
        sy = int(start_y + i * row_gap)
        draw.text((752, sy), loc, fill=RED_ACCENT, font=f_story_loc)
        draw.text((826, sy), desc, fill=DARK_GREY, font=f_story_desc)

    # 8. DATE CHECK BOX (y: 878 to 962)
    rect(15, 878, WIDTH - 15, 962, fill="#fdfaf5", outline=RED_ACCENT, width=1)
    draw.text((25, 886), "DATE CHECK", fill=RED_ACCENT, font=f_date_title)
    
    date_lines = [
        "Left out because they belong to Friday 20 November: Wall Street's fall into correction · the Russian barrage that hit Kyiv's bridges · the missile that landed in Poland · the UK-EU deal · Cyclone Akvan's",
        "landfall. Older still: Voyager 1's light-day (18 Nov). Not confirmed when this page was drawn, so not shown: BepiColombo in Mercury orbit · a final COP31 text.",
        "Every story here happened, or was first reported, on Saturday 21 November 2026. Officials' counts and claims are attributed. Sources named beside each story · original drawings."
    ]
    for idx, dl in enumerate(date_lines):
        draw.text((25, 902 + idx * 14), dl, fill=DARK_GREY, font=f_date_text)

    # 9. FOOTER VERIFICATION KEY
    draw.text((15, 978), "Sources named beside each story · Original drawings · HOW WE CHECKED: CONFIRMED = 2+ outlets · OFFICIAL = on the record · REPORTED = one outlet · CLAIM = one side's account", fill=DARK_GREY, font=f_footer)
    draw.text((WIDTH - 15, 978), "THE GLOBAL BROADSHEET · 21 NOVEMBER 2026", fill=LIGHT_GREY, font=f_footer, anchor="rt")

    im.save(output_path, "PNG", optimize=True)
    print(f"Masterpiece broadsheet saved at {output_path}! Size: {im.size}")

if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(__file__), "entry.png")
    generate_broadsheet(out)
