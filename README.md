# text-normalizer-lite

轻量**文本规范化**工具：全角/半角转换、空白折叠、大小写统一、Unicode NFKC 兼容规范化。
纯标准库，零依赖，CLI 可直接处理文本或文件。

## 功能简介

- **Unicode NFKC** 兼容规范化（`①`→`1` 等）；
- **全角→半角**：全角字母数字标点 `ＡＢＣ！` → `ABC!`，全角空格→半角空格；
- **空白折叠**：连续空白（含制表/换行）→ 单个空格并 strip；
- **大小写统一**：可选 `--case lower|upper`。

## 快速开始

环境：Python 3.10+，零依赖。

```bash
python3 text_normalizer.py "Ｈｅｌｌｏ　世界！！  你好  " --case lower
```

处理文件：

```bash
python3 text_normalizer.py --file messy.txt --case lower
```

作为库：

```python
from text_normalizer import normalize
normalize("价格：１００元！！  打折中")
```

## 使用示例（真实命令）

```bash
$ python3 text_normalizer.py "Ｈｅｌｌｏ　世界！！  你好  " --case lower
hello 世界!! 你好
```

## 无 API key 如何运行

纯本地字符串处理，**不需要任何 API key**，不联网。

## 目录结构

```
text-normalizer-lite/
├── text_normalizer.py            # 规范化函数 + CLI
├── tests/
│   └── test_text_normalizer.py   # unittest
├── README.md
├── LICENSE
└── .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 许可证

[MIT](./LICENSE) © 2026 ljiang9
