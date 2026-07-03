"""
阶段 4：环视
==========
前瞻 · 后顾 · 肯定 · 否定

运行方式（从项目根目录）：
    python run.py 4
"""

import re
from practices.helpers import test


# ── D1: 肯定前瞻 (?=...) ─────────────────────────────


def d1_challenge_1():
    """肯定前瞻：匹配一个数字后面跟着 'px' 的部分（只匹配数字，不含px）"""
    pattern = r"\d+(?=px)"  # 提示：r"\d+(?=px)"
    return test(
        pattern,
        [
            ("有px", "16px", True),
            ("无px", "16em", False),  # 后面不是 px
            ("纯数字", "123", False),
            ("句子中", "font-size: 14px", True),
        ],
    )


def d1_challenge_2():
    """肯定前瞻：匹配 'foo' 后面跟着 'bar' 的 'foo'"""
    pattern = r"foo(?=bar)"  # 提示：r"foo(?=bar)"
    return test(
        pattern,
        [
            ("foobar", "foobar", True),
            ("foo后跟其他", "foobaz", False),
            ("单独foo", "foo", False),
        ],
    )


# ── D2: 否定前瞻 (?!...) ─────────────────────────────


def d2_challenge_1():
    """否定前瞻：匹配一个数字后面不跟着 '%' 的数字"""
    pattern = r"\d+(?!%)"  # 提示：r"\d+(?!%)"
    return test(
        pattern,
        [
            ("无百分号", "42", True),
            ("有百分号", "42%", False),  # 后面有 % 不匹配
            ("混合", "50% off", True),  # 50 后面有 %，但 off 前面的 0 后面没有 %
        ],
    )


def d2_challenge_2():
    """否定前瞻：匹配不以 'Th' 开头的单词"""
    pattern = r"\b(?!Th)\w+\b"  # 提示：r"\b(?!Th)\w+\b"
    return test(
        pattern,
        [
            ("This", "This", False),  # 以 Th 开头，排除
            ("That", "That", False),
            ("The", "The", False),
            ("Other", "Other", True),  # 不以 Th 开头
            ("word", "word", True),
        ],
    )


# ── D3: 肯定后顾 (?<=...) ────────────────────────────


def d3_challenge_1():
    """肯定后顾：匹配 '$' 符号后面的价格数字"""
    pattern = r"(?<=\$)\d+"  # 提示：r"(?<=\$)\d+"
    return test(
        pattern,
        [
            ("美元价格", "$19.99", True),  # 匹配 19
            ("人民币", "¥50", False),  # 前面不是 $
            ("无符号", "100", False),
        ],
    )


def d3_challenge_2():
    """肯定后顾：匹配 '@' 后面的用户名"""
    pattern = r"(?<=@)\w+"  # 提示：r"(?<=@)\w+"
    return test(
        pattern,
        [
            ("艾特", "@emma", True),
            ("邮箱部分", "hello@world", True),  # @ 后面是 world
            ("无艾特", "emma", False),
        ],
    )


# ── D4: 否定后顾 (?<!...) ────────────────────────────


def d4_challenge_1():
    """否定后顾：匹配前面没有 '-' 的数字"""
    pattern = r"(?<!-)\d+"  # 提示：r"(?<!-)\d+"
    return test(
        pattern,
        [
            ("正数", "42", True),
            ("负数", "-42", False),  # 前面有 -
            ("正中间有负", "5-10", True),  # 5 前面无负号，匹配；10 前面有，不匹配
        ],
    )


# ── 混合 ─────────────────────────────────────────────


def d_mixed_1():
    """综合：提取价格数字（支持 $ 符号前缀，排除负数和百分数）"""
    pattern = r"^\$(?<!-)\d+(?!%)$"  # 提示：结合 (?<=\$) 和 (?!%)
    return test(
        pattern,
        [
            ("美元价格", "$99", True),
            ("负数", "-99", False),
            ("百分数", "99%", False),
            ("无符号", "99", False),  # 没有 $ 符号
        ],
    )


def d_mixed_2():
    """综合：匹配密码中长度至少8位且包含至少一个数字的单词"""
    text = "password passw123 abcdefgh noDigitsHere 12345678"
    pattern = r"\b(?=\w*\d)\w{8,}\b"  # 提示：用 (?=...)
    return test(
        pattern,
        [
            ("混合密码", text, True),  # 应匹配 passw123
        ],
    )


# ── 汇总 ─────────────────────────────────────────────

ALL_CHALLENGES = [
    d1_challenge_1,
    d1_challenge_2,
    d2_challenge_1,
    d2_challenge_2,
    d3_challenge_1,
    d3_challenge_2,
    d4_challenge_1,
    d_mixed_1,
    d_mixed_2,
]


def run_all() -> bool:
    """运行阶段 4 所有挑战，返回是否全部通过"""
    results = [fn() for fn in ALL_CHALLENGES]
    all_pass = all(results)
    print(f"\n{'=' * 50}")
    if all_pass:
        print("🏁 阶段 4 全部通过！")
    else:
        print("⚠️  阶段 4 有未通过的题目")
    print(f"{'=' * 50}")
    return all_pass


if __name__ == "__main__":
    run_all()
