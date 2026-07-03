"""
阶段 2：量词与定位
===================
量词 * + ? {n,m} · 贪婪 vs 懒惰 · 锚点 · 单词边界

运行方式（从项目根目录）：
    python run.py 2
"""

import re

from practices.helpers import test


# ── B1: 量词 * + ? {n,m} ────────────────────────────


def b1_challenge_1():
    """'*' 表示 0 次或多次：匹配一个 'a' 后面跟任意数量 'b'"""
    pattern = r"^ab*$"  # ← 你的模式（ab*）
    return test(
        pattern,
        [
            ("0个b", "a", True),
            ("3个b", "abbb", True),
            ("多个b", "abbbbb", True),
            ("ab交替", "ababa", False),  # 模式要求 a 后面不能穿插 a
            ("无a", "bbb", False),  # 没有开头的 a
        ],
    )


def b1_challenge_2():
    """'+' 表示 1 次或多次：匹配至少一个数字的连续序列"""
    pattern = r"\d+"  # ← 你的模式
    return test(
        pattern,
        [
            ("单个数字", "7", True),
            ("多位数", "12345", True),
            ("字母开头", "abc", False),
            ("数字+字母", "42abc", True),  # 前两个字符匹配
            ("空字符串", "", False),
        ],
    )


def b1_challenge_3():
    """'?' 表示 0 次或 1 次：匹配 'color' 或 'colour'（英式u可选）"""
    pattern = r"colou?r"  # ← 你的模式
    return test(
        pattern,
        [
            ("美式", "color", True),
            ("英式", "colour", True),
            ("多u", "colouur", False),
            ("缺字母", "colr", False),
        ],
    )


def b1_challenge_4():
    """'{n,m}' 精确数量：匹配恰好 3 个或 4 个字母 'X'"""
    pattern = r"^X{3,4}$"  # ← 你的模式
    return test(
        pattern,
        [
            ("3个X", "XXX", True),
            ("4个X", "XXXX", True),
            ("2个X", "XX", False),
            ("5个X", "XXXXX", False),
            ("0个X", "", False),
        ],
    )


# ── B2: 贪婪 vs 懒惰 ─────────────────────────────────


def b2_challenge_1():
    """
    贪婪匹配：用 .* 匹配 <div>content</div><div>text</div> 中的内容
    看看 .* 会吞掉多少
    """
    pattern = r"<div>.*</div>"  # ← 试试 r"<div>.*</div>"
    return test(
        pattern,
        [
            ("单个标签", "<div>hello</div>", True),
            (
                "两个标签",
                "<div>hello</div><div>text</div>",
                True,
            ),  # 贪婪匹配会吞到最后一个 </div> 吗？
        ],
    )


def b2_challenge_2():
    """
    懒惰匹配：用 .*? 做同样的事
    预期 .*? 会停在第一个 </div> 就收手
    """
    pattern = r"<div>.*?</div>"  # ← 试试 r"<div>.*?</div>"
    return test(
        pattern,
        [
            ("单个标签", "<div>hello</div>", True),
            (
                "两个标签",
                "<div>hello</div><div>text</div>",
                True,
            ),  # 懒惰只会匹配到第一个 </div>
        ],
    )


def b2_challenge_3():
    """验证懒惰匹配：匹配双引号字符串（避免跨引号吞噬）"""
    pattern = r"“.*?”"  # ← 试试 r"“.*?”"
    return test(
        pattern,
        [
            ("单段", "他说“你好”", True),
            ("两段", "他说“你好”然后“再见”", True),  # 懒惰应只匹配“你好”
        ],
    )


# ── B3: 锚点 ^ $ ────────────────────────────────────


def b3_challenge_1():
    """'^' 行首：匹配以 'Error:' 开头的行"""
    pattern = r"^Error:.*"  # ← 你的模式
    return test(
        pattern,
        [
            ("开头", "Error: timeout", True),
            ("不在行首", "Got Error: timeout", False),
            ("空行前", "Error:", True),
        ],
    )


def b3_challenge_2():
    """'$' 行尾：匹配以 '.py' 结尾的字符串"""
    pattern = r".*\.py$"  # ← 你的模式
    return test(
        pattern,
        [
            ("py结尾", "main.py", True),
            ("多后缀", "script.py.bak", False),
            ("no点", "pymain", False),
            ("完整路径", "/usr/bin/run.py", True),
        ],
    )


def b3_challenge_3():
    """多行模式 re.M：在一段多行文本中匹配以 'def' 开头的行（可能有缩进）"""
    text = "class Foo:\n    def bar(self):\n    def baz(self):\nclass Qux:\n    pass"
    # 提示：需要 flags=re.MULTILINE，且 def 前可能有空格
    pattern = r"^\s*def.*"  # ← 你的模式
    return test(
        pattern,
        [
            ("多行def", text, True),  # 应匹配到 def bar 和 def baz
        ],
        flags=re.MULTILINE,  # ← 可能需要改成 re.M
    )


# ── B4: 单词边界 \b \B ──────────────────────────────


def b4_challenge_1():
    """'\b' 单词边界：匹配独立的单词 'cat'，不匹配 'category' 中的部分"""
    pattern = r"cat\b"  # ← 你的模式
    return test(
        pattern,
        [
            ("独立", "a cat sat", True),
            ("作为词缀", "category", False),
            ("开头", "catapult", False),  # cat 在词首？\b 会匹配吗？试试
            ("结尾", "wildcat", True),  # cat 在词尾
        ],
    )


def b4_challenge_2():
    """'\B' 非单词边界：匹配作为其他单词一部分的 'cat'"""
    pattern = r"cat\B"  # ← 你的模式
    return test(
        pattern,
        [
            ("词中", "category", True),
            ("结尾", "wildcat", False),  # cat 在词边界上
            ("独立", "a cat sat", False),
            ("词首", "catapult", True),  # cat 在词首？\B 不匹配边界
        ],
    )


# ── 混合 ─────────────────────────────────────────────


def b_mixed_1():
    """综合：匹配一个合法的 IPv4 地址（0~255，四段）"""
    # 提示：^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$
    # 这是个简化版，没有严格校验 0-255 范围
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"  # ← 你的模式
    return test(
        pattern,
        [
            ("标准", "192.168.1.1", True),
            ("localhost", "127.0.0.1", True),
            ("五段", "1.2.3.4.5", False),
            ("缺段", "10.0.1", False),
            ("空段", "10..0.1", False),
        ],
    )


# ── 汇总 ─────────────────────────────────────────────

ALL_CHALLENGES = [
    b1_challenge_1,
    b1_challenge_2,
    b1_challenge_3,
    b1_challenge_4,
    b2_challenge_1,
    b2_challenge_2,
    b2_challenge_3,
    b3_challenge_1,
    b3_challenge_2,
    b3_challenge_3,
    b4_challenge_1,
    b4_challenge_2,
    b_mixed_1,
]


def run_all() -> bool:
    """运行阶段 2 所有挑战，返回是否全部通过"""
    for fn in ALL_CHALLENGES:
        fn()
    print(f"\n{'=' * 50}")
    print("🏁 阶段 2 全部完成！")
    print(f"{'=' * 50}")
    return True


if __name__ == "__main__":
    run_all()
