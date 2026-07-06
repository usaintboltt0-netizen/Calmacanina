"""Generate real OG image for CalmaCanina landing page (1200×630px)."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# ── Background gradient (dark green tones from the site) ──
for y in range(H):
    r = int(23 + (y / H) * 20)
    g = int(49 + (y / H) * 30)
    b = int(40 + (y / H) * 18)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# ── Subtle radial glow ──
for r in range(400, 0, -1):
    alpha = max(0, int(32 * (1 - r / 400)))
    draw.ellipse([(W//2 - r, H//2 - r - 60), (W//2 + r, H//2 + r - 60)],
                 fill=(212, 165, 116, alpha) if r > 200 else (82, 183, 136, alpha))

# ── Decorative border (like hero::before) ──
border_color = (255, 255, 255, 40)
draw.rounded_rectangle([(30, 30), (W - 30, H - 30)], radius=40,
                       outline=border_color, width=1)

# ── Try to use available fonts ──
FONTS_DIRS = [
    r"C:\Windows\Fonts",
    "/usr/share/fonts",
    "/System/Library/Fonts",
]

def find_font(name, fallback_size=48):
    """Try to find the font file, return default size-based font if not found."""
    for fd in FONTS_DIRS:
        if not os.path.isdir(fd):
            continue
        for fname in os.listdir(fd):
            if name.lower() in fname.lower() and fname.lower().endswith((".ttf", ".otf")):
                try:
                    return ImageFont.truetype(os.path.join(fd, fname), fallback_size)
                except Exception:
                    pass
    return ImageFont.load_default()

serif = find_font("Playfair", 68)
serif_sm = find_font("Playfair", 40)
sans = find_font("Inter", 28)
sans_badge = find_font("Inter", 22)

# ── Badge ──
badge_text = "MÉTODO GUIADO · 21 DÍAS"
badge_bbox = draw.textbbox((0, 0), badge_text, font=sans_badge)
badge_w = badge_bbox[2] - badge_bbox[0] + 40
badge_h = badge_bbox[3] - badge_bbox[1] + 20
badge_x = 60
badge_y = 80
draw.rounded_rectangle([(badge_x, badge_y), (badge_x + badge_w, badge_y + badge_h)],
                       radius=30, fill=(255, 255, 255, 30), outline=(255, 255, 255, 60), width=1)
draw.text((badge_x + 20, badge_y + 8), badge_text, fill=(255, 228, 189), font=sans_badge)

# ── Title ──
title = "Ayudá a tu perro a\ntranquilo cuando salís de casa"
title_x = 60
title_y = 150
draw.text((title_x, title_y), title, fill=(255, 255, 255), font=serif)

# ── Subtitle ──
subtitle = "Plan guiado de 21 días para reducir ansiedad por separación"
draw.text((title_x, title_y + 170), subtitle, fill=(200, 210, 200), font=sans)

# ── Price pill ──
price_text = "$47 USD · Garantía 30 días"
price_bbox = draw.textbbox((0, 0), price_text, font=sans_badge)
price_w = price_bbox[2] - price_bbox[0] + 50
price_h = price_bbox[3] - price_bbox[1] + 24
price_x = title_x
price_y = title_y + 240
draw.rounded_rectangle([(price_x, price_y), (price_x + price_w, price_y + price_h)],
                       radius=30, fill=(184, 149, 111, 200))
draw.text((price_x + 25, price_y + 10), price_text, fill=(24, 51, 43), font=sans_badge)

# ── Dog ear icon (right side) ──
# Draw a simple paw/heart shape
cx, cy = W - 220, H // 2
for i in range(3):
    r = 40 - i * 5
    draw.ellipse([(cx - r, cy - r + i * 60 - 40),
                  (cx + r, cy + r + i * 60 - 40)],
                 fill=(212, 165, 116, 60 + i * 20))
    draw.ellipse([(cx - r - 50, cy - r + i * 60 - 20),
                  (cx + r - 50, cy + r + i * 60 - 20)],
                 fill=(212, 165, 116, 40 + i * 15))
    draw.ellipse([(cx - r + 50, cy - r + i * 60 - 20),
                  (cx + r + 50, cy + r + i * 60 - 20)],
                 fill=(212, 165, 116, 40 + i * 15))

# Big paw pad center
draw.ellipse([(cx - 60, cy + 70), (cx + 60, cy + 200)],
             fill=(212, 165, 116, 50))

# ═══ Footer bar ═══
footer_y = H - 60
draw.rectangle([(70, footer_y), (W - 70, footer_y + 1)], fill=(255, 255, 255, 60))
footer_text = "calmacanina.com"
draw.text((W // 2 - 100, footer_y + 10), footer_text,
          fill=(255, 255, 255, 120), font=sans_badge)

# ── Convert to RGB and save ──
img_rgb = Image.new("RGB", (W, H), (23, 49, 40))
img_rgb.paste(img, (0, 0), img)
img_rgb.save("og-calmacanina.jpg", "JPEG", quality=95)

print("✅ OG image generated: og-calmacanina.jpg")