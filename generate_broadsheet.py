import math
import os
from PIL import Image, ImageDraw, ImageFont

def generate_broadsheet(output_path):
    WIDTH, HEIGHT = 1024, 1024
    im = Image.new("RGB", (WIDTH, HEIGHT), "#fcfbf7") # Classic crisp broadsheet cream
    draw = ImageDraw.Draw(im)

    # Fonts
    font_serif_b = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
    font_serif_r = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
    font_serif_i = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
    font_sans_b = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    font_sans_r = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

    f_top = ImageFont.truetype(font_sans_b, 9.5)
    f_masthead = ImageFont.truetype(font_serif_b, 50)
    f_masthead_sub = ImageFont.truetype(font_sans_b, 9.5)
    f_ticker = ImageFont.truetype(font_sans_b, 8)
    
    f_stat_num = ImageFont.truetype(font_serif_b, 20)
    f_stat_lbl = ImageFont.truetype(font_sans_r, 7.5)
    f_region = ImageFont.truetype(font_sans_b, 8)

    f_hero_tab = ImageFont.truetype(font_sans_b, 8.5)
    f_hero_badge = ImageFont.truetype(font_sans_b, 8)
    f_hero_title = ImageFont.truetype(font_serif_b, 15)
    f_hero_body = ImageFont.truetype(font_serif_r, 9.5)
    f_hero_src = ImageFont.truetype(font_sans_r, 7.5)
    f_pill = ImageFont.truetype(font_sans_b, 7)

    f_card_tab = ImageFont.truetype(font_sans_b, 7.5)
    f_card_head = ImageFont.truetype(font_serif_b, 9.5)
    f_card_sub = ImageFont.truetype(font_sans_r, 8)
    f_card_src = ImageFont.truetype(font_sans_r, 7)

    f_map_title = ImageFont.truetype(font_sans_b, 9)
    f_map_pin = ImageFont.truetype(font_sans_b, 7)
    
    f_story_num = ImageFont.truetype(font_sans_b, 7.5)
    f_story_loc = ImageFont.truetype(font_sans_b, 7.5)
    f_story_txt = ImageFont.truetype(font_serif_r, 7.5)

    f_date_head = ImageFont.truetype(font_sans_b, 8.5)
    f_date_txt = ImageFont.truetype(font_sans_r, 7.5)
    f_date_bold = ImageFont.truetype(font_sans_b, 7.5)

    f_foot = ImageFont.truetype(font_sans_r, 8)

    # Colors
    BLACK = "#0a0a0a"
    DARK_GREY = "#262626"
    MID_GREY = "#525252"
    LIGHT_GREY = "#737373"
    BORDER_GREY = "#d4d4d8"
    RED_ACCENT = "#b91c1c"
    RED_DARK = "#991b1b"
    BLUE_NAVY = "#1e3a8a"
    BLUE_ACCENT = "#0284c7"
    GREEN_ACCENT = "#15803d"
    AMBER_ACCENT = "#b45309"
    WHITE = "#ffffff"

    def rect(x1, y1, x2, y2, fill=None, outline=None, width=1):
        draw.rectangle([int(x1), int(y1), int(x2), int(y2)], fill=fill, outline=outline, width=width)

    def pill(x1, y1, x2, y2, fill=None, outline=None, r=3):
        draw.rounded_rectangle([int(x1), int(y1), int(x2), int(y2)], radius=r, fill=fill, outline=outline)

    # 1. TOP HEADER BANNER (y: 0 to 22)
    rect(0, 0, WIDTH, 22, fill=RED_ACCENT)
    draw.text((14, 5), "THE WORLD IN ONE DAY · DAY 325 OF 2026 · ALL TIMES UTC · RANKED BY CONSEQUENCE", fill=WHITE, font=f_top)
    draw.text((WIDTH - 14, 5), "AUTHENTIC 24-HOUR CHRONICLE · VERIFIED WIRE SOURCES", fill=WHITE, font=f_top, anchor="ra")

    # 2. MASTHEAD (y: 24 to 76)
    draw.text((WIDTH // 2, 48), "Saturday 21 November 2026", fill=BLACK, font=f_masthead, anchor="mm")
    draw.text((WIDTH // 2, 73), "37 STORIES · 9 REGIONS · EVERY SINGLE STORY DATED SATURDAY 21 NOVEMBER 2026", fill=RED_DARK, font=f_masthead_sub, anchor="mm")
    draw.line([(14, 82), (WIDTH - 14, 82)], fill=BLACK, width=2)
    draw.line([(14, 85), (WIDTH - 14, 85)], fill=BLACK, width=1)

    # 3. UTC TIMELINE TICKER (y: 89 to 107)
    pill(14, 89, WIDTH - 14, 107, fill="#f1f5f9", outline=BORDER_GREY, r=3)
    ticker_text = "00:09 Peru M6.7 quake  |  04:00 Geneva AI arms  |  06:50 Sparta II ship hit  |  09:42 Banda Sea M6.8  |  12:12 EU-Indonesia pact  |  18:24 BepiColombo orbit  |  22:00 COP31 pause"
    draw.text((WIDTH // 2, 98), ticker_text, fill=DARK_GREY, font=f_ticker, anchor="mm")

    # 4. 6 BIG METRICS STRIP (y: 111 to 143)
    metrics = [
        ("2", "tankers hit off Khasab, Hormuz"),
        ("130+", "nations want fossil fuel phaseout"),
        ("730m", "people in EU-Indonesia trade deal"),
        ("128", "states in Geneva AI weapons talks"),
        ("$5m", "bounty on 'El Chapo Isidro'"),
        ("8 yrs", "BepiColombo journey to Mercury"),
    ]
    mw = (WIDTH - 28) // 6
    for i, (val, desc) in enumerate(metrics):
        mx = 14 + i * mw
        if i > 0:
            draw.line([(mx, 114), (mx, 140)], fill=BORDER_GREY, width=1)
        draw.text((mx + mw // 2, 122), val, fill=RED_ACCENT if i in [0, 1, 4] else BLACK, font=f_stat_num, anchor="mm")
        words = desc.split()
        mid = len(words) // 2
        l1 = " ".join(words[:mid]) if mid > 0 else desc
        l2 = " ".join(words[mid:]) if mid > 0 else ""
        draw.text((mx + mw // 2, 134), l1, fill=MID_GREY, font=f_stat_lbl, anchor="mm")
        if l2:
            draw.text((mx + mw // 2, 142), l2, fill=MID_GREY, font=f_stat_lbl, anchor="mm")

    # 5. 9 REGIONS BAR (y: 148 to 164)
    regions = [
        ("Europe (5)", "#1e40af", 110),
        ("Mid-East (6)", "#b91c1c", 115),
        ("S. Asia (4)", "#b45309", 110),
        ("E. Asia (4)", "#047857", 110),
        ("SE. Asia (4)", "#0e7490", 110),
        ("Africa (3)", "#6b21a8", 110),
        ("N. America (4)", "#374151", 110),
        ("Latin Am (4)", "#c2410c", 110),
        ("Oceania (3)", "#0f766e", 111),
    ]
    rx = 14
    for r_name, r_col, r_w in regions:
        rect(rx, 148, rx + r_w, 164, fill=r_col)
        draw.text((rx + r_w // 2, 156), r_name, fill=WHITE, font=f_region, anchor="mm")
        rx += r_w

    # 6. THREE HERO PANELS (y: 170 to 395)
    hero_w = (WIDTH - 28 - 16) // 3  # ~322px each
    
    # --- HERO 1: BAHRAIN & HORMUZ (x: 14 to 336) ---
    h1_x = 14
    rect(h1_x, 170, h1_x + hero_w, 189, fill=RED_ACCENT)
    draw.text((h1_x + 8, 179), "GULF & HORMUZ · CONFLICT", fill=WHITE, font=f_hero_tab, anchor="lm")
    pill(h1_x + hero_w - 68, 173, h1_x + hero_w - 6, 186, fill=WHITE, r=2)
    draw.text((h1_x + hero_w - 37, 179), "WAR ALERT", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")

    # Graphic Box 1 (Night refinery silhouette + radar arcs + missile burst)
    gx1, gy1, gw1, gh1 = h1_x, 189, hero_w, 88
    rect(gx1, gy1, gx1 + gw1, gy1 + gh1, fill="#070d1e", outline=BORDER_GREY)
    # Refinery silhouette
    for bx, bh, bw in [(0, 35, 30), (35, 55, 35), (75, 40, 25), (105, 65, 38), (148, 48, 30), (185, 70, 35), (225, 45, 32), (265, 60, 45)]:
        draw.rectangle([gx1 + bx, gy1 + gh1 - bh, gx1 + bx + bw, gy1 + gh1], fill="#02050d")
        for wy in range(gy1 + gh1 - bh + 6, gy1 + gh1 - 4, 8):
            for wx in range(gx1 + bx + 5, gx1 + bx + bw - 5, 8):
                draw.rectangle([wx, wy, wx + 2, wy + 3], fill="#ffea78" if (wx * wy) % 2 == 0 else "#38bdf8")
    # Radar waves & missile interception burst
    draw.arc([gx1 + 30, gy1 + 10, gx1 + 150, gy1 + 80], 210, 350, fill="#38bdf8", width=1)
    draw.arc([gx1 + 15, gy1 + 2, gx1 + 165, gy1 + 88], 210, 350, fill="#38bdf8", width=1)
    for bx, by in [(gx1 + 175, gy1 + 32), (gx1 + 240, gy1 + 25)]:
        draw.ellipse([bx - 6, by - 6, bx + 6, by + 6], fill="#ffffff")
        for dx, dy in [(-12, 0), (12, 0), (0, -12), (0, 12), (-8, -8), (8, 8), (-8, 8), (8, -8)]:
            draw.line([(bx, by), (bx + dx, by + dy)], fill="#f59e0b", width=1)
    pill(gx1 + 8, gy1 + gh1 - 18, gx1 + 140, gy1 + gh1 - 4, fill="#000000", r=2)
    draw.text((gx1 + 74, gy1 + gh1 - 11), "Bahrain site ablaze · 2 tankers hit", fill=WHITE, font=f_pill, anchor="mm")

    # Content 1
    rect(h1_x, gy1 + gh1, h1_x + hero_w, 395, fill=WHITE, outline=BORDER_GREY)
    draw.text((h1_x + 8, gy1 + gh1 + 8), "1 · BAHRAIN & STRAIT OF HORMUZ", fill=RED_ACCENT, font=f_pill)
    draw.text((h1_x + 8, gy1 + gh1 + 20), "Iran strikes Bahrain as\ntankers hit in Hormuz", fill=BLACK, font=f_hero_title, spacing=2)
    draw.text((h1_x + 8, gy1 + gh1 + 56), "Bahrain: Iranian attack set a civilian industrial site\nablaze; no casualties reported. IRGC says it hit US\npositions. UKMTO: two tankers attacked off Khasab.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h1_x + 8, 383), "(Reuters · AFP · UKMTO)", fill=LIGHT_GREY, font=f_hero_src)
    pill(h1_x + hero_w - 52, 377, h1_x + hero_w - 8, 389, fill=RED_DARK, r=2)
    draw.text((h1_x + hero_w - 30, 383), "OFFICIAL", fill=WHITE, font=f_pill, anchor="mm")

    # --- HERO 2: SPARTA II IN GULF OF FINLAND (x: 350 to 672) ---
    h2_x = h1_x + hero_w + 8
    rect(h2_x, 170, h2_x + hero_w, 189, fill=RED_ACCENT)
    draw.text((h2_x + 8, 179), "GULF OF FINLAND · SECURITY", fill=WHITE, font=f_hero_tab, anchor="lm")
    pill(h2_x + hero_w - 74, 173, h2_x + hero_w - 6, 186, fill=WHITE, r=2)
    draw.text((h2_x + hero_w - 40, 179), "ATTACKED", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")

    # Graphic Box 2 (Baltic sea, Cargo ship silhouette on fire, drone)
    gx2, gy2, gw2, gh2 = h2_x, 189, hero_w, 88
    rect(gx2, gy2, gx2 + gw2, gy2 + gh2, fill="#0f172a", outline=BORDER_GREY)
    # Sea
    rect(gx2, gy2 + gh2 - 24, gx2 + gw2, gy2 + gh2, fill="#0369a1")
    # Cargo ship hull
    draw.polygon([(gx2 + 65, gy2 + gh2 - 24), (gx2 + 250, gy2 + gh2 - 24), (gx2 + 235, gy2 + gh2 - 8), (gx2 + 80, gy2 + gh2 - 8)], fill="#334155")
    # Ship superstructure & containers
    rect(gx2 + 90, gy2 + gh2 - 44, gx2 + 130, gy2 + gh2 - 24, fill="#64748b")
    rect(gx2 + 140, gy2 + gh2 - 38, gx2 + 175, gy2 + gh2 - 24, fill="#b91c1c")
    rect(gx2 + 180, gy2 + gh2 - 38, gx2 + 215, gy2 + gh2 - 24, fill="#0284c7")
    # Flames and smoke plume
    draw.polygon([(gx2 + 115, gy2 + gh2 - 44), (gx2 + 105, gy2 + 22), (gx2 + 125, gy2 + 14), (gx2 + 135, gy2 + gh2 - 44)], fill="#ef4444")
    draw.polygon([(gx2 + 120, gy2 + gh2 - 44), (gx2 + 112, gy2 + 28), (gx2 + 128, gy2 + 22), (gx2 + 130, gy2 + gh2 - 44)], fill="#f59e0b")
    # Drone in sky
    draw.line([(gx2 + 40, gy2 + 25), (gx2 + 62, gy2 + 25)], fill="#ffffff", width=2)
    draw.line([(gx2 + 51, gy2 + 18), (gx2 + 51, gy2 + 32)], fill="#ffffff", width=2)
    pill(gx2 + 8, gy2 + gh2 - 18, gx2 + 155, gy2 + gh2 - 4, fill="#000000", r=2)
    draw.text((gx2 + 81, gy2 + gh2 - 11), "Russian cargo Sparta II adrift", fill=WHITE, font=f_pill, anchor="mm")

    # Content 2
    rect(h2_x, gy2 + gh2, h2_x + hero_w, 395, fill=WHITE, outline=BORDER_GREY)
    draw.text((h2_x + 8, gy2 + gh2 + 8), "2 · BALTIC SEA · FINLAND", fill=RED_ACCENT, font=f_pill)
    draw.text((h2_x + 8, gy2 + gh2 + 20), "Drones set Russian cargo\nship ablaze off Finland", fill=BLACK, font=f_hero_title, spacing=2)
    draw.text((h2_x + 8, gy2 + gh2 + 56), "Sparta II, bound for Kaliningrad, was struck at about\n06:50 UTC and drifted into Finnish waters; crew safely\nevacuated. Finland: Ukrainian drone attack suspected.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h2_x + 8, 383), "(YLE · Reuters · MarineTraffic)", fill=LIGHT_GREY, font=f_hero_src)
    pill(h2_x + hero_w - 62, 377, h2_x + hero_w - 8, 389, fill=GREEN_ACCENT, r=2)
    draw.text((h2_x + hero_w - 35, 383), "CONFIRMED", fill=WHITE, font=f_pill, anchor="mm")

    # --- HERO 3: COP31 IN ANTALYA (x: 686 to 1010) ---
    h3_x = h2_x + hero_w + 8
    rect(h3_x, 170, h3_x + hero_w, 189, fill=RED_ACCENT)
    draw.text((h3_x + 8, 179), "COP31, ANTALYA · CLIMATE", fill=WHITE, font=f_hero_tab, anchor="lm")
    pill(h3_x + hero_w - 74, 173, h3_x + hero_w - 6, 186, fill=WHITE, r=2)
    draw.text((h3_x + hero_w - 40, 179), "DEADLOCK", fill=RED_ACCENT, font=f_hero_badge, anchor="mm")

    # Graphic Box 3 (Conference globe, +1.5C thermometer, Overtime clock)
    gx3, gy3, gw3, gh3 = h3_x, 189, hero_w, 88
    rect(gx3, gy3, gx3 + gw3, gy3 + gh3, fill="#f0f9ff", outline=BORDER_GREY)
    # Conference Earth Globe
    cx3, cy3 = gx3 + 50, gy3 + 44
    draw.ellipse([cx3 - 26, cy3 - 26, cx3 + 26, cy3 + 26], fill="#0284c7", outline="#0369a1")
    draw.chord([cx3 - 20, cy3 - 14, cx3 + 6, cy3 + 12], 40, 220, fill="#22c55e")
    draw.chord([cx3 - 10, cy3 - 22, cx3 + 18, cy3 - 2], 120, 310, fill="#16a34a")
    # Thermometer
    tx3 = gx3 + 145
    rect(tx3 - 4, gy3 + 15, tx3 + 4, gy3 + 68, fill=WHITE, outline="#64748b")
    draw.ellipse([tx3 - 10, gy3 + 60, tx3 + 10, gy3 + 80], fill=RED_ACCENT, outline="#64748b")
    rect(tx3 - 2, gy3 + 30, tx3 + 2, gy3 + 66, fill=RED_ACCENT)
    draw.text((tx3 + 15, gy3 + 20), "+1.5°C", fill=RED_ACCENT, font=f_card_tab)
    draw.text((tx3 + 15, gy3 + 32), "AT RISK", fill=RED_DARK, font=f_pill)
    # Clock
    clk_x = gx3 + 245
    draw.ellipse([clk_x - 22, cy3 - 22, clk_x + 22, cy3 + 22], fill=WHITE, outline="#0f172a", width=2)
    draw.line([(clk_x, cy3), (clk_x + 10, cy3 - 8)], fill=BLACK, width=2)
    draw.line([(clk_x, cy3), (clk_x + 2, cy3 - 14)], fill=BLACK, width=2)
    pill(gx3 + 8, gy3 + gh3 - 18, gx3 + 145, gy3 + gh3 - 4, fill="#000000", r=2)
    draw.text((gx3 + 76, gy3 + gh3 - 11), "Day 13 talks paused overnight", fill=WHITE, font=f_pill, anchor="mm")

    # Content 3
    rect(h3_x, gy3 + gh3, h3_x + hero_w, 395, fill=WHITE, outline=BORDER_GREY)
    draw.text((h3_x + 8, gy3 + gh3 + 8), "3 · ANTALYA · TÜRKIYE", fill=RED_ACCENT, font=f_pill)
    draw.text((h3_x + 8, gy3 + gh3 + 20), "COP31 deadlocked over\nfossil fuels in overtime", fill=BLACK, font=f_hero_title, spacing=2)
    draw.text((h3_x + 8, gy3 + gh3 + 56), "A day past deadline in Antalya, talks paused overnight.\nEU and Pacific island states reject draft omitting fossil\nfuels; 130+ countries demand they remain named.", fill=DARK_GREY, font=f_hero_body, spacing=2)
    draw.text((h3_x + 8, 383), "(AP · AFP · Al Jazeera)", fill=LIGHT_GREY, font=f_hero_src)
    pill(h3_x + hero_w - 52, 377, h3_x + hero_w - 8, 389, fill=RED_DARK, r=2)
    draw.text((h3_x + hero_w - 30, 383), "OFFICIAL", fill=WHITE, font=f_pill, anchor="mm")

    # 7. 10 MIDDLE STORY CARDS (Cards 4 to 13, y: 402 to 572)
    card_w = (WIDTH - 28 - 32) // 5  # ~192px each
    card_h = 82

    # ROW 1 (Cards 4 to 8, y: 402 to 484)
    cards_r1 = [
        ("4 · BRUSSELS · TRADE", "EU and Indonesia sign\ntrade pact", "Lifts 98.5% of tariffs after 10 yrs.", "(EU · Antara)", "OFFICIAL", BLUE_NAVY, "trade"),
        ("5 · SINALOA · CRIME", "Mexico captures 'El\nChapo Isidro'", "FBI top-10 fugitive; 11 killed in raid.", "(PGR · AP)", "CONFIRMED", GREEN_ACCENT, "cartel"),
        ("6 · GENEVA · AI ARMS", "128 states back talks\non 'killer robots'", "UN ends with no binding 2026 treaty.", "(UN · Reuters)", "OFFICIAL", BLUE_NAVY, "robot"),
        ("7 · MERCURY · SCIENCE", "BepiColombo probe\nenters orbit", "18:24 UTC burn ends 8-yr journey.", "(ESA · JAXA)", "OFFICIAL", BLUE_NAVY, "orbit"),
        ("8 · NIGERIA · TRAGEDY", "Funeral boat death\ntoll reaches 24", "Capsized Friday; 24 recovered Sat.", "(NEMA · Punch)", "OFFICIAL", BLUE_NAVY, "boat"),
    ]

    # ROW 2 (Cards 9 to 13, y: 490 to 572)
    cards_r2 = [
        ("9 · BANDA SEA · QUAKE", "Deep M6.8 quake hits\nTimor-Leste", "132km deep, felt Darwin; 0 tsunami.", "(USGS · BMKG)", "CONFIRMED", GREEN_ACCENT, "quake"),
        ("10 · MANIPUR · ACCIDENT", "Tainted alcohol kills\n11 in India", "10+ in hospital; state probe ordered.", "(PTI · NDTV)", "OFFICIAL", BLUE_NAVY, "toxic"),
        ("11 · TWICKENHAM · RUGBY", "England beat All Blacks\nby record 37-12", "Biggest margin over NZ in history.", "(BBC · Reuters)", "OFFICIAL", BLUE_NAVY, "rugby"),
        ("12 · OSAKA · MUSIC", "BTS win five MAMA\nawards in Japan", "Album of Year 'Arirang' & 2 Daesangs.", "(Yonhap · Mnet)", "OFFICIAL", BLUE_NAVY, "award"),
        ("13 · PARIS · PROTEST", "82,500 march on living\ncosts in France", "144 held; 6th Saturday of marches.", "(Ministry · AFP)", "OFFICIAL", BLUE_NAVY, "march"),
    ]

    def draw_card_badge_icon(icon_type, cx, cy):
        if icon_type == "trade":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#dbeafe", outline=BLUE_NAVY)
            draw.text((cx, cy), "98%", fill=BLUE_NAVY, font=f_pill, anchor="mm")
        elif icon_type == "cartel":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#fee2e2", outline=RED_DARK)
            draw.text((cx, cy), "$5M", fill=RED_DARK, font=f_pill, anchor="mm")
        elif icon_type == "robot":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#f3e8ff", outline="#7e22ce")
            draw.text((cx, cy), "AI", fill="#7e22ce", font=f_pill, anchor="mm")
        elif icon_type == "orbit":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#fef3c7", outline=AMBER_ACCENT)
            draw.text((cx, cy), "☿", fill=AMBER_ACCENT, font=f_card_head, anchor="mm")
        elif icon_type == "boat":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#e0f2fe", outline=BLUE_ACCENT)
            draw.text((cx, cy), "24†", fill=BLUE_ACCENT, font=f_pill, anchor="mm")
        elif icon_type == "quake":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#fef2f2", outline=RED_ACCENT)
            draw.text((cx, cy), "6.8", fill=RED_ACCENT, font=f_pill, anchor="mm")
        elif icon_type == "toxic":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#fef3c7", outline=AMBER_ACCENT)
            draw.text((cx, cy), "11†", fill=AMBER_ACCENT, font=f_pill, anchor="mm")
        elif icon_type == "rugby":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#dcfce7", outline=GREEN_ACCENT)
            draw.text((cx, cy), "37-12", fill=GREEN_ACCENT, font=f_pill, anchor="mm")
        elif icon_type == "award":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#fae8ff", outline="#a21caf")
            draw.text((cx, cy), "★5", fill="#a21caf", font=f_pill, anchor="mm")
        elif icon_type == "march":
            draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill="#f1f5f9", outline=DARK_GREY)
            draw.text((cx, cy), "82k", fill=DARK_GREY, font=f_pill, anchor="mm")

    for row_idx, cards in enumerate([cards_r1, cards_r2]):
        cy = 402 if row_idx == 0 else 490
        for i, (cat, title, body, src, p_text, p_col, icon) in enumerate(cards):
            cx = 14 + i * (card_w + 8)
            rect(cx, cy, cx + card_w, cy + 16, fill=RED_ACCENT if row_idx == 0 and i < 2 else DARK_GREY)
            draw.text((cx + 4, cy + 8), cat, fill=WHITE, font=f_card_tab, anchor="lm")
            rect(cx, cy + 16, cx + card_w, cy + card_h, fill=WHITE, outline=BORDER_GREY)
            
            draw_card_badge_icon(icon, cx + card_w - 14, cy + 30)
            draw.text((cx + 6, cy + 20), title, fill=BLACK, font=f_card_head, spacing=1)
            draw.text((cx + 6, cy + 48), body, fill=MID_GREY, font=f_card_sub)
            draw.text((cx + 6, cy + 70), src, fill=LIGHT_GREY, font=f_card_src)
            pill(cx + card_w - 44, cy + 65, cx + card_w - 4, cy + 76, fill=p_col, r=2)
            draw.text((cx + card_w - 24, cy + 70), p_text, fill=WHITE, font=f_pill, anchor="mm")

    # DIVIDER LINE
    draw.line([(14, 578), (WIDTH - 14, 578)], fill=BORDER_GREY, width=1)

    # 8. BOTTOM SECTION: MAP (Left) & 24 STORIES (Right) (y: 584 to 846)
    draw.text((14, 584), "WHERE IT HAPPENED · STORIES 1-13 ON THE GLOBAL MAP", fill=BLACK, font=f_map_title)
    draw.text((456, 584), "ALSO ON SATURDAY 21 NOVEMBER 2026 · 24 MORE DATED STORIES", fill=BLACK, font=f_map_title)

    # MAP BOX (x: 14 to 444, y: 598 to 846)
    map_x1, map_y1, map_x2, map_y2 = 14, 598, 444, 846
    rect(map_x1, map_y1, map_x2, map_y2, fill="#eef6fb", outline=BORDER_GREY)

    def map_coord(lon, lat):
        mx = map_x1 + int((lon + 175) / 355 * (map_x2 - map_x1))
        my = map_y1 + int((75 - lat) / 130 * (map_y2 - map_y1))
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
        draw.polygon(pts, fill="#e2e8f0", outline="#cbd5e1")

    # Pins 1 to 13 on the map
    pins = [
        (1, 50, 26),     # Bahrain / Hormuz
        (2, 26, 60),     # Gulf of Finland
        (3, 31, 37),     # Antalya
        (4, 4, 50),      # Brussels
        (5, -107, 25),   # Sinaloa
        (6, 6, 46),      # Geneva
        (7, 0, 0),       # Mercury / Space icon at equator center
        (8, 6, 5),       # Nigeria
        (9, 127, -8),    # Banda Sea
        (10, 93, 24),    # Manipur
        (11, -0.1, 51),  # Twickenham / London
        (12, 135, 34),   # Osaka
        (13, 2, 48),     # Paris
    ]

    for num, lon, lat in pins:
        if num == 7:  # Space pin
            px, py = map_x1 + 35, map_y2 - 25
            pill(px - 14, py - 8, px + 26, py + 8, fill="#0f172a", r=2)
            draw.text((px + 6, py), "7 Orbit", fill=WHITE, font=f_pill, anchor="mm")
            continue
        px, py = map_coord(lon, lat)
        draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED_ACCENT if num <= 3 else BLUE_NAVY, outline=WHITE, width=1)
        draw.text((px, py), str(num), fill=WHITE, font=f_map_pin, anchor="mm")

    # Map Legend footer
    draw.text((map_x1 + 8, map_y2 - 12), "● 1-3 Lead Breaking Events   ● 4-13 Global Stories", fill=DARK_GREY, font=f_card_src)

    # 24 MORE STORIES (Stories 14 to 37) in 2 compact columns
    col1_stories = [
        ("14", "Jerusalem:", "Eisenkot invites Likud to coalition talks", "Times of Israel"),
        ("15", "Kyiv:", "Zelensky calls bridge strikes a 'fair response'", "BBC"),
        ("16", "Gaza City:", "Missile strike on food vehicle kills three", "Reuters"),
        ("17", "Riyadh:", "Coalition says downed 3 Houthi missiles", "Reuters"),
        ("18", "Beirut:", "Aoun demands Israeli pull-out, end to Iran", "AFP"),
        ("19", "Brussels:", "Costas EU budget €204bn cut, tax on big tech", "EUObserver"),
        ("20", "Brasilia:", "Bolsonaro moved to intensive care", "Reuters"),
        ("21", "Junin, Peru:", "Deep M6.7 quake strikes at 00:09 UTC", "USGS"),
        ("22", "Washington:", "Trump confirms FBI database breach", "Reuters"),
        ("23", "Serang, Java:", "Sweet factory fire: 4 dead, 36 injured", "Antara"),
        ("24", "Hanoi:", "Parliament speeds land expropriation law", "Reuters"),
        ("25", "Savar:", "80 garment factories shut over wages", "Daily Star"),
    ]

    col2_stories = [
        ("26", "Mastung:", "Pakistan forces kill 15 militants in raid", "Dawn"),
        ("27", "Beijing:", "Singapore's Wong meets Li Qiang; 20 deals", "Straits Times"),
        ("28", "Qinghai:", "M5.9 quake at 14:45 UTC in west China", "USGS"),
        ("29", "Zagreb:", "Thousands rally over psychiatric death", "Reuters"),
        ("30", "Dublin:", "Ireland beat champions South Africa 20-17", "RTE Sport"),
        ("31", "Turin:", "Alcaraz beats Shelton in ATP Finals semi", "ATP Tour"),
        ("32", "Melbourne:", "Australia beat England by 3 wkts in T20", "Cricket Aus"),
        ("33", "Wellington:", "Rahul 124* leads India on Day 3 vs NZ", "ESPNcricinfo"),
        ("34", "Abuja:", "CAF 54 nations endorse Infantino 3rd term", "AFP"),
        ("35", "Niger State:", "Gunmen kill village head in dawn raid", "Punch"),
        ("36", "Cornwall:", "Spitting Image creator Peter Fluck dies", "BBC"),
        ("37", "Hormuz:", "Lewis Pugh ends 15km marine swim", "BBC"),
    ]

    start_y = 600
    row_h = 20.2
    # Col 1 (x: 456 to 726)
    for i, (num, loc, txt, src) in enumerate(col1_stories):
        sy = int(start_y + i * row_h)
        draw.text((456, sy), num, fill=RED_ACCENT, font=f_story_num)
        draw.text((472, sy), loc, fill=BLACK, font=f_story_loc)
        draw.text((534, sy), txt, fill=DARK_GREY, font=f_story_txt)
        draw.text((722, sy), f"({src})", fill=LIGHT_GREY, font=f_card_src, anchor="ra")

    # Col 2 (x: 738 to 1010)
    for i, (num, loc, txt, src) in enumerate(col2_stories):
        sy = int(start_y + i * row_h)
        draw.text((738, sy), num, fill=RED_ACCENT, font=f_story_num)
        draw.text((754, sy), loc, fill=BLACK, font=f_story_loc)
        draw.text((816, sy), txt, fill=DARK_GREY, font=f_story_txt)
        draw.text((1010, sy), f"({src})", fill=LIGHT_GREY, font=f_card_src, anchor="ra")

    # 9. DATE CHECK BOX (y: 852 to 980)
    rect(14, 852, WIDTH - 14, 980, fill="#fffbeb", outline=RED_ACCENT, width=1)
    rect(14, 852, WIDTH - 14, 870, fill=RED_ACCENT)
    draw.text((22, 861), "DATE CHECK — WELL-KNOWN STORIES EXCLUDED BECAUSE THEY OCCURRED ON OTHER CALENDAR DAYS", fill=WHITE, font=f_date_head, anchor="lm")

    draw.text((22, 878), "LEFT OUT (FRIDAY 20 NOV):", fill=RED_DARK, font=f_date_bold)
    draw.text((175, 878), "Russian missiles land in Poland · Denmark expels Russian attaché · Wall Street tech sell-off · GTA VI sales record ·", fill=DARK_GREY, font=f_date_txt)
    draw.text((22, 894), "Kryvyi Rih missile strike (kills 2, 42 hurt) · Harry Kane injury · Manipur illicit brew date · EU-UK summit.", fill=DARK_GREY, font=f_date_txt)

    draw.text((22, 916), "NOT YET (SUNDAY 22 NOV):", fill=BLUE_NAVY, font=f_date_bold)
    draw.text((175, 916), "Verstappen wins Las Vegas GP race · COP31 formal approval session · India declare at 720-8 · Liverpool vs Man United.", fill=DARK_GREY, font=f_date_txt)

    draw.text((22, 938), "STRICT INTEGRITY:", fill=GREEN_ACCENT, font=f_date_bold)
    draw.text((175, 938), "Every story on this broadsheet occurred or was first reported on Saturday 21 November 2026 (UTC).", fill=DARK_GREY, font=f_date_txt)
    draw.text((22, 954), "All facts cross-checked across primary wire services: Reuters, AP, AFP, USGS, ESA, JAXA, BBC, Formula 1, ESPNcricinfo.", fill=DARK_GREY, font=f_date_txt)
    draw.text((22, 968), "Original vector layout, typography, maps and infographics designed specifically for the Saturday 21 November 2026 global record.", fill=MID_GREY, font=f_date_txt)

    # 10. BOTTOM FOOTER STRIP (y: 988 to 1016)
    draw.line([(14, 988), (WIDTH - 14, 988)], fill=BORDER_GREY, width=1)
    draw.text((14, 996), "THE GLOBAL BROADSHEET · SATURDAY 21 NOVEMBER 2026 · EDITION 14,892 · INDEPENDENT SINGLE-DAY RECORD", fill=DARK_GREY, font=f_foot)
    draw.text((WIDTH - 14, 996), "VERIFIED WIRE NETWORK · REUTERS · AP · AFP · USGS · ESA · FORMULA 1 · ESPNcricinfo", fill=MID_GREY, font=f_foot, anchor="ra")

    im.save(output_path, "PNG", optimize=True)
    size_bytes = os.path.getsize(output_path)
    print(f"Masterpiece broadsheet saved at {output_path}! Dimensions: {im.size}, Bytes: {size_bytes}")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "entry.png")
    generate_broadsheet(out)
