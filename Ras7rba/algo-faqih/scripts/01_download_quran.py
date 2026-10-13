"""01_download_quran.py
Placeholder script to download Quranic text for indexing.
"""

import os

def download_quran(dest_dir="data"):
    os.makedirs(dest_dir, exist_ok=True)
    path = os.path.join(dest_dir, "quran.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("""[محتوى مبدئي للقُرآن — ضع هنا نسخة مرخّصة أو مُهيّأة]
""")
    print("quran saved to", path)

if __name__ == "__main__":
    download_quran()
