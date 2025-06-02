---
dg-publish: true
---

## Ajuste de Curvas - Método dos Mínimos Quadrados

O **método dos mínimos quadrados** é utilizado para encontrar uma função que melhor se ajusta a um conjunto de dados, minimizando o erro quadrático entre os valores observados e os valores estimados pela função.

É muito utilizado quando queremos ajustar uma curva (reta, parábola, exponencial etc.) a um conjunto de pontos experimentais.

### Objetivo

Dado um conjunto de pontos $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$, encontrar uma função $f(x)$, dentro de uma família específica (por exemplo, uma reta $f(x) = a + bx$), que minimize o **erro quadrático total**:

$$
E(a, b, \dots) = \sum_{i=1}^n [y_i - f(x_i)]^2
$$

### Caso Mais Comum: Ajuste de Uma Reta ($f(x) = a + bx$)

Queremos encontrar os coeficientes $a$ e $b$ que minimizam:

$$
E(a, b) = \sum_{i=1}^n [y_i - (a + b x_i)]^2
$$

#### Derivando o Erro em Relação a $a$ e $b$ e Igualando a Zero (condição de mínimo), Obtemos um Sistema

$$
\begin{cases}

n a + b \sum x_i = \sum y_i \\

a \sum x_i + b \sum x_i^2 = \sum x_i y_i

\end{cases}
$$

Esse sistema pode ser resolvido por substituição, eliminação ou matriz.

### Forma Matricial Do Sistema

Escrevendo o sistema linear como:

$$
\begin{pmatrix}
n & \sum x_i \\
\sum x_i & \sum x_i^2
\end{pmatrix}
\begin{pmatrix}
a \\
b
\end{pmatrix}
=
\begin{pmatrix}
\sum y_i \\
\sum x_i y_i
\end{pmatrix}
$$

### Exemplo Numérico

Dado os pontos:

| $x$ | $y$ |
| --- | --- |
| 1   | 2   |
| 2   | 3   |
| 3   | 5   |
| 4   | 4   |

Calculamos:

- $n = 4$
- $\sum x_i = 1 + 2 + 3 + 4 = 10$
- $\sum y_i = 2 + 3 + 5 + 4 = 14$
- $\sum x_i^2 = 1^2 + 2^2 + 3^2 + 4^2 = 30$
- $\sum x_i y_i = 1\cdot2 + 2\cdot3 + 3\cdot5 + 4\cdot4 = 2 + 6 + 15 + 16 = 39$

Montamos o sistema:

$$
\begin{pmatrix}
4 & 10 \\
10 & 30
\end{pmatrix}
\begin{pmatrix}
a \\
b
\end{pmatrix}
=
\begin{pmatrix}
14 \\
39
\end{pmatrix}
$$

#### Resolvendo

Multiplicamos a primeira equação por 3:

- $12a +

## Arquivo Extra

![[Ajuste de Curvas - Quadrados Mínimos.pdf]]
