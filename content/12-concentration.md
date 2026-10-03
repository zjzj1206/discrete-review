# 12 · 集中不等式与大偏差

尾界按已知信息选择：只知均值用 Markov，知道方差用 Chebyshev，具有独立性和矩母函数控制时用 Chernoff。Sanov 从经验分布角度解释指数衰减率。

:::定理 Markov 与 Chebyshev 不等式
若 $X\ge0,a>0$，$P(X\ge a)\le E[X]/a$。若方差有限，则 $P(|X-E[X]|\ge t)\le\operatorname{Var}(X)/t^2$。
|||证明
$X\ge a1_{X\ge a}$，取期望得 Markov。将其用于非负变量 $(X-E[X])^2$ 得 Chebyshev。不能把 Markov 直接用于可取负值的 $X$。
:::

:::定理 Chernoff 矩母函数界
对 $t>0$，$P(X\ge a)\le e^{-ta}E[e^{tX}]$；对独立和 $S=\sum_iX_i$，右边为 $e^{-ta}\prod_iE[e^{tX_i}]$，可对 $t>0$ 取下确界。
|||证明
对 $e^{tX}$ 使用 Markov；独立性拆开乘积期望。下尾可用 $t<0$ 对事件重新推导，不能沿用上尾的单调方向而不检查。
:::

:::定理 Bernoulli 的 KL 尾界
独立 $X_i\sim\operatorname{Bern}(p)$，$p<q<1$ 时 $P(\bar X\ge q)\le e^{-nd_e(q\Vert p)}$，其中 $d_e(q\Vert p)=q\ln(q/p)+(1-q)\ln((1-q)/(1-p))$。$q<p$ 时有对应下尾界。
|||证明
矩母函数为 $1-p+pe^t$，使 $\ln(1-p+pe^t)-tq$ 最小的参数满足 $e^t=q(1-p)/(p(1-q))$。代回得到散度。注意散度第一参数是偏离目标 $q$，第二参数是真实均值 $p$。
:::

:::定理 乘法型 Chernoff 界
独立 Bernoulli 之和 $S$ 的均值为 $\mu$。$0<\delta\le1$ 时 $P(S\ge(1+\delta)\mu)\le e^{-\mu\delta^2/3}$；$0<\delta<1$ 时 $P(S\le(1-\delta)\mu)\le e^{-\mu\delta^2/2}$。
|||证明思路
用 $1+p(e^t-1)\le\exp(p(e^t-1))$ 控制矩母函数，再优化 $t=\ln(1+\delta)$。下尾类似。最后用对数的二阶估计简化精确指数。
:::

:::定理 Hoeffding 不等式
独立变量 $X_i\in[a_i,b_i]$ 满足 $P(\sum_i(X_i-E[X_i])\ge t)\le\exp(-2t^2/\sum_i(b_i-a_i)^2)$。两侧界在右边乘 2。
|||证明思路
先用凸性证明有界中心化变量的矩母函数不超过 $\exp(s^2(b-a)^2/8)$，再相乘并优化参数。若变量范围不受限或缺少独立性，不能直接套用。
:::

:::定理 弱大数定律
独立同分布且方差有限的 $X_i$ 满足 $\bar X_n\to E[X_1]$（依概率）。
|||证明
$\operatorname{Var}(\bar X_n)=\operatorname{Var}(X_1)/n$，用 Chebyshev 得每个固定 $\varepsilon>0$ 的偏差概率至多 $\operatorname{Var}(X_1)/(n\varepsilon^2)$，趋于零。
:::

:::定理 Stirling 公式与类型计数
$n!\sim\sqrt{2\pi n}(n/e)^n$。在 $m$ 元字母表上，长度 $n$ 的经验分布（类型）至多有 $(n+1)^m$ 种；类型 $Q$ 的序列数不超过 $2^{nH(Q)}$。
|||解释
类型类的精确大小为多项式系数 $n!/\prod_x(nQ(x))!$。Stirling 展开给出主指数 $nH(Q)$ 及多项式规模的修正项。
:::

:::定理 有限字母表的 Sanov 上界
独立样本来自 $P$，经验分布为 $\widehat P_n$，对任意分布集合 $\mathcal A$，$P(\widehat P_n\in\mathcal A)\le(n+1)^m\exp(-n\inf_{Q\in\mathcal A}D_e(Q\Vert P))$。精确渐近指数还需内外逼近等正则条件。
|||证明思路
每个类型 $Q$ 的单个序列概率为 $\exp(-n(H_e(Q)+D_e(Q\Vert P)))$；乘上类型类大小后得到 $\exp(-nD_e)$ 上界，再对不超过 $(n+1)^m$ 个类型求和。不能随意删除有限样本界中的多项式因子。
:::

:::定义 指数倾斜与率函数
对有限支持分布 $P$，令 $P_t(x)=P(x)e^{tx}/Z(t)$，$Z(t)=E_P[e^{tX}]$。$\Lambda(t)=\ln Z(t)$ 满足 $\Lambda'(t)=E_{P_t}[X]$、$\Lambda''(t)=\operatorname{Var}_{P_t}(X)\ge0$。均值尾界的率函数为 $\sup_t(ta-\Lambda(t))$。
|||解释
指数倾斜把罕见均值变成新分布中的常见均值，并连接 Chernoff 与散度最小化。在能选到 $E_{P_t}X=a$ 时，$D_e(P_t\Vert P)=ta-\Lambda(t)$。
:::
