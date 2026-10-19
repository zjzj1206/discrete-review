# 24 · 完整知识目录与学习路线

本页列出 19 个理论章节的实际知识条目。按章节学习时从上往下读；查概念时可用页面搜索。每个链接直接定位并展开原条目，证明仍可独立选择是否展开。

## 总体依赖框架

集合与映射 → 命题与一阶逻辑 → 自然数与公理基础；数论 → 群 → 群作用 → 环 → 域；组合计数 → 概率 → 熵与集中 → 编码、Markov、概率方法。图论以集合为对象基础，以计数、线性代数和概率为工具，优化匹配另设第 21 章。

## 按主题逐项查看


### 01 · 集合、关系与无穷

**1.1 集合与函数：先固定对象和记号**

- [定义 元素、包含、全集与索引族](01-sets.html#01-sets-item-1)

- [定义 集合运算与幂集](01-sets.html#01-sets-item-2)

- [定义 有序对、关系的定义域与逆关系](01-sets.html#01-sets-item-3)

- [定义 函数、单射、满射与双射](01-sets.html#01-sets-item-4)

- [引理 函数复合、左右逆与单满射](01-sets.html#01-sets-item-5)

- [例题 从逐元素证明开始：为什么逆像保持交集](01-sets.html#01-sets-item-6)

**1.2 关系、划分与序**

- [定义 关系性质的量词与反例](01-sets.html#01-sets-item-7)

- [定义 最小、极小、最大、极大必须分开](01-sets.html#01-sets-item-8)

- [定义 等价关系、偏序、全序与良序](01-sets.html#01-sets-item-9)

- [定义 关系闭包](01-sets.html#01-sets-item-10)

- [定义 上下界、上确界与 Hasse 图](01-sets.html#01-sets-item-11)

- [定理 等价关系与划分一一对应](01-sets.html#01-sets-item-12)

- [例题 等价类怎样变成新的对象](01-sets.html#01-sets-item-13)

**1.3 基数：先双射再比较无穷**

- [定义 基数、可数与不可数](01-sets.html#01-sets-item-14)

- [定义 Dedekind 有限与连续统假设](01-sets.html#01-sets-item-15)

- [引理 从有限编码到可数并](01-sets.html#01-sets-item-16)

- [定理 Cantor 定理](01-sets.html#01-sets-item-17)

- [定理 实数不可数](01-sets.html#01-sets-item-18)

- [定理 Cantor–Schröder–Bernstein](01-sets.html#01-sets-item-19)

- [例题 详细枚举：整数、有理数与有限字符串为什么可数](01-sets.html#01-sets-item-20)

**1.4 良序、序数与递归**

- [定义 序同构、初始段与传递集合](01-sets.html#01-sets-item-21)

- [定义 序数与基数运算](01-sets.html#01-sets-item-22)

- [定义 后继序数、极限序数与序数递归](01-sets.html#01-sets-item-23)

- [定义 选择公理、良序定理与 Zorn 引理](01-sets.html#01-sets-item-24)

- [定理 良序集与唯一序数对应](01-sets.html#01-sets-item-25)

- [定理 超限归纳与良序比较](01-sets.html#01-sets-item-26)

- [定理 自然数上的递归定理](01-sets.html#01-sets-item-27)

### 02 · 命题逻辑与证明系统

**2.1 语法：公式是怎样生成的**

- [定义 字母表、原子、连接词与子公式](02-logic.html#02-logic-item-1)

- [定义 公式的递归构造与结构归纳](02-logic.html#02-logic-item-2)

**2.2 语义：赋值、满足与范式**

- [定义 真值规则与可满足性分类](02-logic.html#02-logic-item-3)

- [定义 文字、子句、DNF 与 CNF](02-logic.html#02-logic-item-4)

- [定义 公式、赋值与逻辑后承](02-logic.html#02-logic-item-5)

- [例题 真值表、等价变形与范式](02-logic.html#02-logic-item-6)

**2.3 语法证明：规则与假设作用域**

- [定义 自然演绎规则](02-logic.html#02-logic-item-7)

- [定义 RAA、经典逻辑与直觉主义逻辑](02-logic.html#02-logic-item-8)

- [定义 Frege／Hilbert 风格证明与序列演算的差别](02-logic.html#02-logic-item-9)

- [定义 序列与 System K 的阅读方式](02-logic.html#02-logic-item-10)

- [引理 分情况证明为何必须得到同一结论](02-logic.html#02-logic-item-11)

- [例题 一份逐行自然演绎证明](02-logic.html#02-logic-item-12)

- [例题 Peirce 律的经典证明](02-logic.html#02-logic-item-13)

**2.4 元定理：证明系统为什么可信**

- [引理 真值赋值对应的文字集引理](02-logic.html#02-logic-item-14)

- [定理 可靠性与完备性](02-logic.html#02-logic-item-15)

- [定理 演绎定理与紧致性](02-logic.html#02-logic-item-16)

**2.5 直觉主义：未来世界与反模型**

- [定义 Kripke 模型](02-logic.html#02-logic-item-17)

- [引理 强迫关系的单调性](02-logic.html#02-logic-item-18)

- [例题 两个世界怎样否证 Peirce 律的直觉主义可证性](02-logic.html#02-logic-item-19)

### 03 · 一阶逻辑、算术与公理集合论

**3.1 一阶语法和模型：符号必须有解释**

- [定义 语言签名、元数与项的取值](03-foundations.html#03-foundations-item-1)

- [定义 自由变量、绑定变量、句子与满足](03-foundations.html#03-foundations-item-2)

- [定义 项、公式、结构与赋值](03-foundations.html#03-foundations-item-3)

**3.2 替换与量词推导**

- [定义 量词的自然演绎规则](03-foundations.html#03-foundations-item-4)

- [定理 语义替换引理](03-foundations.html#03-foundations-item-5)

- [例题 自由变量与避免捕获的替换](03-foundations.html#03-foundations-item-6)

**3.3 一致性、完备性与模型构造**

- [定义 一致、完备、扩张、保守扩张与 Henkin 见证](03-foundations.html#03-foundations-item-7)

- [定理 从一致理论构造模型：Henkin 证明的四个阶段](03-foundations.html#03-foundations-item-8)

- [定理 一阶逻辑可靠性、完备性与紧致性](03-foundations.html#03-foundations-item-9)

**3.4 算术：归纳与递归如何工作**

- [定义 Peano 算术与归纳公理模式](03-foundations.html#03-foundations-item-10)

- [引理 强归纳与普通归纳的转换](03-foundations.html#03-foundations-item-11)

- [定理 非标准算术模型的存在](03-foundations.html#03-foundations-item-12)

- [例题 PA 中加法交换律的分步推导路线](03-foundations.html#03-foundations-item-13)

**3.5 集合公理：哪些构造真的给出集合**

- [定义 ZFC 公理体系](03-foundations.html#03-foundations-item-14)

- [定义 传递集合、后继与集合论自然数](03-foundations.html#03-foundations-item-15)

- [定理 正则公理排除有限隶属环](03-foundations.html#03-foundations-item-16)

- [定理 选择公理的常见等价形式](03-foundations.html#03-foundations-item-17)

- [例题 Russell 悖论与分离公理的限制](03-foundations.html#03-foundations-item-18)

**3.6 证明的边界与类型论**

- [定义 类型判断与 Curry–Howard 对应](03-foundations.html#03-foundations-item-19)

- [定义 归纳、结构归纳与余归纳](03-foundations.html#03-foundations-item-20)

- [定理 Gödel 第一不完备定理（Rosser 加强形式）](03-foundations.html#03-foundations-item-21)

- [定理 Gödel 第二不完备定理](03-foundations.html#03-foundations-item-22)

- [解释 不完备性中的对角化究竟在做什么](03-foundations.html#03-foundations-item-23)

### 04 · 初等数论

**4.1 整数整除与带余除法**

- [定义 素数、互素与最小公倍数](04-number.html#04-number-item-1)

- [定义 整除、最大公因数与同余](04-number.html#04-number-item-2)

- [定理 带余除法的存在与唯一](04-number.html#04-number-item-3)

**4.2 公因数、Bézout 与唯一分解**

- [引理 Euclid 引理与算术基本定理](04-number.html#04-number-item-4)

- [引理 指数差的最大公因数](04-number.html#04-number-item-5)

- [定理 Euclid 算法与 Bézout 恒等式](04-number.html#04-number-item-6)

- [例题 扩展 Euclid 算法：从余数表找逆元](04-number.html#04-number-item-7)

**4.3 同余、逆元与方程组**

- [引理 同余中的合法消去](04-number.html#04-number-item-8)

- [定理 线性同余方程](04-number.html#04-number-item-9)

- [定理 中国剩余定理](04-number.html#04-number-item-10)

- [定理 非互素 CRT 与最小公倍数](04-number.html#04-number-item-11)

- [例题 中国剩余定理的构造不是猜数字](04-number.html#04-number-item-12)

- [例题 一次同余与模幂](04-number.html#04-number-item-13)

**4.4 模幂与乘法结构**

- [定义 Euler 函数与单位群](04-number.html#04-number-item-14)

- [定义 二次剩余、Legendre 符号与 RSA](04-number.html#04-number-item-15)

- [引理 Euler 函数的除数求和恒等式](04-number.html#04-number-item-16)

- [定理 Euler 定理与 Fermat 小定理](04-number.html#04-number-item-17)

- [定理 Euler 定理的剩余系置换证明](04-number.html#04-number-item-18)

- [定理 Wilson 定理](04-number.html#04-number-item-19)

- [定理 二次互反律与补充公式](04-number.html#04-number-item-20)

- [例题 RSA 正确性包括非互素明文](04-number.html#04-number-item-21)

**4.5 逼近的量词与误差下界**

- [例题 有理数的逼近指数为什么恰为 1](04-number.html#04-number-item-22)

### 05 · 群与同态

**5.1 运算、公理与基本推论**

- [定义 二元运算、封闭性与群的例子](05-groups.html#05-groups-item-1)

- [定义 半群、幺半群、群与 Abel 群](05-groups.html#05-groups-item-2)

- [引理 单位、逆元的唯一性与消去律](05-groups.html#05-groups-item-3)

**5.2 子群、循环群与置换**

- [定义 子群与生成子群的真正含义](05-groups.html#05-groups-item-4)

- [定义 生成子群、循环群与置换群](05-groups.html#05-groups-item-5)

- [引理 子群判别法](05-groups.html#05-groups-item-6)

- [定理 循环群的子群](05-groups.html#05-groups-item-7)

- [例题 置换的循环、乘法、符号与阶](05-groups.html#05-groups-item-8)

**5.3 陪集、指数与商群**

- [定义 左右陪集、指数与陪集相等判据](05-groups.html#05-groups-item-9)

- [定义 正规子群与商群](05-groups.html#05-groups-item-10)

- [引理 商群乘法良定义的具体检查](05-groups.html#05-groups-item-11)

- [定理 Lagrange 定理](05-groups.html#05-groups-item-12)

- [例题 在 S₃ 中实际计算陪集与共轭](05-groups.html#05-groups-item-13)

**5.4 同态、核与同构定理**

- [定义 同态、同构、核与像](05-groups.html#05-groups-item-14)

- [定理 群的第一同构定理](05-groups.html#05-groups-item-15)

- [定理 第二、第三同构定理与对应定理](05-groups.html#05-groups-item-16)

- [例题 第一同构定理如何成为实际算法](05-groups.html#05-groups-item-17)

**5.5 组合群与结构分类**

- [定义 外直积、内直积与半直积](05-groups.html#05-groups-item-18)

- [定义 自由群与约化字](05-groups.html#05-groups-item-19)

- [定义 交换幺半群的群完备化](05-groups.html#05-groups-item-20)

- [定义 换位子群、可解群与自同构](05-groups.html#05-groups-item-21)

- [定理 有限生成 Abel 群结构定理](05-groups.html#05-groups-item-22)

- [解释 结构定理与单群分类的边界](05-groups.html#05-groups-item-23)

### 06 · 群作用与 Sylow 定理

**6.1 群作用：把元素变成变换**

- [定义 左作用、忠实、传递与自由](06-actions.html#06-actions-item-1)

- [定义 群作用、轨道与稳定子](06-actions.html#06-actions-item-2)

- [定理 轨道—稳定子定理](06-actions.html#06-actions-item-3)

- [定理 Cayley 定理](06-actions.html#06-actions-item-4)

- [例题 正方形的顶点轨道与稳定子](06-actions.html#06-actions-item-5)

**6.2 共轭作用与类方程**

- [定义 p 群、p 子群与 Sylow 子群](06-actions.html#06-actions-item-6)

- [定义 中心化子与正规化子不能混用](06-actions.html#06-actions-item-7)

- [定义 共轭类、中心与中心化子](06-actions.html#06-actions-item-8)

- [定理 类方程与有限 p 群的中心](06-actions.html#06-actions-item-9)

- [定理 Cauchy 定理](06-actions.html#06-actions-item-10)

**6.3 p 群作用与 Sylow 证明链**

- [引理 p 群作用的固定点同余](06-actions.html#06-actions-item-11)

- [定理 Sylow 三定理](06-actions.html#06-actions-item-12)

- [定理 Sylow 存在性的子集作用证明](06-actions.html#06-actions-item-13)

- [定理 Sylow 包含性、共轭性与计数的细节](06-actions.html#06-actions-item-14)

**6.4 用作用识别具体群**

- [例题 15 阶群的结构](06-actions.html#06-actions-item-15)

- [例题 为什么 p² 阶群交换，为什么 pq 阶群未必循环](06-actions.html#06-actions-item-16)

- [例题 正方体旋转群](06-actions.html#06-actions-item-17)

### 07 · 环、理想与整除结构

**7.1 环的两种运算与基本对象**

- [定义 环、整环、域与单位](07-rings.html#07-rings-item-1)

- [定义 子环、环同态、单位群与零因子](07-rings.html#07-rings-item-2)

- [定义 多项式环、函数环与群环](07-rings.html#07-rings-item-3)

- [定义 除环、四元数与术语约定](07-rings.html#07-rings-item-4)

- [定理 有限整环必是域](07-rings.html#07-rings-item-5)

**7.2 理想与商：让加乘都良定义**

- [定义 理想、主理想与商环](07-rings.html#07-rings-item-6)

- [定义 理想的生成、和、积及素极大性](07-rings.html#07-rings-item-7)

- [定理 环的同构定理](07-rings.html#07-rings-item-8)

- [定理 素理想与极大理想判别](07-rings.html#07-rings-item-9)

- [定理 环的中国剩余定理](07-rings.html#07-rings-item-10)

- [例题 理想生成与 Z[x] 不是 PID](07-rings.html#07-rings-item-11)

**7.3 整除、分式域与分解体系**

- [定义 相伴、不可约与素元](07-rings.html#07-rings-item-12)

- [定义 分式域及其构造](07-rings.html#07-rings-item-13)

- [定义 Euclid 整环、PID 与 UFD](07-rings.html#07-rings-item-14)

- [定义 理想链、因子链与分解终止](07-rings.html#07-rings-item-15)

- [引理 整除、相伴与主理想包含的对应](07-rings.html#07-rings-item-16)

- [定理 因子链条件与素性给出 UFD 判据](07-rings.html#07-rings-item-17)

- [例题 从 72 的真因子链到完整分解](07-rings.html#07-rings-item-18)

- [定理 Euclid 整环 ⇒ PID ⇒ UFD](07-rings.html#07-rings-item-19)

- [定理 链条件与整环的 Artin 条件](07-rings.html#07-rings-item-20)

- [定理 PID 中分解存在性与唯一性的展开](07-rings.html#07-rings-item-21)

**7.4 多项式计算与不可约判定**

- [引理 域上多项式的带余除法与根数界](07-rings.html#07-rings-item-22)

- [引理 Gauss 引理与多项式不可约性](07-rings.html#07-rings-item-23)

- [定理 Eisenstein 判别法](07-rings.html#07-rings-item-24)

- [例题 平移后应用 Eisenstein](07-rings.html#07-rings-item-25)

- [例题 多项式 Euclid 算法与商环中的逆](07-rings.html#07-rings-item-26)

- [例题 矩阵环的双边理想为何只有两个](07-rings.html#07-rings-item-27)

### 08 · 域、有限域与 Galois 理论

**8.1 域扩张的线性代数语言**

- [定义 向量空间、线性组合、基与扩张次数](08-fields.html#08-fields-item-1)

- [定义 F[α]、F(α)、代数与超越](08-fields.html#08-fields-item-2)

- [定义 域扩张、代数元素与最小多项式](08-fields.html#08-fields-item-3)

- [定理 最小多项式为什么控制整个单扩张](08-fields.html#08-fields-item-4)

- [定理 塔式定理](08-fields.html#08-fields-item-5)

- [定理 有限扩张必代数，反向对无限扩张不成立](08-fields.html#08-fields-item-6)

- [定理 尺规作图与二次扩张的必要条件](08-fields.html#08-fields-item-7)

- [例题 二次扩张中的求逆与塔式计算](08-fields.html#08-fields-item-8)

**8.2 添根、特征、可分与正规**

- [定义 特征、可分性与正规性](08-fields.html#08-fields-item-9)

- [引理 正特征为什么一定是素数](08-fields.html#08-fields-item-10)

- [定理 根的添入与分裂域](08-fields.html#08-fields-item-11)

- [例题 非正规扩张为何不能直接套 Galois 对应](08-fields.html#08-fields-item-12)

**8.3 有限域的构造、分类和子域**

- [定义 有限域多项式分解的三层任务](08-fields.html#08-fields-item-13)

- [引理 有限域中的 Frobenius 多项式最大公因式](08-fields.html#08-fields-item-14)

- [定理 有限域的分类与乘法群](08-fields.html#08-fields-item-15)

- [定理 有限域存在性、唯一性与乘法循环性的证明](08-fields.html#08-fields-item-16)

- [定理 有限域的子域与 Frobenius](08-fields.html#08-fields-item-17)

- [定理 有限域不可约多项式的计数](08-fields.html#08-fields-item-18)

- [定理 有限域不可约式的根与分裂域](08-fields.html#08-fields-item-19)

- [例题 完整构造四元域](08-fields.html#08-fields-item-20)

- [例题 Frobenius 轨道怎样给出最小多项式](08-fields.html#08-fields-item-21)

**8.4 Galois 对应：固定的元素与允许的对称**

- [定义 域自同构、Galois 群与固定域](08-fields.html#08-fields-item-22)

- [定理 Galois 基本定理（有限情形）](08-fields.html#08-fields-item-23)

- [例题 二次扩张与四次扩张](08-fields.html#08-fields-item-24)

### 09 · 组合计数与生成函数

**9.1 计数对象与基本原则**

- [定义 标号、顺序、重复与计数等价](09-counting.html#09-counting-item-1)

- [定义 排列、组合与多项式系数](09-counting.html#09-counting-item-2)

- [引理 双计数与除法原则的前提](09-counting.html#09-counting-item-3)

- [定理 加法、乘法、双计数与鸽笼原理](09-counting.html#09-counting-item-4)

- [定理 二项式定理、Pascal 与 Vandermonde 恒等式](09-counting.html#09-counting-item-5)

- [例题 同样分 5 个球到 3 个盒子，为什么答案不同](09-counting.html#09-counting-item-6)

**9.2 整数解、容斥与特殊数列**

- [定义 Stirling 数的两种含义](09-counting.html#09-counting-item-7)

- [定义 Stirling 数与整数分拆](09-counting.html#09-counting-item-8)

- [定理 隔板法与受限盒子](09-counting.html#09-counting-item-9)

- [定理 容斥原理与反演](09-counting.html#09-counting-item-10)

- [定理 错排与满射计数](09-counting.html#09-counting-item-11)

- [例题 有上下界的隔板问题](09-counting.html#09-counting-item-12)

**9.3 生成函数：把系数问题变成代数**

- [定义 系数提取与形式幂级数乘法](09-counting.html#09-counting-item-13)

- [定义 普通生成函数与指数生成函数](09-counting.html#09-counting-item-14)

- [定理 递推与有理生成函数](09-counting.html#09-counting-item-15)

- [定理 Catalan 数](09-counting.html#09-counting-item-16)

- [定理 Catalan 的括号分解与反射双射](09-counting.html#09-counting-item-17)

- [定理 EGF 的乘法与集合划分公式](09-counting.html#09-counting-item-18)

- [例题 Fibonacci 的初值为什么不能漏](09-counting.html#09-counting-item-19)

**9.4 对称计数：作用、固定点与循环指标**

- [定义 固定点、轨道数与循环指标的变量](09-counting.html#09-counting-item-20)

- [引理 Burnside 引理](09-counting.html#09-counting-item-21)

- [定理 置换循环型的计数与循环指标](09-counting.html#09-counting-item-22)

- [定理 Pólya 计数](09-counting.html#09-counting-item-23)

- [例题 旋转项链](09-counting.html#09-counting-item-24)

- [例题 正方形顶点二染色：旋转与反射](09-counting.html#09-counting-item-25)

### 10 · 概率基础与概率生成函数

**10.1 概率空间、事件与随机变量**

- [定义 点概率、分布、联合与边缘](10-probability.html#10-probability-item-1)

- [定义 事件族、概率测度与随机变量](10-probability.html#10-probability-item-2)

**10.2 条件概率、独立与 Bayes**

- [定义 随机变量的独立与条件独立](10-probability.html#10-probability-item-3)

- [定义 概率空间、条件概率与独立性](10-probability.html#10-probability-item-4)

- [定理 全概率与 Bayes 公式](10-probability.html#10-probability-item-5)

- [例题 Bayes 公式中的基准概率](10-probability.html#10-probability-item-6)

**10.3 期望与方差：分布的数字特征**

- [定义 期望存在性、矩、协方差与条件期望](10-probability.html#10-probability-item-7)

- [引理 指示变量的期望与二阶矩](10-probability.html#10-probability-item-8)

- [定理 期望、方差与协方差](10-probability.html#10-probability-item-9)

- [定理 全期望与全方差](10-probability.html#10-probability-item-10)

- [定理 全方差公式的代数展开](10-probability.html#10-probability-item-11)

**10.4 分布模型、生成函数与等待时间**

- [定义 凸函数与 Jensen 的前提](10-probability.html#10-probability-item-12)

- [定义 常用离散分布](10-probability.html#10-probability-item-13)

- [定理 概率生成函数](10-probability.html#10-probability-item-14)

- [定理 尾和公式与集券问题](10-probability.html#10-probability-item-15)

- [定理 Jensen 不等式](10-probability.html#10-probability-item-16)

- [例题 无放回抽样的方差为何更小](10-probability.html#10-probability-item-17)

- [例题 几何分布与 Poisson 分布的矩推导](10-probability.html#10-probability-item-18)

**10.5 分支过程：递推概率的应用**

- [定理 分支过程的灭绝概率（历年拓展）](10-probability.html#10-probability-item-19)

- [例题 分支过程求最小不动点](10-probability.html#10-probability-item-20)

### 11 · 熵、散度与互信息

**11.1 信息量和熵：先固定单位**

- [定义 自信息、支撑与零概率约定](11-information.html#11-information-item-1)

- [定义 条件熵是对条件分布的平均](11-information.html#11-information-item-2)

- [定义 熵、联合熵与条件熵](11-information.html#11-information-item-3)

**11.2 散度、互信息与非负性**

- [定义 KL 的支持条件与互信息的等价式](11-information.html#11-information-item-4)

- [定义 KL 散度与互信息](11-information.html#11-information-item-5)

- [引理 对数和不等式与散度的联合凸性](11-information.html#11-information-item-6)

- [定理 Gibbs 不等式](11-information.html#11-information-item-7)

**11.3 链式法则、条件信息与最大熵**

- [定义 条件互信息及其链式法则](11-information.html#11-information-item-8)

- [定理 熵链式法则与条件化](11-information.html#11-information-item-9)

- [定理 最大熵与次可加性](11-information.html#11-information-item-10)

- [定理 固定均值的非负整数分布由几何分布最大化熵](11-information.html#11-information-item-11)

- [定理 Shearer 型三变量熵不等式](11-information.html#11-information-item-12)

- [例题 公平比特、异或与条件互信息](11-information.html#11-information-item-13)

**11.4 数据处理与分布距离**

- [定义 随机通道、Markov 关系与总变差](11-information.html#11-information-item-14)

- [定理 散度链式法则与数据处理](11-information.html#11-information-item-15)

- [定理 Pinsker 不等式](11-information.html#11-information-item-16)

- [定理 Pinsker 的二元微积分步骤](11-information.html#11-information-item-17)

### 12 · 集中不等式与大偏差

**12.1 尾事件与最少假设的界**

- [定义 偏差、尾概率与矩母函数](12-concentration.html#12-concentration-item-1)

- [定理 Markov 与 Chebyshev 不等式](12-concentration.html#12-concentration-item-2)

**12.2 指数方法：独立性带来指数衰减**

- [定义 指数倾斜与率函数](12-concentration.html#12-concentration-item-3)

- [引理 Hoeffding 引理的二阶导数证明](12-concentration.html#12-concentration-item-4)

- [定理 Chernoff 矩母函数界](12-concentration.html#12-concentration-item-5)

- [定理 Hoeffding 不等式](12-concentration.html#12-concentration-item-6)

- [定理 Bernoulli 的 KL 尾界](12-concentration.html#12-concentration-item-7)

- [定理 Bernoulli KL 界的优化过程](12-concentration.html#12-concentration-item-8)

- [定理 乘法型 Chernoff 界](12-concentration.html#12-concentration-item-9)

- [例题 从一次 Markov 到 Bernoulli 指数界](12-concentration.html#12-concentration-item-10)

- [例题 抛硬币偏差：比较 Chebyshev 与 Hoeffding](12-concentration.html#12-concentration-item-11)

**12.3 大数定律与收敛模式**

- [定义 收敛模式与大数定律的使用范围](12-concentration.html#12-concentration-item-12)

- [定理 弱大数定律](12-concentration.html#12-concentration-item-13)

**12.4 类型与大偏差：概率与计数相消**

- [定义 经验分布、类型类与离散网格](12-concentration.html#12-concentration-item-14)

- [定理 Stirling 公式与类型计数](12-concentration.html#12-concentration-item-15)

- [定理 类型方法为何出现相对熵](12-concentration.html#12-concentration-item-16)

- [定理 有限字母表的 Sanov 上界](12-concentration.html#12-concentration-item-17)

### 13 · 离散 Fourier 变换

**13.1 函数空间、复内积与单位根**

- [定义 复共轭、内积、正交与系数](13-fourier.html#13-fourier-item-1)

- [定义 循环群上的 DFT](13-fourier.html#13-fourier-item-2)

- [引理 单位根正交性](13-fourier.html#13-fourier-item-3)

**13.2 逆变换、能量与卷积**

- [定理 逆变换与 Parseval 的逐项消去](13-fourier.html#13-fourier-item-4)

- [定理 Parseval 与卷积定理](13-fourier.html#13-fourier-item-5)

- [定理 FFT 与多项式乘法](13-fourier.html#13-fourier-item-6)

- [例题 四点 DFT、逆变换与能量核对](13-fourier.html#13-fourier-item-7)

- [例题 循环卷积与零填充](13-fourier.html#13-fourier-item-8)

**13.3 有限群与布尔立方体**

- [定义 布尔编码、坐标翻转与噪声相关参数](13-fourier.html#13-fourier-item-9)

- [定义 有限 Abel 群的特征标](13-fourier.html#13-fourier-item-10)

- [定理 布尔立方体上的 Fourier 展开](13-fourier.html#13-fourier-item-11)

- [定理 布尔影响与噪声算子](13-fourier.html#13-fourier-item-12)

- [例题 二元布尔函数的展开、影响与噪声](13-fourier.html#13-fourier-item-13)

### 14 · 压缩与信道编码

**14.1 码字与解码：先明确模型**

- [定义 编码、唯一可译码与前缀码](14-coding.html#14-coding-item-1)

- [定理 Kraft–McMillan 不等式](14-coding.html#14-coding-item-2)

- [定理 McMillan 不等式的计数证明](14-coding.html#14-coding-item-3)

- [例题 单射并不保证串能唯一解码](14-coding.html#14-coding-item-4)

**14.2 无损变长压缩：熵界与 Huffman**

- [定理 无损编码的熵界](14-coding.html#14-coding-item-5)

- [定理 Huffman 最优性](14-coding.html#14-coding-item-6)

- [例题 Huffman 的构造与平均码长](14-coding.html#14-coding-item-7)

**14.3 块压缩、典型集与旁信息**

- [定义 块长、速率、错误概率与典型集](14-coding.html#14-coding-item-8)

- [定义 通用压缩与旁信息](14-coding.html#14-coding-item-9)

- [定理 AEP 与几乎无损压缩](14-coding.html#14-coding-item-10)

- [定理 典型集压缩的可达与逆向计数](14-coding.html#14-coding-item-11)

- [定理 Slepian–Wolf 双源速率区域](14-coding.html#14-coding-item-12)

**14.4 信道：容量与错误下界**

- [定义 信道码的消息、编码器和译码器](14-coding.html#14-coding-item-13)

- [定义 信道与容量](14-coding.html#14-coding-item-14)

- [定理 信道编码定理与 Fano 不等式](14-coding.html#14-coding-item-15)

- [例题 BSC、BEC 容量从互信息直接计算](14-coding.html#14-coding-item-16)

**14.5 距离、线性码与代数构造**

- [定义 Hamming 重量、生成矩阵、校验矩阵与伴随式](14-coding.html#14-coding-item-17)

- [定义 纠错码、距离与线性码](14-coding.html#14-coding-item-18)

- [定理 Hamming 界与 Singleton 界](14-coding.html#14-coding-item-19)

- [定理 随机线性码在 BEC 上的满秩概率](14-coding.html#14-coding-item-20)

- [定理 Reed–Solomon 码](14-coding.html#14-coding-item-21)

- [例题 重复码与随机线性码](14-coding.html#14-coding-item-22)

- [例题 Reed–Solomon 的插值恢复](14-coding.html#14-coding-item-23)

### 15 · 马尔可夫链与混合时间

**15.1 状态、Markov 性与矩阵演化**

- [定义 Markov 性、时齐与行随机矩阵](15-markov.html#15-markov-item-1)

- [定义 转移矩阵与分布演化](15-markov.html#15-markov-item-2)

**15.2 沟通、周期与稳态**

- [定义 可达、沟通类与闭类](15-markov.html#15-markov-item-3)

- [定义 不可约、周期与稳态](15-markov.html#15-markov-item-4)

- [定理 有限链稳态的存在性与不可约时的唯一性](15-markov.html#15-markov-item-5)

- [定理 有限链遍历定理](15-markov.html#15-markov-item-6)

- [例题 二状态链的精确收敛速度](15-markov.html#15-markov-item-7)

**15.3 到达时间、调和与具体随机游走**

- [定义 首达时间与首返时间](15-markov.html#15-markov-item-8)

- [定义 调和函数、吸收概率与 Dirichlet 问题](15-markov.html#15-markov-item-9)

- [定义 常返、暂留与平均返回时间](15-markov.html#15-markov-item-10)

- [例题 赌徒破产概率与平均停止时间](15-markov.html#15-markov-item-11)

- [例题 Birth–Death、Ehrenfest 与超立方体](15-markov.html#15-markov-item-12)

**15.4 可逆性与 MCMC**

- [定义 MCMC 与 Metropolis–Hastings](15-markov.html#15-markov-item-13)

- [定理 细致平衡与随机游走稳态](15-markov.html#15-markov-item-14)

- [例题 为什么随机游走的稳态按度分配](15-markov.html#15-markov-item-15)

**15.5 定量收敛：总变差、耦合与谱**

- [定义 耦合的边缘要求与同步之后的处理](15-markov.html#15-markov-item-16)

- [定义 总变差距离与混合时间](15-markov.html#15-markov-item-17)

- [引理 耦合不等式与最优耦合](15-markov.html#15-markov-item-18)

- [定理 耦合时间控制混合](15-markov.html#15-markov-item-19)

- [定理 可逆链的谱界](15-markov.html#15-markov-item-20)

- [例题 超立方体耦合的显式误差上界](15-markov.html#15-markov-item-21)

### 16 · 图论、平面图与谱图论

**16.1 图的对象与最基本的计数**

- [定义 顶点、边、简单图、多重图与同构](16-graphs.html#16-graphs-item-1)

- [定义 游走、迹、路径、圈与连通分量](16-graphs.html#16-graphs-item-2)

- [定义 图、度、路径与连通性](16-graphs.html#16-graphs-item-3)

- [定义 子图、诱导子图、补图与关联矩阵](16-graphs.html#16-graphs-item-4)

- [定理 握手引理与树的等价刻画](16-graphs.html#16-graphs-item-5)

**16.2 树：无圈与连通的平衡**

- [定义 树、森林、生成树与桥](16-graphs.html#16-graphs-item-6)

- [定理 树存在叶与基本刻画的归纳](16-graphs.html#16-graphs-item-7)

- [定理 Cayley 公式与 Prüfer 编码](16-graphs.html#16-graphs-item-8)

**16.3 矩阵与有向图**

- [定义 邻接矩阵、度矩阵与 Laplacian](16-graphs.html#16-graphs-item-9)

- [定义 有向图、DAG 与竞赛图](16-graphs.html#16-graphs-item-10)

- [定理 邻接矩阵、Laplacian 与游走](16-graphs.html#16-graphs-item-11)

- [定理 矩阵树定理](16-graphs.html#16-graphs-item-12)

- [定理 矩阵树定理的行列式展开](16-graphs.html#16-graphs-item-13)

- [例题 DAG 的拓扑序与路径计数](16-graphs.html#16-graphs-item-14)

**16.4 Euler 与 Hamilton：覆盖边还是顶点**

- [定义 Euler 迹、Euler 回路与 Hamilton 圈](16-graphs.html#16-graphs-item-15)

- [定理 Euler 与 Hamilton 的基本判据](16-graphs.html#16-graphs-item-16)

- [定理 Euler 回路的拼接算法](16-graphs.html#16-graphs-item-17)

- [定理 Hamilton 图的分量必要条件与 Ore 条件](16-graphs.html#16-graphs-item-18)

- [定理 Dirac 条件的最长路径证明](16-graphs.html#16-graphs-item-19)

**16.5 匹配、独立与顶点染色**

- [定义 最大与极大匹配、点覆盖与独立集](16-graphs.html#16-graphs-item-20)

- [定义 顶点染色与二分图](16-graphs.html#16-graphs-item-21)

- [定义 匹配、独立集、覆盖、团与染色](16-graphs.html#16-graphs-item-22)

- [定义 退化度与度序染色界](16-graphs.html#16-graphs-item-23)

- [定理 Hall 与 König 定理](16-graphs.html#16-graphs-item-24)

- [定理 Hall 与 König 的增广路证明](16-graphs.html#16-graphs-item-25)

- [定理 二分图与贪心染色](16-graphs.html#16-graphs-item-26)

- [定理 团、独立数与颜色类下界](16-graphs.html#16-graphs-item-27)

**16.6 平面性、面与对偶**

- [定义 可平面图、平面图、面与边界长度](16-graphs.html#16-graphs-item-28)

- [定义 平面对偶与曲面 Euler 示性数](16-graphs.html#16-graphs-item-29)

- [定理 Euler 平面公式与边数界](16-graphs.html#16-graphs-item-30)

- [定理 Kuratowski 与低度顶点](16-graphs.html#16-graphs-item-31)

- [定理 平面图五色定理](16-graphs.html#16-graphs-item-32)

- [定理 五色证明中 Kempe 链的换色细节](16-graphs.html#16-graphs-item-33)

- [例题 Euler 公式怎样排除 K₅ 与 K₃,₃](16-graphs.html#16-graphs-item-34)

**16.7 进一步的染色、连通与谱**

- [定义 特征值排序、正则图与谱间隙](16-graphs.html#16-graphs-item-35)

- [定义 块、点连通度与边连通度](16-graphs.html#16-graphs-item-36)

- [定义 扩张图与随机图谱的尺度](16-graphs.html#16-graphs-item-37)

- [定理 Brooks 与 Vizing：精确条件及证明层级](16-graphs.html#16-graphs-item-38)

- [定理 二分图的边色数等于最大度](16-graphs.html#16-graphs-item-39)

- [定理 删除—收缩与色多项式](16-graphs.html#16-graphs-item-40)

- [定理 规则图谱与扩张混合引理](16-graphs.html#16-graphs-item-41)

- [定理 谱半径、二分性与 Hoffman 界](16-graphs.html#16-graphs-item-42)

- [定理 Cheeger 不等式（归一化形式）](16-graphs.html#16-graphs-item-43)

### 17 · 概率方法

**17.1 概率存在性：定义坏事件再取期望**

- [定义 随机对象、坏事件与计数变量](17-method.html#17-method-item-1)

- [定理 第一矩方法与并集界](17-method.html#17-method-item-2)

- [定理 期望论证与条件期望法](17-method.html#17-method-item-3)

- [定理 Ramsey 数的概率下界](17-method.html#17-method-item-4)

- [例题 最大割与独立集](17-method.html#17-method-item-5)

**17.2 修补法与经典存在构造**

- [定义 Alteration：先随机再修补](17-method.html#17-method-item-6)

- [定理 高围长且高染色数的图存在](17-method.html#17-method-item-7)

- [定理 高围长、高染色数的定量修补](17-method.html#17-method-item-8)

- [定理 避免全一子矩阵的稠密矩阵](17-method.html#17-method-item-9)

- [定理 非零整数集合中的 sum-free 子集](17-method.html#17-method-item-10)

- [例题 随机竞赛图的支配性质](17-method.html#17-method-item-11)

**17.3 随机排列与极值集合论**

- [定义 集合族、反链与相交族](17-method.html#17-method-item-12)

- [定理 Erdős–Ko–Rado（均匀相交族）](17-method.html#17-method-item-13)

- [定理 Sperner 与 LYM 不等式](17-method.html#17-method-item-14)

- [定理 Bollobás 集合对不等式](17-method.html#17-method-item-15)

- [例题 随机排列为什么自然地产生 LYM 权重](17-method.html#17-method-item-16)

**17.4 二阶矩与随机阈值**

- [定义 随机图模型、阈值与尖锐阈值](17-method.html#17-method-item-17)

- [引理 第二矩下界的推导](17-method.html#17-method-item-18)

- [定理 第二矩方法与 Paley–Zygmund](17-method.html#17-method-item-19)

- [定理 二阶矩的方差判据](17-method.html#17-method-item-20)

- [定理 随机图的连通阈值](17-method.html#17-method-item-21)

- [定理 整数的不同素因子数的正常阶](17-method.html#17-method-item-22)

- [例题 第二矩方法证明三角形出现的阈值](17-method.html#17-method-item-23)

- [例题 随机图与 01 矩阵的共同方法](17-method.html#17-method-item-24)

**17.5 局部引理：利用稀疏依赖**

- [定义 依赖图与局部引理的使用清单](17-method.html#17-method-item-25)

- [定理 对称 Lovász 局部引理（补充工具）](17-method.html#17-method-item-26)

- [定理 一般 Lovász 局部引理的条件概率归纳](17-method.html#17-method-item-27)

- [例题 用局部引理给超图二染色](17-method.html#17-method-item-28)

### 21 · 线性规划、网络流与稳定匹配

**21.1 线性规划模型与对偶证书**

- [定义 可行、不可行、有界与最优值](21-optimization.html#21-optimization-item-1)

- [定义 线性规划、可行域与松弛变量](21-optimization.html#21-optimization-item-2)

- [定义 对偶问题与影子价格](21-optimization.html#21-optimization-item-3)

- [引理 Farkas 二择一定理](21-optimization.html#21-optimization-item-4)

- [定理 弱对偶与互补松弛](21-optimization.html#21-optimization-item-5)

- [定理 线性规划强对偶](21-optimization.html#21-optimization-item-6)

- [例题 不用枚举所有点也能证明最优](21-optimization.html#21-optimization-item-7)

**21.2 整数性与二分图匹配**

- [定义 极点、基本可行解与全幺模矩阵](21-optimization.html#21-optimization-item-8)

- [定理 TU 矩阵的整数性](21-optimization.html#21-optimization-item-9)

- [定理 有向关联矩阵与二分图关联矩阵为 TU](21-optimization.html#21-optimization-item-10)

- [定理 二分图匹配与覆盖的线性规划证明](21-optimization.html#21-optimization-item-11)

- [例题 三角形为什么破坏匹配松弛的整数性](21-optimization.html#21-optimization-item-12)

**21.3 网络流、割与路径**

- [定义 残量边与增广路径的两种操作](21-optimization.html#21-optimization-item-13)

- [定义 容量、可行流、流量与残量网络](21-optimization.html#21-optimization-item-14)

- [定理 最大流最小割与整数流](21-optimization.html#21-optimization-item-15)

- [定理 Menger 的边不交与点不交形式](21-optimization.html#21-optimization-item-16)

- [例题 匹配化成流：为什么会得到整数边选择](21-optimization.html#21-optimization-item-17)

**21.4 稳定匹配：偏好而非最大流量**

- [定义 偏好序、阻挡对与稳定性](21-optimization.html#21-optimization-item-18)

- [定理 Gale–Shapley 延迟接受算法](21-optimization.html#21-optimization-item-19)

- [定理 申请方最优性](21-optimization.html#21-optimization-item-20)

- [例题 延迟接受为何不能立即拒绝未来比较](21-optimization.html#21-optimization-item-21)

**21.5 匹配回到偏序与代表系**

- [定义 链、反链、宽度与高度](21-optimization.html#21-optimization-item-22)

- [定理 相异代表系的 Hall 条件](21-optimization.html#21-optimization-item-23)

- [定理 Dilworth 链分解定理](21-optimization.html#21-optimization-item-24)

- [定理 高度与反链划分的对偶结论](21-optimization.html#21-optimization-item-25)

### 22 · 渐近分析与估算工具

**22.1 渐近符号的量词**

- [定义 大 O、小 o、Θ、Ω 与 ω](22-asymptotics.html#22-asymptotics-item-1)

- [例题 用常数与阈值验证量词](22-asymptotics.html#22-asymptotics-item-2)

**22.2 增长层级、求和与误差**

- [引理 相乘相加的误差如何累计](22-asymptotics.html#22-asymptotics-item-3)

- [引理 指数近似的误差条件](22-asymptotics.html#22-asymptotics-item-4)

- [定理 常见增长层级](22-asymptotics.html#22-asymptotics-item-5)

- [定理 调和数与对数阶乘的积分估计](22-asymptotics.html#22-asymptotics-item-6)

**22.3 阶乘、组合数与概率应用**

- [定理 Stirling 公式与二项式系数的熵形式](22-asymptotics.html#22-asymptotics-item-7)

- [例题 从组合数估计判断概率趋零](22-asymptotics.html#22-asymptotics-item-8)

- [例题 递推复杂度与隐藏常数](22-asymptotics.html#22-asymptotics-item-9)
