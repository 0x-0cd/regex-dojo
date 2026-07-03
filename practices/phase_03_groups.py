"""
阶段 3：分组捕获
===============
捕获组 · 命名组 · 非捕获组 · 反向引用

运行方式（从项目根目录）：
    python run.py 3
"""

import re
from practices.helpers import test


# ── C1: 捕获组 ────────────────────────────────────────


def c1_challenge_1():
    """捕获组：匹配 'abc123' 这样的字母+数字组合，分别捕获字母和数字部分"""
    pattern = r"([a-z]+)(\d+)|(\d+)([a-z]+)"  # ← 你的模式（比如 r"([a-z]+)(\d+)"）
    return test(
        pattern,
        [
            ("字母+数字", "abc123", True),
            ("纯字母", "abcdef", False),  # 没有数字不行
            ("纯数字", "123456", False),  # 没有字母不行
            ("数字+字母", "123abc", True),  # 也是字母+数字的序列
        ],
    )


def c1_challenge_2():
    """捕获组序号：匹配重复的单词，如 'the the'、'is is'"""
    # 提示：(\w+) \1 可以匹配重复单词
    pattern = r"(\w+) \1"  # ← 你的模式
    return test(
        pattern,
        [
            ("重复the", "the the", True),
            ("重复is", "is is", True),
            ("不同词", "the is", False),  # 不是重复
            ("重复但带标点", "the, the", False),  # 被逗号隔开了
            ("单次", "the", False),
        ],
    )


def c1_challenge_3():
    """提取日期格式：匹配 YYYY-MM-DD 并分别捕获年、月、日"""
    pattern = r"(\d{4})-(\d{1,2})-(\d{1,2})"  # ← 你的模式（用三组括号分别捕获）
    return test(
        pattern,
        [
            ("标准日期", "2026-07-03", True),
            ("单月/日", "2026-1-5", True),
            ("月份太大", "2026-13-01", True),  # 格式正确即可，不校验数值
            ("无分隔符", "20260703", False),
            ("格式不对", "03-07-2026", False),  # 顺序不对
        ],
    )


# ── C2: 命名组 ────────────────────────────────────────


def c2_challenge_1():
    """命名组：用 (?P<name>...) 给组起名字，匹配邮箱 user@domain"""
    pattern = r"^(?P<name>[^@]+)@(?P<domain>[^@]+\.[^@]+)$"  # 提示：r"(?P<user>.+)@(?P<domain>.+)"
    return test(
        pattern,
        [
            ("简单邮箱", "alice@example.com", True),
            ("带点", "john.doe@company.org", True),
            ("无@", "bademail", False),
            ("多@", "a@b@c.com", False),
        ],
    )


# ── C3: 非捕获组 ──────────────────────────────────────


def c3_challenge_1():
    """非捕获组：匹配 'cat' 或 'dog' 后面跟 'food'，不捕获前面的动物名"""
    pattern = r"^(?:cat|dog)food$"  # 提示：用 (?:...) 而不是 (...)
    return test(
        pattern,
        [
            ("猫粮", "catfood", True),
            ("狗粮", "dogfood", True),
            ("其他", "birdfood", False),
            ("分开", "cat food", False),  # 没连在一起
        ],
    )


# ── C4: 反向引用 ──────────────────────────────────────


def c4_challenge_1():
    """反向引用：匹配 HTML 标签对，如 <p>...</p>、<h1>...</h1>"""
    pattern = r"<(\w+)>.*?</\1>"  # 提示：r"<(\w+)>.*?</\1>"
    return test(
        pattern,
        [
            ("段落", "<p>text</p>", True),
            ("标题", "<h1>title</h1>", True),
            ("不匹配", "<p>text</h1>", False),  # 标签名不一致
            ("嵌套不处理", "<div><p>ok</p></div>", True),  # 只匹配外层
        ],
    )


def c4_challenge_2():
    """命名反向引用：用 (?P=name) 匹配成对标签（命名版）"""
    pattern = r"<(?P<tag>\w+)>.*?</(?P=tag)>"  # 提示：命名组 (?P<tag>...) 配合 (?P=tag)
    return test(
        pattern,
        [
            ("段落", "<p>text</p>", True),
            ("不匹配", "<p>text</h1>", False),
        ],
    )


# ── 混合 ─────────────────────────────────────────────


def c_mixed_1():
    """综合：提取 Markdown 标题（# 到 ##），分别捕获级别和标题内容"""
    lines = [
        "# 一级标题",
        "## 二级标题",
        "### 三级标题",
        "普通文本",
    ]
    text = "\n".join(lines)
    pattern = r""  # 提示：捕获 # 的个数和后面的标题文本
    return test(
        pattern,
        [
            ("多行标题", text, True),
        ],
    )


# ── 汇总 ─────────────────────────────────────────────

ALL_CHALLENGES = [
    c1_challenge_1,
    c1_challenge_2,
    c1_challenge_3,
    c2_challenge_1,
    c3_challenge_1,
    c4_challenge_1,
    c4_challenge_2,
    c_mixed_1,
]


def run_all() -> bool:
    """运行阶段 3 所有挑战，返回是否全部通过"""
    results = [fn() for fn in ALL_CHALLENGES]
    all_pass = all(results)
    print(f"\n{'=' * 50}")
    if all_pass:
        print("🏁 阶段 3 全部通过！")
    else:
        print("⚠️  阶段 3 有未通过的题目")
    print(f"{'=' * 50}")
    return all_pass


if __name__ == "__main__":
    run_all()
