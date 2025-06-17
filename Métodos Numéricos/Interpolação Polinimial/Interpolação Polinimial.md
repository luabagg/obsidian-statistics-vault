---
dg-publish: true
---

%% Begin Waypoint %%
- **[[Interpolação Polinimial]]**
	- [[Polinômio de Lagrange]]
	- [[Polinômio de Newton]]
	- [[Teorema de Existência e Unicidade do Polinômio de Interpolação]]

%% End Waypoint %%

A **interpolação polinomial** é um método numérico fundamental usado para estimar valores intermediários entre pontos conhecidos. Ela envolve o uso de um polinômio que passa exatamente pelos pontos dados, permitindo a previsão de valores dentro do intervalo desses pontos.

## Definição e Contexto

A interpolação polinomial é uma técnica matemática que consiste em encontrar um polinômio $P(x)$ de grau $n$ ou menor que passa por $n+1$ pontos $(x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)$. O objetivo é estimar o valor do polinômio em um ponto $x$ dentro do intervalo dos pontos conhecidos.

## Formulando a Interpolação

A interpolação polinomial pode ser formulada usando diferentes métodos, como o método de Lagrange e o método de Newton.

### Método de Lagrange

O polinômio de interpolação de Lagrange é dado por:

$$
P(x) = \sum_{j=0}^{n} y_j L_j(x)
$$

onde $L_j(x)$ são os polinômios de Lagrange, definidos como:

$$
L_j(x) = \prod_{\substack{0 \leq m \leq n \\ m \neq j}} \frac{x - x_m}{x_j - x_m}
$$

### Método de Newton

O polinômio de interpolação de Newton é construído usando diferenças divididas. Ele pode ser escrito como:

$$
P(x) = a_0 + a_1 (x - x_0) + a_2 (x - x_0)(x - x_1) + \cdots + a_n (x - x_0)(x - x_1)\cdots(x - x_{n-1})
$$

onde os coeficientes $a_i$ são determinados a partir das diferenças divididas.

## Considerações e Limitações

Embora eficaz, a interpolação polinomial tem algumas limitações. Por exemplo, o uso de polinômios de alta ordem pode levar ao fenômeno conhecido como **oscilações de Runge**, onde o polinômio oscila muito entre os pontos de interpolação, especialmente em intervalos largos.
