"""
阶段 1：基础匹配
=================
字面量 · 字符类 · 预定义类 · 通配符

运行方式（从项目根目录）：
    python run.py 1         ← 推荐
    python -m practices.phase_01_basics
"""

from practices.helpers import test


# ── A1: 字面量匹配 ──────────────────────────────────


def a1_challenge_1():
    """匹配字符串中的 'cat'"""
    pattern = r"^.*cat.*$"  # ← 你的模式写在这里
    return test(
        pattern,
        [
            ("包含 cat", "The cat sat", True),
            ("不包含", "The dog ran", False),
            ("单词部分", "category", True),
        ],
    )


def a1_challenge_2():
    """匹配 'hello world'（含中间空格）"""
    pattern = r"^.*hello world.*$"  # ← 你的模式
    return test(
        pattern,
        [
            ("标准问候", "hello world", True),
            ("没空格", "helloworld", False),
            ("首尾", "hello world!", True),
        ],
    )


# ── A2: 字符类 ──────────────────────────────────────


def a2_challenge_1():
    """匹配任意一个元音字母（a/e/i/o/u）"""
    pattern = r"^.*[aeiou].*$"  # ← 你的模式
    return test(
        pattern,
        [
            ("开头元音", "apple", True),
            ("中间元音", "sky", False),
            ("数字", "123", False),
            ("辅音开头", "Python", True),
        ],
    )


def a2_challenge_2():
    """匹配一个非数字字符"""
    pattern = r"^[^0-9]$"  # ← 你的模式
    return test(
        pattern,
        [
            ("字母", "A", True),
            ("数字", "5", False),
            ("符号", "@", True),
            ("空格", " ", True),
        ],
    )


def a2_challenge_3():
    """匹配小写字母 a 到 f 中的一个"""
    pattern = r"^[a-f].*$"  # ← 你的模式
    return test(
        pattern,
        [
            ("a", "apple", True),
            ("f", "fox", True),
            ("g", "golf", False),
            ("大写 A", "Apple", False),
        ],
    )


# ── A3: 预定义字符类 ─────────────────────────────────


def a3_challenge_1():
    """匹配一个数字字符"""
    pattern = r"^.*\d.*$"  # ← 你的模式
    return test(
        pattern,
        [
            ("数字", "version 2.0", True),
            ("字母", "hello", False),
            ("数字开头", "3 amigos", True),
        ],
    )


def a3_challenge_2():
    """匹配一个非空白字符"""
    pattern = r"^.*[\S].*$"  # ← 你的模式
    return test(
        pattern,
        [
            ("字母", "a b", True),
            ("空格", "  ", False),
            ("制表符", "\t", False),
            ("换行", "\n", False),
        ],
    )


def a3_challenge_3():
    """匹配一个单词字符（字母、数字、下划线）"""
    pattern = r"^[a-zA-Z0-9_]*$"  # ← 你的模式
    return test(
        pattern,
        [
            ("字母", "x", True),
            ("数字", "9", True),
            ("下划线", "_", True),
            ("空格", " ", False),
            ("符号", "@", False),
        ],
    )


# ── A4: 通配符与转义 ────────────────────────────────


def a4_challenge_1():
    """匹配任意一个字符（除换行）"""
    pattern = r"^.$"  # ← 你的模式
    return test(
        pattern,
        [
            ("字母", "a", True),
            ("数字", "7", True),
            ("符号", "?", True),
            ("换行", "\n", False),
            ("空字符串", "", False),
        ],
    )


def a4_challenge_2():
    """匹配一个真实的句点 '.'（不是通配符）"""
    pattern = r"^.*\..*$"  # ← 你的模式
    return test(
        pattern,
        [
            ("句点", "end.", True),
            ("字母", "end", False),
            ("数字", "3.14", True),
        ],
    )


def a4_challenge_3():
    """匹配 'www.example.com' 这个完整域名"""
    pattern = r"^.*www\.example\.com.*$"  # ← 你的模式
    return test(
        pattern,
        [
            ("完整域名", "www.example.com", True),
            ("少个点", "wwwexamplecom", False),
            ("前缀", "visit www.example.com now", True),
        ],
    )


# ── 汇总 ─────────────────────────────────────────────

ALL_CHALLENGES = [
    a1_challenge_1,
    a1_challenge_2,
    a2_challenge_1,
    a2_challenge_2,
    a2_challenge_3,
    a3_challenge_1,
    a3_challenge_2,
    a3_challenge_3,
    a4_challenge_1,
    a4_challenge_2,
    a4_challenge_3,
]


def run_all() -> bool:
    """运行阶段 1 所有挑战，返回是否全部通过"""
    results = [fn() for fn in ALL_CHALLENGES]
    all_pass = all(results)
    print(f"\n{'=' * 50}")
    if all_pass:
        print("🏁 阶段 1 全部通过！")
    else:
        print("⚠️  阶段 1 有未通过的题目")
    print(f"{'=' * 50}")
    return all_pass


if __name__ == "__main__":
    run_all()
