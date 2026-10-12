import argparse
from pathlib import Path
from PIL import Image
import pikepdf
from carousel_common import load_manifest

def verify(path):
    d,files=load_manifest(path)
    if d.get('format')=='multi_image':return {'assets':len(files),'hashes_order_dimensions':'pass','visual_review_required':True}
    root=Path(path).resolve().parent;pdfpath=(root/d['pdf']).resolve()
    if not pdfpath.is_relative_to(root):raise ValueError('PDF outside manifest directory')
    with pikepdf.open(pdfpath) as pdf:
        if len(pdf.pages)!=len(files):raise ValueError('PDF page count mismatch')
        for i,(page,f) in enumerate(zip(pdf.pages,files),1):
            ims=list(page.images.values())
            if len(ims)!=1:raise ValueError('expected one image per page')
            embedded=pikepdf.PdfImage(ims[0]).as_pil_image()
            with Image.open(f) as im:
                im=im.convert(embedded.mode)
                if im.size!=embedded.size or im.tobytes()!=embedded.tobytes():raise ValueError(f'PDF page {i} differs from manifest image')
    return {'pages':len(files),'pixel_order':'pass','visual_review_required':True}
if __name__=='__main__':
    import json
    p=argparse.ArgumentParser();p.add_argument('manifest');a=p.parse_args();print(json.dumps(verify(a.manifest),indent=2))
