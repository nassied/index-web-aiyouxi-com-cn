from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class KeywordNote:
    keyword: str
    description: str
    url: str
    created_at: Optional[str] = None
    tags: Optional[List[str]] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.tags is None:
            self.tags = []

    def summary(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return f"[{self.keyword}] {self.description} | 标签: {tag_str} | 来源: {self.url} | 时间: {self.created_at}"


def format_notes(notes: List[KeywordNote], sort_by: str = "keyword") -> str:
    if sort_by == "keyword":
        sorted_notes = sorted(notes, key=lambda n: n.keyword)
    elif sort_by == "time":
        sorted_notes = sorted(notes, key=lambda n: n.created_at or "")
    else:
        sorted_notes = notes

    lines = ["关键词笔记列表", "=" * 40]
    for idx, note in enumerate(sorted_notes, 1):
        lines.append(f"\n--- 笔记 {idx} ---")
        lines.append(note.summary())
    return "\n".join(lines)


def create_sample_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword="爱游戏",
            description="这是一个专注于游戏资讯与娱乐的平台，提供最新游戏动态与评测。",
            url="https://index-web-aiyouxi.com.cn",
            tags=["游戏", "娱乐", "资讯"],
        ),
        KeywordNote(
            keyword="Python 编程",
            description="Python 是一种广泛使用的解释型高级编程语言，适合快速开发与数据科学。",
            url="https://www.python.org",
            tags=["编程", "教程"],
        ),
        KeywordNote(
            keyword="数据结构",
            description="学习常见数据结构的实现与应用，包括列表、字典、树、图等。",
            url="https://example.com/data-structures",
            tags=["计算机科学", "算法"],
        ),
    ]


if __name__ == "__main__":
    notes = create_sample_notes()
    print(format_notes(notes, sort_by="keyword"))
    print("\n按时间排序：")
    print(format_notes(notes, sort_by="time"))