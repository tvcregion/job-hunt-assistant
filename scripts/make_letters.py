#!/usr/bin/env python3
"""Render one-page cover letters from JSON into PDFs.

    python3 make_letters.py --dir <job-hunt folder>            # every letter
    python3 make_letters.py --dir <job-hunt folder> slug1 slug2  # only these

Reads <dir>/profile.json and <dir>/letters.json, writes <dir>/letters/Cover_Letter_<slug>.pdf.

profile.json:  {"name": "...", "contact": "City, Country · relocating to X · +phone · email",
                "links": "linkedin.com/in/...", "sign_off": "Kind regards,", "date_locale": "en"}
letters.json:  [{"slug", "company", "role", "location"?, "salutation"?, "paragraphs": [...],
                 "date"?: "13 November 2026", "cv"?: "CV file used for this application"}]
"""
import argparse
import datetime
import html
import json
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from html_to_pdf import render  # noqa: E402

TEMPLATE = """<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 22mm 20mm; }}
body {{ font-family: -apple-system, "Helvetica Neue", Helvetica, Arial, sans-serif;
       font-size: 10.5pt; line-height: 1.45; color: #111; margin: 0; }}
h1 {{ font-size: 20pt; margin: 0 0 4px; }}
.contact {{ color: #555; font-size: 9.5pt; line-height: 1.5; }}
.date {{ margin-top: 22px; }}
.re {{ font-weight: 600; margin-top: 18px; }}
p {{ margin: 0 0 10px; }}
.sal {{ margin-top: 14px; }}
</style></head><body>
<h1>{name}</h1>
<div class="contact">{contact}{links}</div>
<div class="date">{date}</div>
<div class="re">Re: {role}{loc}</div>
<p class="sal">{salutation}</p>
{body}
<p>{sign_off}<br>{name}</p>
</body></html>"""


def letter_html(profile: dict, letter: dict) -> str:
    e = html.escape
    today = datetime.date.today()
    date = letter.get("date") or f"{today.day} {today.strftime('%B %Y')}"
    links = profile.get("links")
    return TEMPLATE.format(
        name=e(profile["name"]),
        contact=e(profile.get("contact", "")),
        links=("<br>" + e(links)) if links else "",
        date=e(date),
        role=e(letter["role"]),
        loc=(", " + e(letter["location"])) if letter.get("location") else "",
        salutation=e(letter.get("salutation") or f"Dear {letter['company']} Hiring Team,"),
        body="\n".join(f"<p>{e(p)}</p>" for p in letter["paragraphs"]),
        sign_off=e(profile.get("sign_off", "Kind regards,")),
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="job-hunt working folder")
    ap.add_argument("slugs", nargs="*")
    a = ap.parse_args()
    root = pathlib.Path(a.dir).expanduser()
    profile = json.loads((root / "profile.json").read_text())
    letters = json.loads((root / "letters.json").read_text())
    for letter in letters:
        if a.slugs and letter["slug"] not in a.slugs:
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
            fh.write(letter_html(profile, letter))
            src = pathlib.Path(fh.name)
        try:
            render(src, root / "letters" / f"Cover_Letter_{letter['slug']}.pdf")
        finally:
            src.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
