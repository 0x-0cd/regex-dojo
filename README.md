# regex-dojo 🥋

> 系统学习 Python 正则表达式的练习道场。

## 用法

```bash
# 跑所有阶段
python run.py

# 跑指定阶段
python run.py 1
python run.py 1 3       # 跑阶段 1 和 3
```

填好模式后直接验证，从根目录跑就行，不用折腾模块路径。

## 结构

```
regex-dojo/
├── run.py                     ← 入口：python run.py
├── playground.py              ← 自由练习场
├── practices/
│   ├── __init__.py
│   ├── helpers.py             # 验证工具
│   ├── phase_01_basics.py     # 阶段 1：基础匹配
│   ├── phase_02_quantifiers.py
│   ├── ...
│   └── phase_07_challenge.py
├── .gitignore
└── README.md
```

## 阶段

| # | 主题 | 子技能 |
|---|------|--------|
| 1 | 基础匹配 | 字面量、字符类、预定义类、通配符 |
| 2 | 量词与定位 | `* + ? {n,m}`、贪婪 vs懒惰、`^ $ \b` |
| 3 | 分组捕获 | 捕获组、命名组、非捕获组、反向引用 |
| 4 | 环视 | 前瞻后顾、肯定否定 |
| 5 | Python re API | search/match/findall/sub/split、flags |
| 6 | 进阶 | 原子组、回溯陷阱、真实场景 |
| 7 | 综合挑战 | 混合场景实战 |
