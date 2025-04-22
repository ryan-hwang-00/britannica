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

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="단어 목록을 받아 Britannica 정의를 마크다운으로 출력합니다.")
    parser.add_argument("words", nargs="+", help="정의할 단어 목록 (예: test apple banana)")
    parser.add_argument("--output", "-o", type=str, help="출력할 마크다운 파일 경로 (예: result.md)")

    args = parser.parse_args()
    word_list = args.words

    markdown_doc = generate_page(word_list)
    print(markdown_doc)

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(markdown_doc)
            print(f"\n📁 파일 저장 완료: {args.output}")
        except Exception as e:
            print(f"\n❗ 파일 저장 실패: {e}")

    try:
        import pyperclip
        pyperclip.copy(markdown_doc)
        print("✅ 클립보드에 복사 완료!")
    except Exception:
        print("⚠️ 클립보드 복사 실패")
