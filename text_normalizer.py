#!/usr/bin/env python3
"""text_normalizer —— 轻量文本规范化。

能力（全部可开关，默认开启）：
  - Unicode 兼容规范化 NFKC；
  - 全角/半角转换（全角字母数字标点 -> 半角）；
  - 空白折叠（连续空白 -> 单个空格）；
  - 首尾去空白；
  - 大小写统一（可选 lower / upper）。
仅依赖标准库 unicodedata / re。
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata


def to_halfwidth(text: str) -> str:
    out = []
    for ch in text:
        code = ord(ch)
        if 0xFF01 <= code <= 0xFF5E:
            out.append(chr(code - 0xFEE0))
        elif code == 0x3000:
            out.append(" ")
        else:
            out.append(ch)
    return "".join(out)


_WS = re.compile(r"\s+")


def normalize(text, *, nkfc=True, halfwidth=True, collapse_ws=True, case=None):
    if nkfc:
        text = unicodedata.normalize("NFKC", text)
    if halfwidth:
        text = to_halfwidth(text)
    if collapse_ws:
        text = _WS.sub(" ", text).strip()
    if case == "lower":
        text = text.lower()
    elif case == "upper":
        text = text.upper()
    return text


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="轻量文本规范化")
    p.add_argument("text", nargs="?", help="待规范化文本；不传则读标准输入")
    p.add_argument("--file", help="从文件读取")
    p.add_argument("--case", choices=["lower", "upper"], help="大小写统一")
    p.add_argument("--no-halfwidth", action="store_true", help="不做全角转半角")
    p.add_argument("--no-collapse", action="store_true", help="不折叠空白")
    args = p.parse_args(argv)
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = args.text if args.text is not None else sys.stdin.read()
    out = normalize(text, halfwidth=not args.no_halfwidth, collapse_ws=not args.no_collapse, case=args.case)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
