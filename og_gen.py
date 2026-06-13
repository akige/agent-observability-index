#!/usr/bin/env python3
"""One-off generator for the static OG image (1200x630). Output: static/og.png.
Run with the Pillow venv; build.py just copies static/ into the site (no dep)."""
import os, sys
from PIL import Image, ImageDraw, ImageFont

N = sys.argv[1] if len(sys.argv) > 1 else "116"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#020617")
d = ImageDraw.Draw(img)

# border
d.rounded_rectangle([40, 40, W - 40, H - 40], radius=24, outline="#1e293b", width=2)

# radar glyph (ring + dot)
cx, cy = 120, 140
d.ellipse([cx - 34, cy - 34, cx + 34, cy + 34], outline="#34d399", width=9)
d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill="#34d399")

f_brand = ImageFont.truetype(FB, 40)
f_big = ImageFont.truetype(FB, 70)
f_sub = ImageFont.truetype(FR, 32)

d.text((184, 122), "AgentObs Index", font=f_brand, fill="#ffffff")
d.text((100, 250), "The neutral index of", font=f_big, fill="#ffffff")
d.text((100, 338), "AI agent observability tooling", font=f_big, fill="#34d399")
d.text((100, 470), f"{N} tools  ·  observability · evals · guardrails · cost",
       font=f_sub, fill="#94a3b8")
d.text((100, 512), "facts checked against primary sources  ·  tools.panshi.io",
       font=f_sub, fill="#64748b")

os.makedirs("static", exist_ok=True)
img.save("static/og.png", "PNG", optimize=True)
print("wrote static/og.png", os.path.getsize("static/og.png"), "bytes")
