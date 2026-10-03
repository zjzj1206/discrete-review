# 05 · 群与同态

群把“可逆操作”抽象出来。先认识子群和陪集，再理解正规性为何保证商运算良定义，最后用同态把复杂群分解为核与像。

:::定义 半群、幺半群、群与 Abel 群
封闭二元运算满足结合律得到半群；有单位元得到幺半群；每个元素可逆得到群；再满足交换律得到 Abel 群。元素阶是使 $g^n=e$ 的最小正整数，不存在时为无限阶。
|||解释
单位元唯一，逆元唯一，$(ab)^{-1}=b^{-1}a^{-1}$，消去律成立。有限可消去幺半群必为群；无限情形不成立，如 $(\mathbb N,+)$。
:::

:::引理 子群判别法
非空子集 $H\subseteq G$ 为子群，当且仅当对所有 $a,b\in H$ 有 $ab^{-1}\in H$。
|||证明
取 $a=b$ 得 $e\in H$；取 $a=e$ 得逆元封闭；再把 $b^{-1}$ 代入得到乘法封闭。结合律从 $G$ 继承。
:::

:::定义 生成子群、循环群与置换群
$\langle S\rangle$ 为包含 $S$ 的最小子群。单个元素生成的群称循环群。$S_n$ 为 $n$ 个点上的置换群，$A_n$ 为偶置换子群。置换可分解为不交循环，阶等于循环长度的最小公倍数。
|||解释
长度 $k$ 的循环符号为 $(-1)^{k-1}$；置换复合先作用哪一侧要统一约定。$|S_n|=n!$，$n\ge2$ 时 $|A_n|=n!/2$。
:::

:::定理 循环群的子群
无限循环群同构于 $(\mathbb Z,+)$；$n$ 阶循环群同构于 $\mathbb Z/n\mathbb Z$。循环群的子群仍循环；对每个 $d\mid n$，$n$ 阶循环群有唯一的 $d$ 阶子群。
|||证明
映射 $k\mapsto g^k$ 的核为 $n\mathbb Z$ 或 $\{0\}$。对子群取最小正指数 $m$ 使 $g^m\in H$，带余除法说明每个子群元素均由 $g^m$ 生成。另有 $\operatorname{ord}(g^k)=n/\gcd(n,k)$。
:::

:::定理 Lagrange 定理
有限群 $G$ 的子群 $H$ 满足 $|G|=[G:H]|H|$。元素阶整除群阶。
|||证明
左陪集构成 $G$ 的划分，每个陪集经 $h\mapsto gh$ 与 $H$ 等势。取 $H=\langle g\rangle$ 得后半句。整除关系的逆命题一般不成立：群阶的每个因子未必都对应一个子群。
:::

:::定义 正规子群与商群
$N\trianglelefteq G$ 表示 $gNg^{-1}=N$ 对每个 $g$ 成立，等价于左右陪集相等。商群 $G/N$ 以陪集为元素，$(gN)(hN)=ghN$。
|||解释
正规性保证更换代表元不改变乘积陪集。指数为 2 的子群必正规。Abel 群的每个子群正规；正规性本身不传递，$K\trianglelefteq H\trianglelefteq G$ 不自动推出 $K\trianglelefteq G$。
:::

:::定理 群的第一同构定理
群同态 $f:G\to H$ 的核正规，像为子群，且 $G/\ker f\cong\operatorname{im}f$。
|||证明
$f(gkg^{-1})=e$ 说明核正规。映射 $g\ker f\mapsto f(g)$ 良定义且保乘法；相同像当且仅当两代表元相差核中的元素，故单射；满射来自像的定义。
:::

:::定理 第二、第三同构定理与对应定理
若 $N\trianglelefteq G$、$H\le G$，则 $HN/N\cong H/(H\cap N)$。若 $N\le K\trianglelefteq G$ 且 $N\trianglelefteq G$，则 $(G/N)/(K/N)\cong G/K$。包含 $N$ 的子群与 $G/N$ 的子群通过取像、取逆像一一对应，并保持正规性。
|||证明思路
第一式限制自然映射到 $H$，核为 $H\cap N$；第二式使用 $gN\mapsto gK$，核为 $K/N$。对应定理检查 $\pi^{-1}(\pi(H))=H$ 与 $\pi(\pi^{-1}(L))=L$。
:::

:::定义 换位子群、可解群与自同构
$G'=\langle aba^{-1}b^{-1}:a,b\in G\rangle$。若反复取换位子群最终得到平凡群，则 $G$ 可解。自同构组成 $\operatorname{Aut}(G)$，共轭映射组成内自同构群 $\operatorname{Inn}(G)$。
|||解释
$G'\trianglelefteq G$，且 $G/N$ 为 Abel 群当且仅当 $G'\le N$。$\operatorname{Inn}(G)\cong G/Z(G)$，并正规于 $\operatorname{Aut}(G)$，因为 $\alpha c_g\alpha^{-1}=c_{\alpha(g)}$。
:::

:::定理 有限生成 Abel 群结构定理
每个有限生成 Abel 群同构于 $\mathbb Z^r\oplus\mathbb Z/d_1\mathbb Z\oplus\cdots\oplus\mathbb Z/d_k\mathbb Z$，其中 $1<d_1\mid d_2\mid\cdots\mid d_k$，这些不变量唯一。有限 Abel 群也可唯一分解为素数幂阶循环群的直积。
|||证明思路
把生成元间关系写为整数矩阵，以可逆整行整列运算化成 Smith 标准形。对角元给出有限循环因子，零方向给出自由部分。注意 $C_4$ 与 $C_2\times C_2$ 同阶但不同构，可用元素阶区分。
:::

处理同构题时，先明确映射，再依次验证良定义、保运算、单射与满射。不能用“元素个数相同”直接认定同构。
