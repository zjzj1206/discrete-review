"""Regenerate the knowledge map from the actual theory chapters before building."""
from pathlib import Path
import re

def build_index(root):
    content=root/'content'
    header='''# 24 · 完整知识目录与学习路线

本页列出 19 个理论章节的实际知识条目。按章节学习时从上往下读；查概念时可用页面搜索。每个链接直接定位并展开原条目，证明仍可独立选择是否展开。

## 总体依赖框架

集合与映射 → 命题与一阶逻辑 → 自然数与公理基础；数论 → 群 → 群作用 → 环 → 域；组合计数 → 概率 → 熵与集中 → 编码、Markov、概率方法。图论以集合为对象基础，以计数、线性代数和概率为工具，优化匹配另设第 21 章。

## 按主题逐项查看
'''
    parts=[header]
    for p in sorted(content.glob('*.md')):
        if int(p.name[:2]) not in list(range(1,18))+[21,22]:continue
        text=p.read_text();parts.append('### '+text.splitlines()[0][2:]);counter=0
        for line in text.splitlines():
            if line.startswith('## ') and not line.startswith('## 本章回顾'):
                parts.append('**'+line[3:]+'**')
            elif line.startswith(':::') and line!=':::':
                counter+=1
                parts.append(f'- [{line[3:]}]({p.stem}.html#{p.stem}-item-{counter})')
    (content/'24-knowledge-map.md').write_text('\n\n'.join(parts)+'\n')

if __name__=='__main__':build_index(Path(__file__).resolve().parent)
