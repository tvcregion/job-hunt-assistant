#!/usr/bin/env python3
"""Render an HTML file to PDF with headless Chrome/Chromium.

    python3 html_to_pdf.py cv/cv.html CV_Name.pdf

Finds Chrome on macOS, Linux and Windows; set CHROME=/path/to/chrome to override.
Prints the page count when `pdfinfo` is available, so you can keep a CV to 2 pages.
"""
import os
import pathlib
import shutil
import subprocess
import sys

CANDIDATES = [
    os.environ.get("CHROME", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]
NAMES = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"]


def find_chrome() -> str:
    for c in CANDIDATES:
        if c and pathlib.Path(c).exists():
            return c
    for n in NAMES:
        p = shutil.which(n)
        if p:
            return p
    sys.exit("Chrome/Chromium not found. Install it or set CHROME=/path/to/chrome.")


def render(src: pathlib.Path, out: pathlib.Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [find_chrome(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={out.resolve()}", src.resolve().as_uri()],
        check=True, capture_output=True,
    )
    pages = ""
    if shutil.which("pdfinfo"):
        info = subprocess.run(["pdfinfo", str(out)], capture_output=True, text=True).stdout
        pages = next((l.split()[-1] for l in info.splitlines() if l.startswith("Pages:")), "")
    print(f"{out}" + (f"  ({pages} pages)" if pages else ""))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    render(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]))
