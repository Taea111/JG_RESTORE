"""자료/*/README.md 의 제목·한 줄 설명을 읽어 루트 README.md 목록을 다시 쓴다."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- 목록 시작 -->", "<!-- 목록 끝 -->"


def read_item(folder: Path):
    text = (folder / "README.md").read_text(encoding="utf-8")
    title = re.search(r"^#\s+(.+)$", text, re.M)
    summary = re.search(r"^>\s+(.+)$", text, re.M)
    date = re.search(r"올린 날짜:\s*(\S+)", text)
    return (
        title.group(1).strip() if title else folder.name,
        summary.group(1).strip() if summary else "",
        date.group(1) if date else "",
    )


def main():
    rows = []
    for folder in sorted((ROOT / "자료").glob("*/")):
        if not (folder / "README.md").exists():
            continue
        title, summary, date = read_item(folder)
        link = f"자료/{folder.name}".replace(" ", "%20")
        manuals = sorted(p.name for p in folder.iterdir() if "설명서" in p.name)
        manual = f"[설명서]({link}/{manuals[0].replace(' ', '%20')})" if manuals else "-"
        rows.append(f"| [{title}]({link}) | {summary} | {manual} | {date} |")

    if rows:
        table = "| 항목 | 설명 | 설명서 | 올린 날짜 |\n|---|---|---|---|\n" + "\n".join(rows)
    else:
        table = "_아직 올린 항목이 없습니다._"

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _: f"{START}\n{table}\n{END}",
        text,
        flags=re.S,
    )
    readme.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
