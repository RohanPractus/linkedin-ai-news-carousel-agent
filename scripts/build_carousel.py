import argparse
from pathlib import Path
import img2pdf
from carousel_common import load_manifest

def main():
    p=argparse.ArgumentParser();p.add_argument('manifest');p.add_argument('--overwrite',action='store_true');a=p.parse_args()
    d,files=load_manifest(a.manifest)
    if d.get('format')=='multi_image':raise ValueError('multi-image format does not need PDF')
    root=Path(a.manifest).resolve().parent;out=(root/d['pdf']).resolve()
    if not out.is_relative_to(root):raise ValueError('PDF outside manifest directory')
    if out.exists() and not a.overwrite:raise ValueError('PDF exists; use --overwrite explicitly')
    out.write_bytes(img2pdf.convert([str(f) for f in files]));print(out)
if __name__=='__main__':main()
