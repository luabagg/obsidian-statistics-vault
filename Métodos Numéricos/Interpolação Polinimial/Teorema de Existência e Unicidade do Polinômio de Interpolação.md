---
dg-publish: true
---

## Definição e Contexto

O teorema de existência e unicidade do polinômio de interpolação é um resultado fundamental na teoria da interpolação numérica. Este teorema garante que, sob certas condições, existe exatamente um polinômio de grau $n$ que passa por $n+1$ pontos distintos no plano complexo.

### Notação e Suposições

Sejam $x_0, x_1, \ldots, x_n$ pontos distintos em $\mathbb{R}$ (ou $\mathbb{C}$) e $y_0, y_1, \ldots, y_n$ valores associados a esses pontos. O problema de interpolação consiste em encontrar um polinômio $P(x)$ de grau menor ou igual a $n$ que satisfaz as condições:

$$
P(x_i) = y_i, \quad i = 0, 1, \ldots, n.
$$

## Enunciado

Sejam dados $n+1$ pontos distintos $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n) \in \mathbb{R}^2$, com $x_i \ne x_j$ para $i \ne j$.

Então, existe **um único** polinômio $P \in \mathbb{R}[x]$, de grau no máximo $n$, tal que:

$$
P(x_i) = y_i \quad \text{para todo } i = 0, 1, \dots, n.
$$

**Demonstração**

**1. Unicidade**

Suponha que existam dois polinômios $P(x)$ e $Q(x)$ de grau $\le n$ tais que:

$$
P(x_i) = Q(x_i) = y_i \quad \text{para } i = 0, 1, \dots, n.
$$

Definimos $R(x) = P(x) - Q(x)$. Então:

- $R(x)$ é um polinômio de grau no máximo $n$,
- $R(x_i) = P(x_i) - Q(x_i) = 0$ para cada $i$.

Logo, $R(x)$ possui $n+1$ raízes **distintas**, pois os $x_i$ são distintos.

Mas, um polinômio de grau $\le n$ não pode ter mais que $n$ raízes distintas a menos que seja o polinômio nulo.

Portanto, $R(x) \equiv 0 \Rightarrow P(x) = Q(x)$.

**Conclusão:** o polinômio interpolador é único.

**2. Existência**

Vamos construir explicitamente esse polinômio usando a **fórmula de Lagrange**:

$$
P(x) = \sum_{i=0}^{n} y_i \cdot L_i(x)
$$

onde cada $L_i(x)$ é o **polinômio base de Lagrange**:

$$
L_i(x) = \prod_{\substack{j=0 \ j \ne i}}^{n} \frac{x - x_j}{x_i - x_j}
$$

Cada $L_i(x)$ satisfaz:

- $L_i(x_i) = 1$
- $L_i(x_j) = 0$ para $j \ne i$

Assim, substituindo $x = x_k$:

$$
P(x_k) = \sum_{i=0}^{n} y_i \cdot L_i(x_k) = y_k \cdot 1 + \sum_{i \ne k} y_i \cdot 0 = y_k
$$

Logo, $P(x_i) = y_i$ para todos os $i$.

Como $P(x)$ é combinação de polinômios de grau $n$, então $\deg P \le n$.

---

**Exemplo**

Sejam os pontos $(1, 2)$, $(2, 3)$ e $(4, 1)$.

Construímos os polinômios de Lagrange:

- $L_0(x) = \dfrac{(x - 2)(x - 4)}{(1 - 2)(1 - 4)} = \dfrac{(x - 2)(x - 4)}{3}$
- $L_1(x) = \dfrac{(x - 1)(x - 4)}{(2 - 1)(2 - 4)} = \dfrac{(x - 1)(x - 4)}{-2}$
- $L_2(x) = \dfrac{(x - 1)(x - 2)}{(4 - 1)(4 - 2)} = \dfrac{(x - 1)(x - 2)}{6}$

Logo,

$$
P(x) = 2 \cdot L_0(x) + 3 \cdot L_1(x) + 1 \cdot L_2(x)
$$

Esse polinômio é de grau $2$ e satisfaz $P(1) = 2$, $P(2) = 3$, $P(4) = 1$.
