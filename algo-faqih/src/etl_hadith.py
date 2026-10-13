# ETL for Hadith JSONL into faqih_search.db
# Expects algo-faqih/data/raw/hadith.jsonl where each line is a JSON object with keys: id, title, body, reference

import os
import sys
import json
from pathlib import Path
# ensure src on path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from database import Database, normalize_arabic

RAW_PATH = Path("algo-faqih/data/raw/hadith.jsonl")


def run():
    db = Database(path="algo-faqih/data/faqih_search.db")
    src = db.get_source_by_name('الحديث النبوي')
    if not src:
        sid = db.add_source('الحديث النبوي', 'hadith', 0.9, {'notes': 'placeholder'})
    else:
        sid = src[0]

    if not RAW_PATH.exists():
        print(f"Raw hadith file not found at {RAW_PATH}. Create one with JSONL lines: {"id":1, "title":"..", "body":"..", "reference":".."}")
        db.close()
        return

    with open(RAW_PATH, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                print('skipping invalid json line', i)
                continue
            title = obj.get('title') or f"hadith-{obj.get('id') or i}"
            body = obj.get('body') or ''
            ref = obj.get('reference') or obj.get('id') or f'line-{i}'
            norm = normalize_arabic(body)
            provenance = json.dumps({'source': 'hadith', 'ref': ref}, ensure_ascii=False)
            try:
                db.add_text(sid, str(ref), body, norm, 'hadith', provenance)
            except AssertionError as e:
                print('skipping - assertion', e)
            except Exception as e:
                print('error inserting hadith line', i, e)

    db.close()
    print('ETL complete for Hadith (placeholder)')


if __name__ == '__main__':
    run()
