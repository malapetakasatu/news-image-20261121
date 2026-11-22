import math
import os
from PIL import Image, ImageDraw, ImageFont

def generate_broadsheet(output_path):
    WIDTH, HEIGHT = 1024, 1024
    im = Image.new("RGB", (WIDTH, HEIGHT), "#0b1329") # Premium midnight blue canvas
    draw = ImageDraw.Draw(im)

    # Fonts
    font_serif_b = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
    font_serif_i = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
    font_sans_b = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    font_sans_r = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

    f_top = ImageFont.truetype(font_sans_b, 12)
    f_masthead = ImageFont.truetype(font_serif_b, 54)
    f_deck = ImageFont.truetype(font_serif_i, 16)
    
    f_hub_title = ImageFont.truetype(font_sans_b, 15)
    f_hub_sub = ImageFont.truetype(font_sans_b, 11)
    
    f_panel_head = ImageFont.truetype(font_sans_b, 17)
    f_panel_sub = ImageFont.truetype(font_sans_b, 12)
    f_card_tag = ImageFont.truetype(font_sans_b, 11)
    f_panel_badge = ImageFont.truetype(font_sans_b, 10)
    f_panel_src = ImageFont.truetype(font_sans_b, 10)
    
    f_footer_bold = ImageFont.truetype(font_sans_b, 11)
    f_footer_reg = ImageFont.truetype(font_sans_r, 10)

    # Palette
    GOLD = "#f59e0b"
    GOLD_LIGHT = "#fef3c7"
    RED_ACCENT = "#ef4444"
    BLUE_ACCENT = "#38bdf8"
    GREEN_ACCENT = "#22c55e"
    WHITE = "#ffffff"
    OFF_WHITE = "#f8fafc"
    PANEL_BG = "#131f37"
    PANEL_BORDER = "#1e293b"
    CARD_OUTLINE = "#334155"

    def pill(x1, y1, x2, y2, fill=None, outline=None, r=5):
        draw.rounded_rectangle([int(x1), int(y1), int(x2), int(y2)], radius=r, fill=fill, outline=outline)

    def rect(x1, y1, x2, y2, fill=None, outline=None, width=1):
        draw.rectangle([int(x1), int(y1), int(x2), int(y2)], fill=fill, outline=outline, width=width)

    # 1. TOP HEADER BANNER (y: 12 to 38)
    pill(16, 10, WIDTH - 16, 36, fill="#b91c1c", r=4)
    draw.text((28, 23), "THE WORLD IN ONE DAY · SATURDAY 21 NOVEMBER 2026", fill=WHITE, font=f_top, anchor="lm")
    draw.text((WIDTH - 28, 23), "SIX GLOBAL BEATS · VERIFIED PRIMARY SOURCES · STRICT SINGLE-DAY RECORD", fill=WHITE, font=f_top, anchor="rm")

    # 2. PROMINENT DATE MASTHEAD (y: 42 to 102)
    draw.text((WIDTH // 2, 62), "Saturday 21 November 2026", fill=WHITE, font=f_masthead, anchor="mm")
    draw.text((WIDTH // 2, 94), "COP31 climate summit in overtime · 3 missiles intercepted over Riyadh · M6.7 earthquake shakes Peru", fill="#94a3b8", font=f_deck, anchor="mm")
    draw.line([(24, 110), (WIDTH - 24, 110)], fill="#334155", width=2)

    # 3. CENTRAL GLOBE HUB (Center at x: 512, y: 512, radius: 135px)
    cx, cy, cr = 512, 512, 135
    # Outer glow rings
    draw.ellipse([cx - cr - 16, cy - cr - 16, cx + cr + 16, cy + cr + 16], outline="#1e293b", width=1)
    draw.ellipse([cx - cr - 8, cy - cr - 8, cx + cr + 8, cy + cr + 8], outline="#334155", width=2)
    # Ocean sphere
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill="#0284c7", outline="#38bdf8", width=3)
    
    # Continents on the globe
    draw.chord([cx - 105, cy - 75, cx + 35, cy + 65], 40, 220, fill="#22c55e")
    draw.chord([cx - 45, cy - 110, cx + 105, cy - 10], 120, 310, fill="#16a34a")
    draw.chord([cx - 70, cy + 25, cx + 80, cy + 115], 0, 180, fill="#22c55e")
    draw.chord([cx + 20, cy - 65, cx + 110, cy + 30], 60, 250, fill="#15803d")
    
    # Latitude / Longitude grid lines
    draw.ellipse([cx - cr, cy - cr // 2, cx + cr, cy + cr // 2], outline="#38bdf8", width=1)
    draw.line([(cx, cy - cr), (cx, cy + cr)], fill="#38bdf8", width=1)
    draw.line([(cx - cr, cy), (cx + cr, cy)], fill="#38bdf8", width=1)

    # Hub Center Badge
    pill(cx - 95, cy - 28, cx + 95, cy + 28, fill="#0f172a", outline=GOLD, r=8)
    draw.text((cx, cy - 8), "THE WORLD IN ONE DAY", fill=GOLD, font=f_hub_title, anchor="mm")
    draw.text((cx, cy + 12), "21 NOVEMBER 2026", fill=WHITE, font=f_hub_sub, anchor="mm")

    # 4. SIX SURROUNDING VIGNETTES / STORY PANELS
    # Panel layout:
    # Top-Left (1), Top-Right (2)
    # Mid-Left (3), Mid-Right (4)
    # Bottom-Left (5), Bottom-Right (6)
    
    pw, ph = 340, 240 # Panel width & height
    
    # Coordinates of 6 panels
    panels = [
        # 1. Top-Left: RIYADH MISSILES
        (20, 122, "1 · MIDDLE EAST & GULF", RED_ACCENT, "RIYADH: 3 MISSILES DOWNED", "Patriot batteries intercept 3 ballistic missiles over capital; Bahrain naval alerts raised.", "Reuters · AFP · Coalition Cmd", "OFFICIAL", "missiles"),
        
        # 2. Top-Right: PERU QUAKE
        (WIDTH - 20 - pw, 122, "2 · NATURAL DISASTERS", "#b45309", "PERU: M6.7 DEEP QUAKE", "Magnitude 6.7 deep tremor strikes Carhuamayo at 00:09 UTC; 0 deaths, 0 tsunami risk.", "USGS · IGP Lima", "USGS VERIFIED", "quake"),
        
        # 3. Mid-Left: COP31 OVERTIME
        (20, 390, "3 · CLIMATE & ENVIRONMENT", BLUE_ACCENT, "COP31 ENTERS OVERTIME", "Antalya talks deadlock on Day 13 as 200 nations split over draft omitting fossil phaseout.", "AP · AFP · Al Jazeera", "DAY 13 DEADLOCK", "climate"),
        
        # 4. Mid-Right: CRIMEA KERCH BRIDGE
        (WIDTH - 20 - pw, 390, "4 · EUROPE & CONFLICT", "#6366f1", "CRIMEA: KERCH BRIDGE ALERT", "Zelensky warns Kerch bridge \"will not stand\"; Russian strikes injure 42 in Kryvyi Rih.", "NBC News · Kyiv Ind.", "HIGH ALERT", "bridge"),
        
        # 5. Bottom-Left: IRAN DRONE & TARIFFS
        (20, 658, "5 · GEOPOLITICS & TECH", "#8b5cf6", "HORMUZ: US DRONE DOWNED", "Iran claims downing US MQ-9 drone; Trump vows punitive tariffs on foreign AI compute.", "IRIB · ABC News · ToI", "REPORTED", "drone"),
        
        # 6. Bottom-Right: SPORTS & MARKETS
        (WIDTH - 20 - pw, 658, "6 · SPORTS & MARKETS", GREEN_ACCENT, "LAS VEGAS F1 & CRICKET", "Russell tops wet Las Vegas GP practice; Rahul 124* anchors India; Bitcoin at $58,983.", "Formula 1 · AFP · CoinGecko", "OFFICIAL", "sports"),
    ]

    for px, py, tag, tag_col, head, body, src, badge, icon_type in panels:
        # Background card
        pill(px, py, px + pw, py + ph, fill=PANEL_BG, outline=CARD_OUTLINE, r=8)
        
        # Header banner inside card
        pill(px, py, px + pw, py + 26, fill="#0f172a", outline=CARD_OUTLINE, r=8)
        draw.text((px + 10, py + 13), tag, fill=tag_col, font=f_card_tag, anchor="lm")
        pill(px + pw - 85, py + 4, px + pw - 6, py + 22, fill=tag_col, r=3)
        draw.text((px + pw - 45, py + 13), badge, fill="#ffffff" if tag_col != GOLD else "#000000", font=f_panel_badge, anchor="mm")

        # Graphic Scene Box inside card (x: px + 8, y: py + 32, w: pw - 16, h: 96)
        gx, gy, gw, gh = px + 8, py + 32, pw - 16, 96
        pill(gx, gy, gx + gw, gy + gh, fill="#050a17", outline="#1e293b", r=5)

        if icon_type == "missiles":
            # Riyadh night skyline + intercept bursts
            for bx, bh, bw in [(0, 35, 30), (35, 55, 35), (75, 40, 25), (105, 70, 40), (150, 45, 30), (185, 80, 40), (230, 50, 35), (270, 65, 35)]:
                draw.rectangle([gx + bx, gy + gh - bh, gx + bx + bw, gy + gh], fill="#020611")
                for wy in range(gy + gh - bh + 6, gy + gh - 4, 8):
                    for wx in range(gx + bx + 5, gx + bx + bw - 5, 8):
                        draw.rectangle([wx, wy, wx + 2, wy + 3], fill="#ffea78" if (wx * wy) % 2 == 0 else "#38bdf8")
            # Arcs
            for t in range(40):
                u = t / 40.0
                ax1 = (1-u)**2 * (gx + 30) + 2*(1-u)*u*(gx + 90) + u**2*(gx + 150)
                ay1 = (1-u)**2 * (gy + gh) + 2*(1-u)*u*(gy + 35) + u**2*(gy + 30)
                draw.point((ax1, ay1), fill="#ffdd44")
                draw.point((ax1+1, ay1), fill="#ffdd44")
                ax2 = (1-u)**2 * (gx + gw - 30) + 2*(1-u)*u*(gx + gw - 90) + u**2*(gx + 180)
                ay2 = (1-u)**2 * (gy + gh) + 2*(1-u)*u*(gy + 40) + u**2*(gy + 35)
                draw.point((ax2, ay2), fill="#ff9933")
            for bx, by in [(gx + 150, gy + 30), (gx + 180, gy + 35)]:
                draw.ellipse([bx - 6, by - 6, bx + 6, by + 6], fill="#ffffff")
                for dx, dy in [(-12, 0), (12, 0), (0, -12), (0, 12), (-8, -8), (8, 8), (-8, 8), (8, -8)]:
                    draw.line([(bx, by), (bx + dx, by + dy)], fill="#f59e0b", width=1)
            pill(gx + 8, gy + gh - 22, gx + 155, gy + gh - 6, fill="#000000", r=2)
            draw.text((gx + 81, gy + gh - 14), "Patriot Battery Intercepts", fill="#ffffff", font=f_panel_src, anchor="mm")

        elif icon_type == "quake":
            # Peru Andes & Seismograph
            seismo = [
                (gx + 10, gy + 50), (gx + 35, gy + 50), (gx + 40, gy + 35), (gx + 45, gy + 65),
                (gx + 50, gy + 20), (gx + 55, gy + 80), (gx + 60, gy + 15), (gx + 65, gy + 85),
                (gx + 70, gy + 30), (gx + 75, gy + 70), (gx + 80, gy + 45), (gx + 90, gy + 50),
                (gx + 120, gy + 50), (gx + 125, gy + 38), (gx + 130, gy + 62), (gx + 140, gy + 50)
            ]
            for k in range(len(seismo) - 1):
                draw.line([seismo[k], seismo[k+1]], fill=RED_ACCENT, width=2)
            # Andes mountain peaks
            draw.polygon([(gx + 155, gy + gh), (gx + 200, gy + 35), (gx + 235, gy + 60), (gx + 270, gy + 25), (gx + gw, gy + gh)], fill="#78350f")
            draw.polygon([(gx + 185, gy + gh), (gx + 225, gy + 45), (gx + 275, gy + gh)], fill="#92400e")
            # Metric badges
            pill(gx + 10, gy + 8, gx + 135, gy + 26, fill="#78350f", r=3)
            draw.text((gx + 72, gy + 17), "MAGNITUDE 6.7", fill=WHITE, font=f_panel_badge, anchor="mm")
            pill(gx + gw - 120, gy + gh - 22, gx + gw - 8, gy + gh - 6, fill="#000000", r=2)
            draw.text((gx + gw - 64, gy + gh - 14), "Depth: 108 km · Carhuamayo", fill="#ffffff", font=f_panel_src, anchor="mm")

        elif icon_type == "climate":
            # Earth globe + +1.5C thermometer + Clock
            gx_c, gy_c = gx + 55, gy + 48
            draw.ellipse([gx_c - 30, gy_c - 30, gx_c + 30, gy_c + 30], fill="#0284c7", outline="#38bdf8", width=2)
            draw.chord([gx_c - 22, gy_c - 16, gx_c + 8, gy_c + 14], 40, 220, fill="#22c55e")
            # Thermometer
            tx = gx + 155
            rect(tx - 5, gy + 15, tx + 5, gy + 75, fill="#ffffff", outline="#64748b", width=1)
            draw.ellipse([tx - 12, gy + 68, tx + 12, gy + 90], fill=RED_ACCENT, outline="#64748b")
            rect(tx - 3, gy + 30, tx + 3, gy + 72, fill=RED_ACCENT)
            draw.text((tx + 18, gy + 20), "+1.5°C", fill=RED_ACCENT, font=f_panel_head)
            draw.text((tx + 18, gy + 40), "THRESHOLD", fill="#94a3b8", font=f_panel_src)
            # Clock
            cx_c, cy_c = gx + 250, gy + 48
            draw.ellipse([cx_c - 28, cy_c - 28, cx_c + 28, cy_c + 28], fill="#ffffff", outline="#0f172a", width=2)
            draw.line([(cx_c, cy_c), (cx_c + 14, cy_c - 8)], fill="#000000", width=3)
            draw.line([(cx_c, cy_c), (cx_c + 3, cy_c - 18)], fill="#000000", width=2)
            pill(cx_c - 32, gy + gh - 22, cx_c + 32, gy + gh - 6, fill="#0f172a", r=2)
            draw.text((cx_c, gy + gh - 14), "DAY 13 OVERTIME", fill=WHITE, font=f_panel_src, anchor="mm")

        elif icon_type == "bridge":
            # Kerch Bridge + Targeting crosshair
            rect(gx, gy + gh - 25, gx + gw, gy + gh, fill="#0284c7")
            draw.line([(gx + 10, gy + gh - 25), (gx + gw - 10, gy + gh - 25)], fill="#ffffff", width=4)
            draw.line([(gx + 80, gy + 20), (gx + 80, gy + gh - 25)], fill="#e2e8f0", width=5)
            draw.line([(gx + 210, gy + 20), (gx + 210, gy + gh - 25)], fill="#e2e8f0", width=5)
            draw.arc([gx + 10, gy + 15, gx + 150, gy + gh], 200, 340, fill="#f59e0b", width=2)
            draw.arc([gx + 140, gy + 15, gx + 280, gy + gh], 200, 340, fill="#f59e0b", width=2)
            # Reticle
            draw.ellipse([gx + 130, gy + 25, gx + 165, gy + 60], outline=RED_ACCENT, width=2)
            draw.line([(gx + 147, gy + 18), (gx + 147, gy + 67)], fill=RED_ACCENT, width=2)
            draw.line([(gx + 123, gy + 42), (gx + 172, gy + 42)], fill=RED_ACCENT, width=2)
            pill(gx + 8, gy + gh - 22, gx + 150, gy + gh - 6, fill="#000000", r=2)
            draw.text((gx + 79, gy + gh - 14), "Crimea Kerch Strait Bridge", fill="#ffffff", font=f_panel_src, anchor="mm")

        elif icon_type == "drone":
            # MQ-9 Drone + AI Compute Chip
            dcx, dcy = gx + 85, gy + 45
            draw.line([(dcx - 45, dcy), (dcx + 45, dcy)], fill="#94a3b8", width=4)
            draw.line([(dcx, dcy - 22), (dcx, dcy + 22)], fill="#94a3b8", width=5)
            draw.line([(dcx - 30, dcy - 10), (dcx - 30, dcy + 10)], fill="#cbd5e1", width=2)
            draw.line([(dcx + 30, dcy - 10), (dcx + 30, dcy + 10)], fill="#cbd5e1", width=2)
            draw.ellipse([dcx + 36, dcy - 7, dcx + 46, dcy + 7], fill=RED_ACCENT)
            pill(gx + 10, gy + gh - 22, gx + 145, gy + gh - 6, fill="#000000", r=2)
            draw.text((gx + 77, gy + gh - 14), "MQ-9 Reaper / Hormuz", fill="#ffffff", font=f_panel_src, anchor="mm")
            # AI Chip
            ccx, ccy = gx + 225, gy + 45
            rect(ccx - 28, ccy - 28, ccx + 28, ccy + 28, fill="#1e293b", outline="#38bdf8", width=2)
            draw.text((ccx, ccy - 6), "AI", fill="#38bdf8", font=f_panel_head, anchor="mm")
            draw.text((ccx, ccy + 12), "TARIFF", fill="#f59e0b", font=f_panel_src, anchor="mm")
            for off in [-18, 0, 18]:
                draw.line([(ccx + off, ccy - 34), (ccx + off, ccy - 28)], fill="#38bdf8", width=2)
                draw.line([(ccx + off, ccy + 28), (ccx + off, ccy + 34)], fill="#38bdf8", width=2)
                draw.line([(ccx - 34, ccy + off), (ccx - 28, ccy + off)], fill="#38bdf8", width=2)
                draw.line([(ccx + 28, ccy + off), (ccx + 34, ccy + off)], fill="#38bdf8", width=2)

        elif icon_type == "sports":
            # F1 Car & Cricket Century
            fcx, fcy = gx + 95, gy + 45
            rect(fcx - 50, fcy - 8, fcx + 40, fcy + 8, fill=RED_ACCENT)
            rect(fcx - 14, fcy - 18, fcx + 14, fcy - 8, fill="#0f172a")
            draw.ellipse([fcx - 38, fcy + 5, fcx - 20, fcy + 23], fill="#0a0a0a")
            draw.ellipse([fcx + 16, fcy + 5, fcx + 34, fcy + 23], fill="#0a0a0a")
            draw.text((fcx + 45, fcy - 10), "P1", fill="#ffffff", font=f_panel_head)
            draw.text((fcx + 45, fcy + 8), "1:34.041", fill="#a7f3d0", font=f_panel_src)
            # Cricket bat & ball
            bcx, bcy = gx + 230, gy + 45
            draw.line([(bcx - 18, bcy + 20), (bcx + 10, bcy - 16)], fill="#f59e0b", width=5)
            draw.ellipse([bcx + 14, bcy - 10, bcx + 28, bcy + 4], fill="#dc2626")
            draw.text((bcx, bcy + 24), "124* RAHUL", fill="#ffffff", font=f_panel_badge, anchor="mm")
            pill(gx + 10, gy + gh - 22, gx + 175, gy + gh - 6, fill="#000000", r=2)
            draw.text((gx + 92, gy + gh - 14), "Las Vegas GP & NZ Test", fill="#ffffff", font=f_panel_src, anchor="mm")

        # Story Headline (Large, Crisp 17pt Bold)
        draw.text((px + 10, py + 136), head, fill=WHITE, font=f_panel_head)
        
        # Story Short Summary (12.5pt, Perfectly Wrapped)
        words = body.split()
        lines = []
        cur = []
        for w in words:
            t_line = " ".join(cur + [w])
            bbox = draw.textbbox((0, 0), t_line, font=f_panel_sub)
            if bbox[2] - bbox[0] <= pw - 20:
                cur.append(w)
            else:
                if cur: lines.append(" ".join(cur))
                cur = [w]
        if cur: lines.append(" ".join(cur))
        
        sy = py + 160
        for l in lines[:3]:
            draw.text((px + 10, sy), l, fill="#cbd5e1", font=f_panel_sub)
            sy += 17

        # Source Attribution footer inside card
        draw.text((px + 10, py + ph - 18), src, fill="#94a3b8", font=f_panel_src)

    # 5. FOOTER VERIFICATION STRIP (y: 955 to 1014)
    pill(16, 955, WIDTH - 16, 1012, fill="#0f172a", outline="#334155", r=5)
    draw.text((28, 970), "STRICT 24-HOUR CHRONICLE · RECORD OF RECORD FOR SATURDAY 21 NOVEMBER 2026", fill=GOLD, font=f_footer_bold)
    draw.text((28, 990), "Verified wires: Reuters, AP, AFP, USGS, Formula 1, ESPNcricinfo. Single-calendar-day global dispatch.", fill="#94a3b8", font=f_footer_reg)
    draw.text((WIDTH - 28, 980), "GLOBAL NEWS DESK · EDITION 2026.11.21", fill=WHITE, font=f_footer_bold, anchor="rm")

    im.save(output_path, "PNG", optimize=True)
    print(f"Masterpiece Magazine Broadsheet saved at {output_path}! Size: {im.size}, Bytes: {os.path.getsize(output_path)}")

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "entry.png")
    generate_broadsheet(out)
