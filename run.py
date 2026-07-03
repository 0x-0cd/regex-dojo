"""
运行入口 · 从项目根目录跑测试

用法:
    python run.py          # 跑所有阶段
    python run.py 1        # 跑阶段 1
    python run.py 1 3 5    # 跑指定阶段
"""

import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中（运行本文件时自动就是）
PROJECT_ROOT = Path(__file__).parent

PHASES = {
    1: "practices.phase_01_basics",
    2: "practices.phase_02_quantifiers",
    3: "practices.phase_03_groups",
    4: "practices.phase_04_lookaround",
    5: "practices.phase_05_re_api",
    # 6: "practices.phase_06_advanced",
    # 7: "practices.phase_07_final_challenge",
}


def run_phase(phase_num: int) -> bool:
    """运行指定阶段，返回是否全部通过"""
    import importlib

    if phase_num not in PHASES:
        print(f"❌ 阶段 {phase_num} 不存在")
        return False
    module = importlib.import_module(PHASES[phase_num])
    print(f"\n{'=' * 60}")
    print(f"  🥋 阶段 {phase_num}")
    print(f"{'=' * 60}")
    return module.run_all()


def main():
    phases = (
        [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else sorted(PHASES.keys())
    )

    results = {}
    for p in phases:
        results[p] = run_phase(p)

    print(f"\n{'=' * 60}")
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    print(f"  结果: {passed}/{total} 阶段通过")
    if passed == total:
        print("  🎉 全部通关！")
    else:
        failed = [k for k, v in results.items() if not v]
        print(f"  ⚠️  未通过阶段: {failed}")
    print(f"{'=' * 60}")

    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
