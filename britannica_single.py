# britannica_single.py

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
import re
import sys
import pyperclip

def cleanup_linebreaks(text: str) -> str:
    patterns_to_remove = [
        r'\[\+\] more examples',
        r'\[\-\] hide examples',
        r'\[\+\] Example sentences',
        r'\[\-\] Hide examples'
    ]
    for pattern in patterns_to_remove:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    lines = text.splitlines()
    clean_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join(clean_lines)

def lookup_britannica(word: str) -> str:
    url = f"https://www.britannica.com/dictionary/{word}"
    res = requests.get(url)
    if res.status_code != 200:
        return f"{word}\n?\n❗ 페이지를 불러올 수 없습니다."

    soup = BeautifulSoup(res.text, "html.parser")
    section = soup.find(id="ld_entries_v2_all")
    if not section:
        return f"{word}\n?\n❗ 정의를 찾을 수 없습니다."

    markdown = markdownify(str(section), heading_style="atx")
    cleaned = cleanup_linebreaks(markdown)
    return f"# {word}\n?\n{cleaned}"

# ✅ 단독 실행 시 단어 인자를 받아 처리
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ 사용법: python britannica_single.py [단어]")
        sys.exit(1)

    word = sys.argv[1]
    result = lookup_britannica(word)
    print(result)

    try:
        pyperclip.copy(result)
        print("\n✅ 클립보드에 복사 완료!")
    except Exception:
        print("\n⚠️ 클립보드 복사 실패")

