#!/usr/bin/env python3
"""
Render an HTML file to a PNG with headless Chrome. No image model or API.

Write the graphic as HTML or SVG and screenshot it. Keep brand-specific colours,
fonts, and assets in the input file rather than this reusable helper.

Usage:
  python3 scripts/render_graphic.py graphics/templates/blackout-chart.html --date 2026-06-03
  python3 scripts/render_graphic.py some.html --out path/to/image.png --size 1080x1080

Inline any local JavaScript dependencies into the input when rendering must work
without network access.
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
QUEUE_DIR = REPO_ROOT / "work/queue"   # set this to wherever finished posts should land
MAC_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def find_chrome():
    configured = os.environ.get("CHROME_BIN")
    if configured:
        return configured
    if Path(MAC_CHROME).exists():
        return MAC_CHROME
    for command in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        found = shutil.which(command)
        if found:
            return found
    return None


def main():
    p = argparse.ArgumentParser(description="Render HTML to PNG via headless Chrome")
    p.add_argument("html", help="Path to the HTML file to render")
    p.add_argument("--date", help="Queue date YYYY-MM-DD -> saves to that folder's image.png")
    p.add_argument("--out", help="Explicit output path (overrides --date)")
    p.add_argument("--size", default="1080x1080", help="WxH window size, e.g. 1080x1080")
    p.add_argument("--wait", type=int, default=2000, help="virtual-time-budget ms for JS")
    args = p.parse_args()

    html = Path(args.html).resolve()
    if not html.exists():
        sys.exit(f"No such HTML file: {html}")

    if args.out:
        out = Path(args.out)
    elif args.date:
        out = QUEUE_DIR / args.date / "image.png"
        if not out.parent.exists():
            sys.exit(f"No queue folder for {args.date}")
    else:
        sys.exit("Provide --date or --out")

    w, h = args.size.lower().split("x")
    chrome = find_chrome()
    if not chrome:
        sys.exit("Chrome not found. Install Chrome/Chromium or set CHROME_BIN.")
    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        chrome, "--headless", "--disable-gpu",
        f"--screenshot={out}", f"--window-size={w},{h}",
        f"--virtual-time-budget={args.wait}",
        "--default-background-color=FFFFFFFF", str(html),
    ]
    subprocess.run(cmd, stderr=subprocess.DEVNULL, check=False)
    if out.exists():
        print(f"Saved {out} ({out.stat().st_size // 1024} KB)")
    else:
        sys.exit("Render produced no file")


if __name__ == "__main__":
    main()
