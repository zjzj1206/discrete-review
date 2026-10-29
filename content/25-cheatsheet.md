# 期中 Cheat Sheet · 四面 A4

**两张纸，双面共四面。** 范围从集合到计数（含），对应本站第 01–09 章。更新于 2026-10-29。

## 下载与打印

- [打开或下载四面版 PDF](downloads/discrete-midterm-cheatsheet.pdf)
- [下载可编辑源码包（含 PDF、Typst 源码、构建脚本与详细说明）](downloads/discrete-cheatsheet-editable.zip)

打印选择：**全部 4 页、A4 横向、实际大小 100%、双面短边翻转**，共两张纸。每面已经排成三栏，请勿再开启“每张多页”。正文和公式为 7.5pt，高公式保留上下间距。

## 四面的内容

|面|内容|
|---|---|
|1|集合、关系、无穷与序数；命题和一阶逻辑；PA、ZFC、模型与元定理|
|2|整除、同余、CRT、模幂；群、商群和结构；群作用、类方程与 Sylow|
|3|环、理想和不可约判定；域扩张、有限域与 Galois；代数计算和旧期中题型|
|4|计数模型、容斥、Stirling 数；生成函数与反演；Burnside、Pólya 和着色例题|

内容包括定义、定理条件、公式、短证明、计算模板与反例。它用于考试速查；需要完整长证明时，回到本站相应章节阅读。

## 自己修改与重新构建

解压源码包后，内容位于 `cheatsheet/sections/`，每个 `.typ` 文件对应一栏。排版参数位于 `cheatsheet/main.typ`，完整修改说明见 `cheatsheet/README.md`。

在解压目录运行：

```bash
bash cheatsheet/build.sh
```

第一次需要联网，脚本会建立独立 Python 环境并安装固定版本依赖；之后可离线构建。需要 Python 3.10+、venv 和中文字体。本版使用 Noto Serif CJK SC 与 Noto Sans CJK SC，换字体后请重新检查排版。

输出为 `output/pdf/discrete-midterm-cheatsheet.pdf`。构建会检查已知公式语法风险、各栏高度、A4 纸张和总页数必须为 4；失败时保留原 PDF。

Windows 用户可在解压目录运行：

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r cheatsheet\requirements.txt
.venv\Scripts\python cheatsheet\build.py
```

## 复习时配合使用

- [从集合与无穷开始](01-sets.html)
- [计数与生成函数](09-counting.html)
- [完整知识目录](24-knowledge-map.html)
- [官方作业与试卷索引](20-exercise-index.html)
