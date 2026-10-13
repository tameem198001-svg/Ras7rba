"""02_download_hadith.py
Placeholder script to download/collect hadith datasets.
"""

import os

def download_hadith(dest_dir="data"):
    os.makedirs(dest_dir, exist_ok=True)
    path = os.path.join(dest_dir, "hadith.jsonl")
    with open(path, "w", encoding="utf-8") as f:
        f.write("[]")
    print("hadith placeholder saved to", path)

if __name__ == "__main__":
    download_hadith()
