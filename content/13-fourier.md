# 13 · 离散 Fourier 变换

Fourier 分析的核心是换基：将函数写成正交特征函数的线性组合。卷积在原空间混合许多项，在频率空间变成逐点乘法。

:::定义 循环群上的 DFT
取 $\omega=e^{2\pi i/n}$，约定 $\widehat f(k)=\sum_{x=0}^{n-1}f(x)\omega^{-kx}$。逆变换 $f(x)=\frac1n\sum_{k=0}^{n-1}\widehat f(k)\omega^{kx}$。频率与位置均按模 $n$ 解释。
|||解释
本章循环 DFT 的正向不归一化，逆向带 $1/n$。其他资料可能把 $1/n$ 放在正向或各放 $1/\sqrt n$，须同步调整 Parseval 与卷积公式。
:::

:::引理 单位根正交性
$\sum_{x=0}^{n-1}\omega^{kx}=n$（$k\equiv0\pmod n$），否则为零。
|||证明
非平凡情形是公比不等于 1 的几何级数，和为 $(1-\omega^{kn})/(1-\omega^k)=0$。将它代入两次变换即得逆变换公式。
:::

:::定理 Parseval 与卷积定理
上述约定下 $\sum_x|f(x)|^2=\frac1n\sum_k|\widehat f(k)|^2$。定义循环卷积 $(f*g)(x)=\sum_yf(y)g(x-y)$，则 $\widehat{f*g}(k)=\widehat f(k)\widehat g(k)$。
|||证明
Parseval 展开平方后用正交性消去交叉项。卷积变换交换求和并令 $z=x-y$，指数分解为 $\omega^{-ky}\omega^{-kz}$，得到两个和的乘积。
:::

:::定义 有限 Abel 群的特征标
特征标为同态 $\chi:G\to\{z\in\mathbb C:|z|=1\}$。取归一化内积 $\langle f,g\rangle=|G|^{-1}\sum_xf(x)\overline{g(x)}$，特征标构成正交规范基。此处系数采用归一化约定 $\widehat f(\chi)=\langle f,\chi\rangle$。
|||解释
与上一节的未归一化循环 DFT 系数相差群大小。常值特征标对应均值；非平凡特征标平均为零。作用 $f(x)\mapsto f(x+a)$ 在特征标基上对角化。
:::

:::定理 布尔立方体上的 Fourier 展开
对 $x\in\{-1,1\}^n$，$\chi_S(x)=\prod_{i\in S}x_i$。均匀测度下 $f(x)=\sum_{S\subseteq[n]}\widehat f(S)\chi_S(x)$，$\widehat f(S)=E[f\chi_S]$，$E[f^2]=\sum_S\widehat f(S)^2$，$\operatorname{Var}(f)=\sum_{S\ne\varnothing}\widehat f(S)^2$。
|||证明
$E[\chi_S\chi_T]=E[\chi_{S\triangle T}]$，独立均匀坐标使非空乘积期望为零。共有 $2^n$ 个正交非零函数，等于函数空间维数，故成基。
:::

:::定理 布尔影响与噪声算子
对 $f:\{-1,1\}^n\to\{-1,1\}$，坐标影响 $\operatorname{Inf}_i(f)=P(f(x)\ne f(x^{\oplus i}))=\sum_{S\ni i}\widehat f(S)^2$。若每个坐标独立以概率 $(1-\rho)/2$ 翻转，噪声算子满足 $T_\rho\chi_S=\rho^{|S|}\chi_S$。
|||证明思路
离散导数 $(f(x)-f(x^{\oplus i}))/2$ 只保留含 $i$ 的 Fourier 项，平方期望即影响。噪声下每个坐标的条件均值乘 $\rho$，独立性使 $|S|$ 个坐标产生因子 $\rho^{|S|}$。
:::

:::定理 FFT 与多项式乘法
长度为 $n=2^k$ 的 DFT 可用 $O(n\log n)$ 次算术运算计算。次数分别小于 $a,b$ 的多项式相乘，可零填充到至少 $a+b-1$ 点，变换、逐点相乘、逆变换。
|||解释
按偶数和奇数下标拆分，得到两个长度 $n/2$ 的变换，递推 $T(n)=2T(n/2)+O(n)$。零填充避免循环卷积绕回。有限域 NTT 需域中存在所需阶的单位根，且变换长度可逆。
:::
