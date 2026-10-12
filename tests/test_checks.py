import unittest,sys,json,tempfile,hashlib
from pathlib import Path
from datetime import datetime,timezone,timedelta
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_freshness import check
from carousel_common import load_manifest
from PIL import Image
class Freshness(unittest.TestCase):
 def test_boundary(self):
  now=datetime(2026,10,12,tzinfo=timezone.utc)
  for hours,passes in [(72,True),(96,True),(96.01,False),(-1,False)]:
   e={'event_at':(now-timedelta(hours=hours)).isoformat(),'primary_source_urls':['https://example.com/original']}
   if passes:self.assertTrue(check(e,now)['freshness_pass'])
   else:
    with self.assertRaises(ValueError):check(e,now)
 def test_unknown_or_unverified(self):
  for e in [{'event_at':'2026-10-12T00:00:00'}, {'primary_source_urls':[]}]:
   with self.assertRaises((ValueError,KeyError)):check(e,datetime.now(timezone.utc))
class Ordering(unittest.TestCase):
 def test_reorder_and_hash_rejected(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t);slides=[]
   for i in range(1,4):
    f=root/f'slide-{i}.png';Image.new('RGB',(40,50),(i*40,0,0)).save(f)
    slides.append({'page':i,'label':f'{i:02d} / 03','file':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
   m=root/'manifest.json';d={'format':'multi_image','slides':slides};m.write_text(json.dumps(d));self.assertEqual(len(load_manifest(m)[1]),3)
   d['slides']=[slides[1],slides[0],slides[2]];m.write_text(json.dumps(d))
   with self.assertRaises(ValueError):load_manifest(m)
   d['slides']=slides;d['slides'][0]['sha256']='bad';m.write_text(json.dumps(d))
   with self.assertRaises(ValueError):load_manifest(m)
if __name__=='__main__':unittest.main()
