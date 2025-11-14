#!/usr/bin/env python3
"""
Scan assets/icons/menu and assets/icons/setting and write assets/icons/manifest.json
Run from repo root: python3 scripts/generate_icon_manifest.py
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
icons_dir = root / 'assets' / 'icons'
menu_dir = icons_dir / 'menu'
setting_dir = icons_dir / 'setting'
manifest = {'menu': [], 'setting': []}

for p in menu_dir.glob('*'):
    if p.is_file():
        rel = p.relative_to(root).as_posix()
        manifest['menu'].append(rel)

for p in setting_dir.glob('*'):
    if p.is_file():
        rel = p.relative_to(root).as_posix()
        manifest['setting'].append(rel)

# also scan favicon presets
favicon_dir = icons_dir / 'favicon'
manifest['favicon'] = []
for p in favicon_dir.glob('*'):
    if p.is_file():
        rel = p.relative_to(root).as_posix()
        manifest['favicon'].append(rel)

# scan background presets
background_dir = icons_dir / 'background'
manifest['background'] = []
for p in background_dir.glob('*'):
    if p.is_file():
        rel = p.relative_to(root).as_posix()
        manifest['background'].append(rel)

icons_dir.mkdir(parents=True, exist_ok=True)
with open(icons_dir / 'manifest.json', 'w', encoding='utf8') as f:
    json.dump(manifest, f, indent=2)
print('Wrote', icons_dir / 'manifest.json')
