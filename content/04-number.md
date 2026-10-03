# 04 · 初等数论

数论的基本手段是把整数关系改写为线性组合与同余。Euclid 算法处理最大公因数，Bézout 处理可解性，中国剩余定理把互素模数拆开。

:::定义 整除、最大公因数与同余
$a\mid b$ 指 $b=ak$ 对某整数 $k$ 成立。非全零整数 $a,b$ 的最大公因数取正值。$a\equiv b\pmod m$ 表示 $m\mid(a-b)$，这里 $m\ge1$。
|||解释
模运算中可以加、减、乘；约去因子需要条件。由 $ac\equiv bc\pmod m$ 仅能推出 $a\equiv b\pmod{m/\gcd(c,m)}$。
:::

:::定理 Euclid 算法与 Bézout 恒等式
$\gcd(a,b)=\gcd(b,a-qb)$，且存在整数 $x,y$ 使 $ax+by=\gcd(a,b)$。
|||证明
两边具有相同的公因数。重复带余除法直到余数为零，最后非零余数即最大公因数；逆向代入每一步除法，得到线性组合。反过来仅有 $ax+by=d$ 还不足以说明 $d$ 是最大公因数，需再证明 $d$ 为公因数。
:::

:::引理 Euclid 引理与算术基本定理
若 $p$ 为素数且 $p\mid ab$，则 $p\mid a$ 或 $p\mid b$。每个大于 1 的整数可唯一分解为素数乘积，忽略因子顺序。
|||证明
若 $p\nmid a$，则 $\gcd(p,a)=1$，用 Bézout 得 $up+va=1$，乘以 $b$ 即得 $p\mid b$。分解存在性对整数归纳；唯一性逐个用 Euclid 引理消去素因子。
:::

:::定理 线性同余方程
$ax\equiv b\pmod m$ 可解当且仅当 $d=\gcd(a,m)$ 整除 $b$。可解时模 $m$ 恰有 $d$ 个不同解；模 $m/d$ 有唯一解。
|||证明
方程等价于 $ax+my=b$，Bézout 给出充要条件。除以 $d$ 后 $a/d$ 与 $m/d$ 互素可逆，解为某个 $x_0$ 模 $m/d$ 的同余类，在模 $m$ 中展开得到 $d$ 个代表。
:::

:::定理 中国剩余定理
若 $m_1,\ldots,m_r$ 两两互素，则任意 $x\equiv a_i\pmod{m_i}$ 有唯一模 $M=\prod_i m_i$ 的解。等价地 $\mathbb Z/M\mathbb Z\cong\prod_i\mathbb Z/m_i\mathbb Z$。
|||证明
置 $M_i=M/m_i$，取 $u_iM_i\equiv1\pmod{m_i}$，则 $x=\sum_i a_i u_iM_i$ 满足全部同余。两解之差被每个 $m_i$ 整除，故被 $M$ 整除。模数不互素时还需余数在公因数模意义下相容。
:::

:::定义 Euler 函数与单位群
$\varphi(n)$ 是 $1\le a\le n$ 中与 $n$ 互素者个数，等于单位群 $(\mathbb Z/n\mathbb Z)^\times$ 的阶。$\varphi(n)=n\prod_{p\mid n}(1-1/p)$。
|||解释
用容斥排除能被各素因子整除的整数即得公式。素数幂满足 $\varphi(p^k)=p^k-p^{k-1}$；互素数满足 $\varphi(mn)=\varphi(m)\varphi(n)$。
:::

:::定理 Euler 定理与 Fermat 小定理
若 $\gcd(a,n)=1$，则 $a^{\varphi(n)}\equiv1\pmod n$。若 $p$ 为素数，任意整数 $a$ 满足 $a^p\equiv a\pmod p$。
|||证明
在单位群使用 Lagrange 定理，元素阶整除群阶。Fermat 的互素情形由 $\varphi(p)=p-1$ 得到；$p\mid a$ 的情形直接成立。约化指数前必须先检查互素条件。
:::

:::定理 Wilson 定理
整数 $p>1$ 为素数，当且仅当 $(p-1)!\equiv-1\pmod p$。
|||证明
素数情形在单位群中把互逆但不相等的元素配对，留下 $1,-1$，积为 $-1$，$p=2$ 单独检查。反向若 $p$ 合成，取真因子 $d$，则 $d\mid(p-1)!$，不可能同时有 $d\mid((p-1)!+1)$。
:::

:::引理 指数差的最大公因数
对整数 $a\ge2$ 和正整数 $m,n$，$\gcd(a^m-1,a^n-1)=a^{\gcd(m,n)}-1$。
|||证明
当 $m\ge n$，用 $a^m-1=a^{m-n}(a^n-1)+(a^{m-n}-1)$，将指数对替换为 $(n,m-n)$。按 Euclid 算法反复操作，终止时得到 $(d,0)$。
:::

:::定义 二次剩余、Legendre 符号与 RSA
奇素数 $p$ 下，非零平方称二次剩余；$\left(\frac ap\right)$ 分别在非零平方、非平方、零时取 $1,-1,0$。Euler 判别为 $a^{(p-1)/2}\equiv\left(\frac ap\right)\pmod p$。RSA 的数学模型取不同素数 $p,q$、$N=pq$，选 $ed\equiv1\pmod{\varphi(N)}$，加密 $x\mapsto x^e$，解密取 $d$ 次幂。
|||解释与证明思路
有限域乘法群循环，平方对应偶指数，因而恰占非零元素的一半并得到 Euler 判别与乘法性。RSA 正确性分别在模 $p$、模 $q$ 下用 Fermat（整除时直接检查），再用 CRT 拼合。这里仅说明数论原理，不是实际安全加密协议的完整实现。
:::

:::例题 一次同余与模幂
求解 $2024x\equiv23\pmod{115}$，并求 $\varphi(2024)$。
|||解答
$\gcd(2024,115)=23$，约去后为 $88x\equiv1\pmod5$，即 $x\equiv2\pmod5$；在 90 到 99 中为 92、97。$2024=2^3\cdot11\cdot23$，故 $\varphi(2024)=2024(1-1/2)(1-1/11)(1-1/23)=880$。
:::
