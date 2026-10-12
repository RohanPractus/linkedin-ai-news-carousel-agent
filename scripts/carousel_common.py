import hashlib,json
from pathlib import Path
from PIL import Image

def load_manifest(path):
    path=Path(path).resolve();d=json.loads(path.read_text());slides=d['slides']
    if not 3<=len(slides)<=7:raise ValueError('expected 3–7 assets')
    if d.get('format')=='multi_image' and len(slides)>5:raise ValueError('multi-image maximum is five')
    paths=[];size=None
    for i,s in enumerate(slides,1):
        if s['page']!=i or s['label']!=f'{i:02d} / {len(slides):02d}':raise ValueError('noncontiguous page/label order')
        f=(path.parent/s['file']).resolve()
        if not f.is_relative_to(path.parent):raise ValueError('asset outside manifest directory')
        if hashlib.sha256(f.read_bytes()).hexdigest()!=s['sha256']:raise ValueError('asset hash mismatch')
        with Image.open(f) as im:
            if size is None:size=im.size
            if im.size!=size:raise ValueError('inconsistent asset dimensions')
        paths.append(f)
    return d,paths
