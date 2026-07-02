"""验证工具函数 —— 每个练习都引用这个模块"""

import re


def test(pattern, test_cases, flags=0, method="search"):
    """
    批量验证正则模式。

    test_cases: list of (描述, 待匹配字符串, 期望结果)
        期望结果 = True（应匹配）/ False（不应匹配）
        或者传字符串列表表示 findall 的期望结果
        或者传替换后的字符串表示 sub 的期望结果
    """
    print(f"\n  /{pattern}/")
    all_ok = True
    for desc, string, expected in test_cases:
        if method == "search":
            result = re.search(pattern, string, flags)
            ok = (result is not None) == bool(expected)
        elif method == "match":
            result = re.match(pattern, string, flags)
            ok = (result is not None) == bool(expected)
        elif method == "fullmatch":
            result = re.fullmatch(pattern, string, flags)
            ok = (result is not None) == bool(expected)
        elif method == "findall":
            result = re.findall(pattern, string, flags)
            ok = result == expected
        elif method == "sub":
            result = re.sub(pattern, "★", string, flags=flags)
            ok = result == expected
        else:
            raise ValueError(f"Unknown method: {method}")

        status = "✅" if ok else "❌"
        if not ok:
            all_ok = False
        print(f"  {status} [{desc:10}] '{string}' → {result}")

    if all_ok:
        print(f"  🎉 全部通过！")
    else:
        print(f"  ⚠️  有未通过项，再试试？")
    return all_ok


def test_one(pattern, string, expected=True, flags=0, method="search"):
    """单条验证快捷方式"""
    return test(pattern, [(string, string, expected)], flags, method)
