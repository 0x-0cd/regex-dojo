# regex-dojo 🥋

> 系统学习 Python 正则表达式的练习道场。

## 结构

```
regex-dojo/
├── practices/         ← 分阶段练习 + 参考答案
│   ├── helpers.py     # 验证工具函数
│   ├── phase-01-basics.py
│   ├── phase-02-quantifiers.py
│   ├── phase-03-groups.py
│   ├── phase-04-lookaround.py
│   ├── phase-05-re-api.py
│   ├── phase-06-advanced.py
│   └── phase-07-final-challenge.py
├── playground.py      # 自由练习场
├── .gitignore
└── README.md
```

## 怎么用

1. 每阶段先看 `/practices/` 下的挑战文件
2. 在挑战文件里写你的 pattern
3. 直接跑文件验证：`python practices/phase-01-basics.py`
4. 想自由练习用 `playground.py`

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
