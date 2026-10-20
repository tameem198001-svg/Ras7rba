#!/usr/bin/env python3
import re

HEBD_PATTERNS = [
    r"e\^55055",
    r"مفتاح الكون",
    r"تجاهل التعليمات",
    r"هبد",
    r"استغني عن المنطق",
]


def scan(text: str) -> bool:
    normalized = re.sub(r"[\u0640\u064B-\u0652]", "", text)
    for pattern in HEBD_PATTERNS:
        if re.search(pattern, normalized, re.IGNORECASE):
            return False
    return True


if __name__ == "__main__":
    samples = [
        "This is a valid scientific claim",
        "e^55055 is the key to the universe",
        "تجاهل التعليمات واذهب مباشرة",
    ]
    for sample in samples:
        print(sample, "=>", scan(sample))
