# generate_markdown_page.py

from britannica_single import lookup_britannica
import pyperclip

def generate_page(words):
    blocks = [lookup_britannica(word) for word in words]
    return "\n\n".join(blocks)

if __name__ == "__main__":
    word_list = ["test", "apple", "banana"]

    markdown_doc = generate_page(word_list)
    print(markdown_doc)

    try:
        pyperclip.copy(markdown_doc)
        print("\n✅ 클립보드에 복사 완료!")
    except Exception:
        print("\n⚠️ 클립보드 복사 실패")

