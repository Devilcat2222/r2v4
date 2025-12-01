#!/usr/bin/env python3
"""
Generate a fonts manifest JSON file listing all files in assets/fonts/ (and optionally /fonts/) with supported font extensions.
Output path: /fonts/manifest.json (relative to project root) and /assets/fonts/manifest.json as fallback.
"""
import os, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ASSETS_FONTS = os.path.join(ROOT, 'assets', 'fonts')
FONTS_DIR = os.path.join(ROOT, 'fonts')

OUT1 = os.path.join(ROOT, 'fonts', 'manifest.json')
OUT2 = os.path.join(ROOT, 'assets', 'fonts', 'manifest.json')

EXTENSIONS = {'.woff2', '.woff', '.ttf', '.otf', '.svg', '.eot'}

files = []
for base in [ASSETS_FONTS, FONTS_DIR]:
    if os.path.isdir(base):
        for fn in os.listdir(base):
            p = os.path.join(base, fn)
            if os.path.isfile(p):
                if os.path.splitext(fn)[1].lower() in EXTENSIONS:
                    path = os.path.relpath(p, ROOT).replace('\\', '/')
                    files.append('/' + path)

# dedupe
files = sorted(list(dict.fromkeys(files)))

# Write to both outputs
os.makedirs(os.path.dirname(OUT1), exist_ok=True)
with open(OUT1, 'w') as f:
    json.dump(files, f, indent=2)

os.makedirs(os.path.dirname(OUT2), exist_ok=True)
with open(OUT2, 'w') as f:
    json.dump(files, f, indent=2)

print(f'Wrote {len(files)} fonts to {OUT1} and {OUT2}')
