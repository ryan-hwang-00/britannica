import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import pyperclip
import sys

def cleanup_linebreaks(text: str) -> str:
    lines = text.splitlines()
    clean_lines = [line.strip() for line in lines if line.strip()]
    return "\n".join(clean_lines)

def lookup(word: str) -> str:
    url = f"https://www.britannica.com/dictionary/{word}"
    res = requests.get(url)
    if res.status_code != 200:
        return "❗ 페이지를 불러올 수 없습니다."

    soup = BeautifulSoup(res.text, "html.parser")
    section = soup.find(id="ld_entries_v2_all")
    if not section:
        return "❗ 정의를 찾을 수 없습니다."

    # 1. HTML → Markdown
    markdown = md(str(section), heading_style="atx")

    # 2. 불필요한 줄 제거
    cleaned = cleanup_linebreaks(markdown)
    return cleaned

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("🔍 사용법: python britannica_cli.py [단어]")
        sys.exit(1)

    word = sys.argv[1]
    result = lookup(word)
    output = f"# {word}\n?\n{result}"

    print(output)

    try:
        pyperclip.copy(output)
        print("\n✅ 복사됨! 클립보드에 저장되었습니다.")
    except Exception:
        print("\n⚠️ 클립보드 복사 실패 (환경에 따라 pyperclip 제한 가능)")

