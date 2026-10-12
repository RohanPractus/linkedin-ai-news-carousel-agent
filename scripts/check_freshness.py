"""Check verified event age. Source accuracy still requires human/agent review."""
import argparse,json
from datetime import datetime,timezone

def parse_time(value):
    dt=datetime.fromisoformat(value.replace('Z','+00:00'))
    if dt.tzinfo is None: raise ValueError('timestamp must include timezone')
    return dt

def check(event,now):
    if not event.get('primary_source_urls'): raise ValueError('primary source URLs required')
    age=(now-parse_time(event['event_at'])).total_seconds()/3600
    if age<0: raise ValueError('future event rejected')
    if age>96: raise ValueError('event exceeds 96-hour freshness limit')
    return {'freshness_pass':True,'age_hours':round(age,3),'preferred':age<=72,'checked_at':now.isoformat()}

def main():
    p=argparse.ArgumentParser();p.add_argument('event');p.add_argument('--now');a=p.parse_args()
    try:
        event=json.load(open(a.event));now=parse_time(a.now) if a.now else datetime.now(timezone.utc)
        print(json.dumps(check(event,now),indent=2));return 0
    except (ValueError,KeyError) as e: print(json.dumps({'freshness_pass':False,'reason':str(e)}));return 1
if __name__=='__main__':raise SystemExit(main())
