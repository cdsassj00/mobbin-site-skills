"""Offline design selection. Standard library only; no network or model calls."""
import json
from pathlib import Path
import re

SKILL = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((SKILL / 'references' / name).read_text(encoding='utf-8'))


def load_brief(path):
    brief = json.loads(Path(path).read_text(encoding='utf-8'))
    if not isinstance(brief, dict):
        raise ValueError('Brief must be a JSON object')
    for key in ('purpose', 'audience', 'primary_action'):
        if not isinstance(brief.get(key, ''), str):
            raise ValueError(f'{key} must be a string')
    for key in ('vibes', 'pages', 'features'):
        if not isinstance(brief.get(key, []), list) or any(not isinstance(v, str) for v in brief.get(key, [])):
            raise ValueError(f'{key} must be an array of strings')
    for key in ('brand', 'constraints'):
        if not isinstance(brief.get(key, {}), dict):
            raise ValueError(f'{key} must be an object')
    avoid = brief.get('constraints', {}).get('avoid', [])
    if not isinstance(avoid, list) or any(not isinstance(v, str) for v in avoid):
        raise ValueError('constraints.avoid must be an array of strings')
    return brief


def contrast(a, b):
    def luminance(hex_color):
        channels = [int(hex_color[i:i+2], 16)/255 for i in (1, 3, 5)]
        linear = [c/12.92 if c <= .04045 else ((c+.055)/1.055)**2.4 for c in channels]
        return sum(c*w for c,w in zip(linear, (.2126,.7152,.0722)))
    hi, lo = sorted([luminance(a), luminance(b)], reverse=True)
    return (hi+.05)/(lo+.05)


def pick_layout(brief):
    text = ' '.join([brief.get('purpose', ''), brief.get('primary_action', ''), *brief.get('pages', []), *brief.get('features', [])]).casefold()
    layouts = read('layouts.json')
    scores = [(sum(3 for word in x['keywords'] if word.casefold() in text)+sum(1 for word in x['actions'] if word.casefold() in text), -i, x) for i,x in enumerate(layouts)]
    return max(scores, key=lambda x: (x[0], x[1]))[2]


def recommend(brief):
    layout = pick_layout(brief)
    affinity = {
        'landing': ['precise-saas','dark-developer','corporate-trust','soft-gradient','technical-grid'],
        'dashboard': ['data-dense','refined-finance','technical-grid','precise-saas'],
        'commerce': ['bold-commerce','luxury-minimal','tactile-natural'],
        'editorial': ['warm-editorial','monochrome-portfolio','community-friendly'],
        'portfolio': ['monochrome-portfolio','playful-studio','brutalist-display','luxury-minimal'],
        'booking': ['travel-photographic','luxury-minimal','calm-health','tactile-natural'],
        'learning': ['learning-colorful','community-friendly','precise-saas','warm-editorial'],
        'directory': ['corporate-trust','data-dense','community-friendly','precise-saas']
    }
    purpose = ' '.join([brief.get('purpose', ''), brief.get('primary_action', '')]).casefold()
    vibes = ' '.join(brief.get('vibes', [])).casefold()
    avoid = [x.casefold() for x in brief.get('constraints', {}).get('avoid', []) if x]
    candidates = []
    for i, style in enumerate(read('styles.json')):
        matches = [x for x in style['aliases'] if x.casefold() in vibes]
        uses = [x for x in style['purposes'] if x.casefold() in purpose]
        if any(a in style['id'].casefold() or a in style['name'].casefold() or any(a == alias.casefold() for alias in style['aliases']) for a in avoid):
            continue
        fits_layout = style['id'] in affinity[layout['id']]
        score = len(matches)*5 + len(uses)*3 + (4 if fits_layout else 0)
        candidates.append(dict(style=style, score=score, reasons=[*[f'선호: {x}' for x in matches], *[f'목적: {x}' for x in uses], *([f'구조 적합: {layout["id"]}'] if fits_layout else [])] or ['직접 일치가 없어 기본 후보로 제안'], order=i))
    candidates.sort(key=lambda x: (-x['score'], x['order']))
    # Prefer visibly distinct silhouettes among the three proposals.
    selected = []
    for c in candidates:
        if len(selected) < 3 and c['style']['silhouette'] not in {x['style']['silhouette'] for x in selected}:
            selected.append(c)
    refs = read('library.json')
    for c in selected:
        ranked = sorted([r for r in refs if r.get('usable', True)], key=lambda r: -len(set(r['tags']) & set(c['style']['reference_tags'])))
        evidence = []
        for r in ranked:
            if not set(r['tags']) & set(c['style']['reference_tags']):
                continue
            if r['site'] in {x['site'] for x in evidence}:
                continue
            o = r['observations'][0]
            evidence.append(dict(site=r['site'], reference_id=r['id'], mobbin_url=r['mobbin_url'],
                                 local_image=o.get('local_asset', f'assets/references/{o["screen_id"]}.jpg'), observation=o['note']))
            if len(evidence)==3:
                break
        c['references'] = evidence
        c.pop('order')
        c['layout'] = layout['id']
    return dict(layout=layout, directions=selected, missing=[k for k in ('purpose','audience','primary_action') if not brief.get(k)],
                scoring='Local heuristic, not a measured quality ranking. Style tokens are original presets, not measured source values.')


def css_tokens(style, accent=None):
    t = dict(style['tokens'])
    if accent:
        if not re.fullmatch(r'#[0-9a-fA-F]{6}', accent):
            raise ValueError('brand.accent must be a six-digit hex color')
        t['accent'] = accent
    t['on_accent'] = '#ffffff' if contrast(t['accent'], '#ffffff') >= contrast(t['accent'], '#111111') else '#111111'
    t['accent_ink'] = t['accent'] if contrast(t['accent'], t['surface']) >= 4.5 else t['text']
    fonts = {'sans': 'system-ui, -apple-system, "Segoe UI", sans-serif',
             'serif': 'Georgia, "Times New Roman", serif', 'mono': 'ui-monospace, Consolas, monospace'}
    values = {**{k.replace('_','-'):v for k,v in t.items() if k not in ('radius','font','max_width')},
              'radius': f'{t["radius"]}px', 'font-heading': fonts[t['font']], 'max-width': f'{t["max_width"]}px'}
    return ':root {\n'+''.join(f'  --{k}: {v};\n' for k,v in values.items())+'}\n'
