---
dg-publish: true
---

O **método de Gauss-Seidel** é um método iterativo utilizado para resolver sistemas lineares do tipo:

$Ax = b$

Ele é uma melhoria do método de Jacobi, pois utiliza os valores mais recentes disponíveis para acelerar a convergência.

---

## Formulação

Dado um sistema com matriz A $\in \mathbb{R}^{n \times n}$, vetor b $\in \mathbb{R}^n$, e uma aproximação inicial $x^{(0)}$, o método atualiza cada componente da solução x segundo a fórmula:

$$
x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j=1}^{i-1} a_{ij} x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij} x_j^{(k)} \right)
$$

### Critério da Norma Linha (Norma ∞)

Esse critério é **matemático** e envolve a matriz de iteração T do método. Por exemplo, no Gauss-Jacobi:

$T = D^{-1}(L + U)$

Onde:

- D: diagonal da matriz A
- L: parte inferior de A (sem a diagonal)
- U: parte superior de A (sem a diagonal)

A **norma linha** (ou norma infinita) de uma matriz T é o **máximo das somas dos módulos dos elementos de cada linha**:

$$
\|T\|\infty = \max{1 \leq i \leq n} \sum_{j=1}^{n} |t_{ij}|
$$

### Convergência

Se $\|T\|_\infty < 1$, o Método Converge

---

### Exemplo (Critério da Norma Linha)

Considere o sistema:

$$
\begin{aligned} 4x_1 + x_2 + x_3 &= 7 \\ x_1 + 5x_2 + 2x_3 &= -8 \\ 2x_1 + 3x_2 + 10x_3 &= 6 \end{aligned}
$$

A matriz A é:

$$
A = \begin{bmatrix} 4 & 1 & 1 \\ 1 & 5 & 2 \\ 2 & 3 & 10 \end{bmatrix}
$$

Para o **Jacobi**, a matriz de iteração é $T = D^{-1}(L + U)$. Calculando isso (ou com código), você obterá algo como:

$$
T = \begin{bmatrix} 0 & -0.25 & -0.25 \\ -0.2 & 0 & -0.4 \\ -0.2 & -0.3 & 0 \end{bmatrix}
$$

Agora, calcule a soma dos módulos dos elementos de cada linha:

- linha 1: $|0| + |{-0.25}| + |{-0.25}| = 0.5$
- linha 2: $|{-0.2}| + |0| + |{-0.4}| = 0.6$
- linha 3: $|{-0.2}| + |{-0.3}| + |0| = 0.5$

**Maior valor**: $\|T\|_\infty = 0.6 < 1$

O método de Jacobi (e provavelmente o de Gauss-Seidel) converge.

---

## Critério de Sassenfeld

Esse critério é mais **fácil de aplicar manualmente** e muito útil, principalmente para o método de **Gauss-Seidel**.

Ele define uma sequência de valores $\beta_i$, onde:

$$
\beta_i = \frac{1}{|a_{ii}|} \left( \sum_{j=1}^{i-1} |a_{ij}| \beta_j + \sum_{j=i+1}^{n} |a_{ij}| \right)
$$

Você **usa os** $\beta$**’s anteriores** conforme vai calculando. É uma espécie de “feedback” para estimar o quanto cada linha depende das outras.

### Convergência

Se $\max(\beta_1, \dots, \beta_n) < 1$, o Método Converge

### Exemplo (Critério de Sassenfeld)

Use a mesma matriz A:

$$
A = \begin{bmatrix} 4 & 1 & 1 \\ 1 & 5 & 2 \\ 2 & 3 & 10 \end{bmatrix}
$$

Vamos calcular os $\beta_i$:

- $\beta_1 = \frac{1}{4} (|1| + |1|) = \frac{2}{4} = 0.5$
- $\beta_2 = \frac{1}{5} (|1| \cdot 0.5 + |2|) = \frac{1}{5}(0.5 + 2) = 0.5$
- $\beta_3 = \frac{1}{10} (|2| \cdot 0.5 + |3| \cdot 0.5) = \frac{1}{10}(1 + 1.5) = 0.25$

Logo:

$$
\max(\beta_1, \beta_2, \beta_3) = 0.5 < 1
$$

O método de Gauss-Seidel **converge**!
