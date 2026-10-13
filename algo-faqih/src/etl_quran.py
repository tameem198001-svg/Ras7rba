# ETL for Quran text into faqih_search.db
# This script expects algo-faqih/data/raw/quran.txt to exist.
# Each line ideally: <sura_number>:<ayah_number>\t<text>

import os
import re
import sys
from pathlib import Path
# ensure src on path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from database import Database, normalize_arabic
import json


RAW_PATH = Path("algo-faqih/data/raw/quran.txt")


def parse_line(line: str):
    line = line.strip()
    if not line:
        return None
    m = re.match(r"^(\d+):(\d+)\t(.+)$", line)
    if m:
        sura, aya, text = m.group(1), m.group(2), m.group(3)
        ref = f"{sura}:{aya}"
        title = f"سورة {sura} آية {aya}"
        return ref, title, text
    parts = line.split('\t', 1)
    if len(parts) == 2:
        ref = parts[0]
        text = parts[1]
        title = ref
        return ref, title, text
    return None


def run():
    db = Database(path="algo-faqih/data/faqih_search.db")
    src = db.get_source_by_name('القرآن الكريم')
    if not src:
        sid = db.add_source('القرآن الكريم', 'quran', 1.0, {'lang': 'ar'})
    else:
        sid = src[0]

    if not RAW_PATH.exists():
        print(f"Raw Quran file not found at {RAW_PATH}. Create one with lines like '2:255\ttext'")
        db.close()
        return

    with open(RAW_PATH, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            parsed = parse_line(line)
            if not parsed:
                continue
            ref, title, text = parsed
            norm = normalize_arabic(text)
            provenance = json.dumps({'source': 'quran', 'ref': ref}, ensure_ascii=False)
            try:
                db.add_text(sid, ref, text, norm, 'quran', provenance)
            except AssertionError as e:
                print('skipping - assertion', e)
            except Exception as e:
                print('error inserting line', i, e)

    db.close()
    print('ETL complete for Quran (placeholder)')


if __name__ == '__main__':
    run()
