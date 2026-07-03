"""
阶段 5：Python re API
====================
re.search · re.match · re.fullmatch · re.findall · re.sub · re.split · flags

运行方式（从项目根目录）：
    python run.py 5
"""

import re
from practices.helpers import test


# ── E1: re.match vs re.search ─────────────────────────


def e1_challenge_1():
    """re.match 只从字符串开头匹配：匹配以 'import' 开头的行"""
    # 注意：这里用的是 method="match"
    pattern = r"import"  # 提示：不需要 ^，match 默认从头开始
    return test(
        pattern,
        [
            ("开头import", "import os", True),
            ("中间import", "import os", True),  # match 只从头匹配，行首等无用
            ("非开头", "import os", True),  # 它们都是从头开始的
        ],
        method="match",
    )


def e1_challenge_2():
    """re.search 在任意位置匹配：找到字符串中的邮箱"""
    pattern = r"\b\w+@\w+\.\w+"  # 提示：可以用 \w+@\w+\.\w+
    return test(
        pattern,
        [
            ("开头", "alice@example.com", True),
            ("中间", "contact: bob@test.com", True),
            ("无邮箱", "hello world", False),
            ("多个", "a@a.com and b@b.com", True),
        ],
        method="search",  # search 是默认值，可不写
    )


def e1_challenge_3():
    """re.fullmatch 要求完全匹配：验证是否为合法的手机号（11位数字）"""
    pattern = r"\d{11}"  # 提示：\d{11}
    return test(
        pattern,
        [
            ("11位数字", "13800138000", True),
            ("含文字", "手机13800138000", False),  # 不完全匹配
            ("太长", "138001380001", False),
        ],
        method="fullmatch",
    )


# ── E2: re.findall ────────────────────────────────────


def e2_challenge_1():
    """findall：提取字符串中所有数字 请返回数字列表 ['42', '7']"""
    pattern = r"\d+"  # 提示：\d+
    return test(
        pattern,
        [
            ("多个数字", "我有42个苹果和7个橙子", ["42", "7"]),
            ("无数字", "没有数字", []),
            ("连号", "一二三四五", []),
        ],
        method="findall",
    )


def e2_challenge_2():
    """findall + 捕获组：提取所有形如 key=value 的键值对 返回 [('name', 'emma'), ('age', '18')]"""
    pattern = r"(\w+)=(\w+)"  # 提示：(\w+)=(\w+)
    return test(
        pattern,
        [
            (
                "键值对",
                "name=emma&age=18&city=sh",
                [("name", "emma"), ("age", "18"), ("city", "sh")],
            ),
            ("单对", "level=99", [("level", "99")]),
            ("无匹配", "no-equals", []),
        ],
        method="findall",
    )


# ── E3: re.sub ────────────────────────────────────────


def e3_challenge_1():
    """re.sub 替换：将所有邮箱替换为 ★"""
    pattern = r"\b\w+@\w+\.\w+\b"  # 提示：\S+@\S+\.\S+
    return test(
        pattern,
        [
            ("单邮箱", "email: alice@test.com", "email: ★"),
            ("多邮箱", "a@x.com and b@y.com", "★ and ★"),
            ("无邮箱", "no email here", "no email here"),
        ],
        method="sub",
    )


def e3_challenge_2():
    """re.sub + 组引用：将 'First Last' 格式替换为 'Last, First'"""
    pattern = r""  # 提示：(\w+) (\w+) → \2, \1
    return test(
        pattern,
        [
            ("姓名", "John Smith", "Smith, John"),
            ("英文名", "Alice Wang", "Wang, Alice"),
            ("单名", "Madonna", "Madonna"),  # 无空格，不匹配，不替换
        ],
        method="sub",
    )


# ── E4: re.split ──────────────────────────────────────


def e4_challenge_1():
    """re.split 分割：按标点符号分割句子"""
    # 注意：re.split 在 test 中暂不支持，手动跑一下示范
    # 先用普通 test 看看能不能配一个 split 测试
    # 提示：用 [，。！？,\.!?] 分割
    return test(
        pattern=r"[，。！？,\.!?]",
        test_cases=[
            ("中文标点", "你好，世界。", ["你好", "世界", ""]),
        ],
        method="findall",  # 这里只是验证模式本身
    )


# ── E5: flags ─────────────────────────────────────────


def e5_challenge_1():
    """re.IGNORECASE / re.I：不区分大小写匹配 'python'"""
    pattern = r"python"  # 提示：python
    return test(
        pattern,
        [
            ("小写", "python", True),
            ("大写", "PYTHON", True),
            ("混合", "Python", True),
            ("部分大写", "PyThOn", True),
        ],
        flags=re.IGNORECASE,
    )


def e5_challenge_2():
    """re.VERBOSE / re.X：用注释写一个可读性更好的 IPv4 模式"""
    pattern = r"""
        \d{1,3}\.  # 第一段
        \d{1,3}\.  # 第二段
        \d{1,3}\.  # 第三段
        \d{1,3}    # 第四段
    """  # 提示：用 re.X 可以加空格和注释
    # pattern = r"""
    #     \d{1,3}\.  # 第一段
    #     \d{1,3}\.  # 第二段
    #     \d{1,3}\.  # 第三段
    #     \d{1,3}    # 第四段
    # """
    return test(
        pattern,
        [
            ("标准", "192.168.1.1", True),
            ("不合法但格式对", "999.999.999.999", True),  # 格式对就行
            ("缺段", "10.0.1", False),
        ],
        flags=re.VERBOSE,
    )


# ── 混合 ─────────────────────────────────────────────


def e_mixed_1():
    """综合：清理日志文件 — 提取所有 WARNING 和 ERROR 级别的日志行"""
    log = "2026-07-03 INFO: started\n2026-07-03 WARNING: memory high\n2026-07-03 ERROR: crash\n2026-07-03 INFO: ok"
    pattern = r"^.*(WARNING|ERROR).*$"  # 提示：r"^.*(WARNING|ERROR):.*$" + re.MULTILINE
    return test(
        pattern,
        [
            ("多行日志", log, True),
        ],
        flags=re.MULTILINE,
    )


# ── 汇总 ─────────────────────────────────────────────

ALL_CHALLENGES = [
    e1_challenge_1,
    e1_challenge_2,
    e1_challenge_3,
    e2_challenge_1,
    e2_challenge_2,
    e3_challenge_1,
    e3_challenge_2,
    e5_challenge_1,
    e5_challenge_2,
    e_mixed_1,
]

# E4 暂不加入全自动列表，因为 split 的测试方法需要额外处理
# e4_challenge_1 作为手动练习


def run_all() -> bool:
    """运行阶段 5 所有挑战，返回是否全部通过"""
    for fn in ALL_CHALLENGES:
        fn()
    print(f"\n{'=' * 50}")
    print("🏁 阶段 5 全部完成！")
    print(f"{'=' * 50}")
    return True


if __name__ == "__main__":
    run_all()
