# 12 · 集中不等式与大偏差

本章按概念的依赖顺序展开：尾事件与最少假设的界 → 指数方法：独立性带来指数衰减 → 大数定律与收敛模式 → 类型与大偏差：概率与计数相消。先读每节常显主线，再展开定义、推导与例子；基础符号不会留到例题后才解释。

**阅读前提**：第 10 章的期望方差；KL 形式需第 11 章。**来源范围**：师生笔记第 12 章；教参附录 A。条目按本站顺序编号，原资料编号以来源为准。

## 12.1 尾事件与最少假设的界

先定义想控制的事件和阈值，再看手里知道均值、方差还是独立有界性。上界不是精确概率，可以同时有多个有效上界。

:::定义 偏差、尾概率与矩母函数
- **尾概率**：上尾为 $P(X\ge a)$，下尾为 $P(X\le a)$；若 $E[X]$ 有限，双侧偏差概率为 $P(|X-E[X]|\ge t)$（$t>0$）。
- **矩母函数**：$M_X(\lambda)=E[e^{\lambda X}]$，参数 $\lambda\in\mathbb R$。它可能为 $+\infty$；用于得到有效数值界时要选择使其有限的参数。
- **上尾的指数界**：$\lambda>0$ 时，$X\ge a\Rightarrow e^{\lambda X}\ge e^{\lambda a}$，故由 Markov 不等式得 $P(X\ge a)\le e^{-\lambda a}M_X(\lambda)$。
- **下尾的指数界**：$\lambda<0$ 时，$X\le a\Rightarrow e^{\lambda X}\ge e^{\lambda a}$，同样得 $P(X\le a)\le e^{-\lambda a}M_X(\lambda)$。
- **参数选择**：上尾在允许的 $\lambda>0$ 中取下确界，下尾在 $\lambda<0$ 中取下确界；不能忽略指数函数随参数符号改变的单调方向。
|||最初的两步推导
- $X\ge 0$ 时逐点有 $X\ge a1_{X\ge a}$（$a>0$），取期望得 Markov。

- 对 $(X-EX)^2$ 应用同一结论，得 Chebyshev 的 $\operatorname{Var}(X)/t^{2}$。

- Chebyshev 不需要正态分布，也不需要独立；只有在计算随机和方差时才可能用到独立性。
:::

:::定理 Markov 与 Chebyshev 不等式
- 若 $X\ge0,a>0$，$P(X\ge a)\le E[X]/a$。

- 若方差有限，则 $P(|X-E[X]|\ge t)\le\operatorname{Var}(X)/t^2$。
|||证明
- $X\ge a1_{X\ge a}$，取期望得 Markov。

- 将其用于非负变量 $(X-E[X])^2$ 得 Chebyshev。

- 不能把 Markov 直接用于可取负值的 $X$。
:::

## 12.2 指数方法：独立性带来指数衰减

先对指数变量用 Markov，再将独立和的矩母函数分解，最后优化参数。每一个前提都出现在一个具体步骤中。

:::定义 指数倾斜与率函数
- 对有限支持分布 $P$，令 $P_t(x)=P(x)e^{tx}/Z(t)$，$Z(t)=E_P[e^{tX}]$。

- $\Lambda(t)=\ln Z(t)$ 满足 $\Lambda'(t)=E_{P_t}[X]$、$\Lambda''(t)=\operatorname{Var}_{P_t}(X)\ge0$。

- 均值尾界的率函数为 $\sup_t(ta-\Lambda(t))$。
|||解释
- 指数倾斜把罕见均值变成新分布中的常见均值，并连接 Chernoff 与散度最小化。

- 在能选到 $E_{P_t}X=a$ 时，$D_e(P_t\Vert P)=ta-\Lambda(t)$。
:::

:::引理 Hoeffding 引理的二阶导数证明
- 若 $X\in[a,b]$ 且 $E[X]=0$，则 $\ln E[e^{tX}]\le t^2(b-a)^2/8$。
|||倾斜分布把求导变成方差
- 令 $\psi(t)=\ln E[e^{tX}]$。

- 因为有界，可以交换求导与期望；$\psi'(t)$ 是指数倾斜分布下的均值，$\psi''(t)$ 是其方差。

- 任意落在 $[a,b]$ 的变量 $Y$ 满足

  $$\operatorname{Var}(Y)=\min_c E[(Y-c)^2]\le E[(Y-(a+b)/2)^2]\le(b-a)^2/4.$$

- 倾斜后支持不变，故 $\psi''(t)\le(b-a)^2/4$。

- 由 $\psi(0)=\psi'(0)=0$，二阶积分或 Taylor 积分余项得所需上界。

- 独立中心化和的对数矩母函数相加，因此尾概率至多 $\exp(-st+s^2V/8)$，其中 $V=\sum_i(b_i-a_i)^2$。

- 选择 $s=4t/V$ 即得到指数 $-2t^2/V$。
:::

:::定理 Chernoff 矩母函数界
- 对 $t>0$，$P(X\ge a)\le e^{-ta}E[e^{tX}]$；对独立和 $S=\sum_iX_i$，右边为 $e^{-ta}\prod_iE[e^{tX_i}]$，可对 $t>0$ 取下确界。
|||证明
- 对 $e^{tX}$ 使用 Markov；独立性拆开乘积期望。

- 下尾可用 $t<0$ 对事件重新推导，不能沿用上尾的单调方向而不检查。
:::

:::定理 Hoeffding 不等式
- 独立变量 $X_i\in[a_i,b_i]$ 满足 $P(\sum_i(X_i-E[X_i])\ge t)\le\exp(-2t^2/\sum_i(b_i-a_i)^2)$。

- 两侧界在右边乘 $2$。
|||证明思路
- 先用凸性证明有界中心化变量的矩母函数不超过 $\exp(s^2(b-a)^2/8)$，再相乘并优化参数。

- 若变量范围不受限或缺少独立性，不能直接套用。
:::

:::定理 Bernoulli 的 KL 尾界
- 独立 $X_i\sim\operatorname{Bern}(p)$，$p<q<1$ 时 $P(\bar X\ge q)\le e^{-nd_e(q\Vert p)}$，其中 $d_e(q\Vert p)=q\ln(q/p)+(1-q)\ln((1-q)/(1-p))$。

- $q<p$ 时有对应下尾界。
|||证明
- 矩母函数为 $1-p+pe^t$，使 $\ln(1-p+pe^t)-tq$ 最小的参数满足 $e^t=q(1-p)/(p(1-q))$。

- 代回得到散度。

- 注意散度第一参数是偏离目标 $q$，第二参数是真实均值 $p$。
:::

:::定理 Bernoulli KL 界的优化过程
- 对 $S\sim\operatorname{Bin}(n,p)$、$p<q<1$，$P(S\ge nq)\le e^{-nd_e(q\Vert p)}$。
|||从一维凸优化到答案
- 独立性给 $E[e^{tS}]=(1-p+pe^t)^n$。

- Markov 后取对数并除以 $n$，要最小化 $f(t)=\ln(1-p+pe^t)-tq$，$t>0$。

- 导数为 $pe^t/(1-p+pe^t)-q$。

- 令其为零，得 $e^{t_*}=q(1-p)/(p(1-q))>1$。

- 二阶导数非负，故确为最小点。

- 此时 $1-p+pe^{t_*}=(1-p)/(1-q)$，代回可得

  $$f(t_*)=(1-q)\ln\frac{1-p}{1-q}+q\ln\frac pq=-d_e(q\Vert p).$$

- 当 $q<p$ 时相同代数给 $t_*<0$，对应下尾而非上尾；边界 $q=1$ 可直接算出 $P(S=n)=p^n$。
:::

:::定理 乘法型 Chernoff 界
- 独立 Bernoulli 之和 $S$ 的均值为 $\mu$。

- $0<\delta\le1$ 时 $P(S\ge(1+\delta)\mu)\le e^{-\mu\delta^2/3}$；$0<\delta<1$ 时 $P(S\le(1-\delta)\mu)\le e^{-\mu\delta^2/2}$。
|||证明思路
- 用 $1+p(e^t-1)\le\exp(p(e^t-1))$ 控制矩母函数，再优化 $t=\ln(1+\delta)$。

- 下尾类似。

- 最后用对数的二阶估计简化精确指数。
:::

:::例题 从一次 Markov 到 Bernoulli 指数界
- 设 $S=\sum_{i=1}^nX_i$，各 Xi 独立 $\operatorname{Bernoulli}(p)$。

- 对 $\lambda >0$，$P(S\ge nq)\le e^{-\lambda nq}(1-p+pe^\lambda)^n$。
|||逐步说明每一项
- 单个变量 $E[e^{\lambda X_i}]=(1-p)e^0+pe^\lambda$；独立性把乘积的期望变成期望的乘积。

- 对 $q>p$，最优参数满足 $e^\lambda=q(1-p)/(p(1-q))$，代回指数得到 $-nD_e(q\Vert p)$。

- $q=p$ 时优化值为 $0$；$q<p$ 求上尾不能强用负 $\lambda$，负参数对应下尾。

- 端点 $q=1$ 应取极限或直接算 $P(S=n)=p^{n}$。
:::

:::例题 抛硬币偏差：比较 Chebyshev 与 Hoeffding
- 独立抛 $1000$ 次公平硬币，令正面数为 $S$。

- 估计 $P(|S-500|\ge100)$。
|||把变量尺度统一再代入
- $E[S]=500$，$\operatorname{Var}(S)=250$，所以 Chebyshev 给 $250/100^2=0.025$。

- Hoeffding 中每项范围长度是 $1$，所以双侧上界为 $2\exp(-2\cdot100^2/1000)=2e^{-20}$，约 $4.12\times10^{-9}$。

- 这不是实际概率的等式，只是两个上界。

- 若写样本均值 $\bar X=S/1000$，阈值必须改成 $0.1$，得到 $2e^{-2\cdot1000\cdot0.1^2}$，与前式一致。
:::

## 12.3 大数定律与收敛模式

“偏差概率趋零”是关于每个固定 ε 的极限，不是保证某一条样本路径从此完全无偏差。

:::定义 收敛模式与大数定律的使用范围
- **共同前提**：$(X_n)_{n\ge1}$ 与 $X$ 为同一概率空间上的随机变量。
- **依概率收敛**：$X_n\xrightarrow{P}X$ 指 $\forall\varepsilon>0,\ \lim_{n\to\infty}P(|X_n-X|>\varepsilon)=0$。
- **几乎处处收敛**：$X_n\xrightarrow{a.s.}X$ 指 $P(\{\omega:\lim_{n\to\infty}X_n(\omega)=X(\omega)\})=1$。
- **路径上的“最终”**：在上述概率为 $1$ 的事件内，$\forall\varepsilon>0,\exists N=N(\omega,\varepsilon),\forall n\ge N,\ |X_n(\omega)-X(\omega)|<\varepsilon$；下标可依赖样本结果与误差容限。
- **关系**：几乎处处收敛推出依概率收敛，反向一般不成立。
- **大数定律的对象**：弱大数定律讨论样本平均 $\bar X_n$ 依概率趋向均值；强大数定律讨论几乎处处收敛。使用时必须核对独立性、同分布和矩条件。
|||不能从一个尾界跳过量词
- Chebyshev 给出独立同分布有限方差样本均值的依概率收敛。

- 对有界独立同分布变量，Hoeffding 给出的偏差概率对 $n$ 可求和；由第一 Borel–Cantelli 引理，每个固定有理正阈值仅被超过有限次，再取可数交得到几乎处处收敛。

- 第一 Borel–Cantelli 的证明只用并界：$P(\exists n\ge N:A_n)\le\sum_{n\ge N}P(A_n)\to0$。

- 但仅知道各项概率趋零，不保证级数收敛，不能照搬这一证明。
:::

:::定理 弱大数定律
- 独立同分布且方差有限的 $X_i$ 满足 $\bar X_n\to E[X_1]$（依概率）。
|||证明
- $\operatorname{Var}(\bar X_n)=\operatorname{Var}(X_1)/n$，用 Chebyshev 得每个固定 $\varepsilon>0$ 的偏差概率至多 $\operatorname{Var}(X_1)/(n\varepsilon^2)$，趋于零。
:::

## 12.4 类型与大偏差：概率与计数相消

经验分布记录各符号出现的比例。类型类数目由组合计数决定，每条序列的概率由源分布决定，二者相乘出现 KL。

:::定义 经验分布、类型类与离散网格
- **对象**：有限字母表 $\mathcal X$，$|\mathcal X|=m$，观测序列 $x^n=(x_1,\ldots,x_n)\in\mathcal X^n$。
- **经验分布／类型**：$Q_{x^n}(a)=\frac1n|\{i\in[n]:x_i=a\}|$。它非负、总和为 $1$，每个坐标只能取 $0,1/n,\ldots,1$。
- **可实现条件**：分布 $Q$ 是某个长度 $n$ 序列的类型，当且仅当 $nQ(a)\in\mathbb N_0$ 对每个 $a$ 成立。
- **类型类**：$T_Q=\{x^n\in\mathcal X^n:Q_{x^n}=Q\}$；可实现时 $|T_Q|=n!/\prod_a(nQ(a))!$。
- **离散网格的作用**：若二元成功次数要求 $S\ge nq$，但 $nq$ 不是整数，则实际最小值为 $\lceil nq\rceil$。精确概率计算必须在合法类型上求和。
|||例子与网格边界
- 长度 $4$ 的二元序列有 $5$ 种类型，正面频率只可能 $0$、$1/4$、$1/2$、$3/4$、$1$；$Q(1)=1/2$ 的类型类有 $C(4,2)=6$ 条。

- 在 $P(S\ge nq)$ 中若 nq 非整数，最小成功次数是 $\operatorname{ceil}(nq)$，不能把不存在的类型直接作为某一项精确概率。
:::

:::定理 Stirling 公式与类型计数
- $n!\sim\sqrt{2\pi n}(n/e)^n$。

- 在 $m$ 元字母表上，长度 $n$ 的经验分布（类型）至多有 $(n+1)^m$ 种；类型 $Q$ 的序列数不超过 $2^{nH(Q)}$。
|||解释
- 类型类的精确大小为多项式系数 $n!/\prod_x(nQ(x))!$。

- Stirling 展开给出主指数 $nH(Q)$ 及多项式规模的修正项。
:::

:::定理 类型方法为何出现相对熵
- 有限字母表上，一个类型 $Q$ 的序列在源 $P$ 下的总概率满足 $P(T_Q)\le e^{-nD_e(Q\Vert P)}$。
|||序列数量与单条概率的指数相消
- 同类型每条序列的概率相同，为

  $$\prod_xP(x)^{nQ(x)}=\exp\left(n\sum_xQ(x)\ln P(x)\right)=e^{-n(H_e(Q)+D_e(Q\Vert P))}.$$

- 另一方面，在以 $Q$ 为源的实验中，每条同类型序列概率为 $e^{-nH_e(Q)}$，而整个类型类概率至多 $1$，故 $|T_Q|\le e^{nH_e(Q)}$。

- 两者相乘，熵项消掉，只留下散度。

- 再对所有满足条件的类型求和，类型数至多 $(n+1)^m$，得到 Sanov 的有限样本上界。

- 它提供上界；若要证明极限指数恰等于某个值，还必须从目标集合内找到逼近最优分布的可实现类型并给下界。
:::

:::定理 有限字母表的 Sanov 上界
- 独立样本来自 $P$，经验分布为 $\widehat P_n$，对任意分布集合 $\mathcal A$，$P(\widehat P_n\in\mathcal A)\le(n+1)^m\exp(-n\inf_{Q\in\mathcal A}D_e(Q\Vert P))$。

- 精确渐近指数还需内外逼近等正则条件。
|||证明思路
- 每个类型 $Q$ 的单个序列概率为 $\exp(-n(H_e(Q)+D_e(Q\Vert P)))$；乘上类型类大小后得到 $\exp(-nD_e)$ 上界，再对不超过 $(n+1)^m$ 个类型求和。

- 不能随意删除有限样本界中的多项式因子。
:::

## 本章回顾：把结论连起来

同一个硬币偏差问题分别用 Chebyshev、Hoeffding 和 KL 界，比较利用的条件而非只看数值。能从 Markov 写出矩母函数优化，并把类型类的计数指数与单序列概率指数相消。
