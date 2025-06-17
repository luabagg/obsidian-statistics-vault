---
dg-publish: true
---

A distribuição uniforme é uma distribuição de probabilidade contínua onde todos os valores em um intervalo $[a, b]$ têm a mesma probabilidade de ocorrer.

## Função de Densidade (FDP)

A função de densidade de probabilidade é dada por:

$$
f(x) = \begin{cases} 
\frac{1}{b - a} & \text{se } a \leq x \leq b \\
0 & \text{caso contrário}
\end{cases}
$$

Essa função é constante no intervalo $[a, b]$, indicando que a probabilidade é uniformemente distribuída.

## Função Acumulada (FDA)

A função de distribuição acumulada é definida como:

$$
F(x) = \begin{cases} 
0 & \text{se } x < a \\
\frac{x - a}{b - a} & \text{se } a \leq x \leq b \\
1 & \text{se } x > b
\end{cases}
$$

A CDF representa a probabilidade de que a variável aleatória $X$ seja menor ou igual a $x$, aumentando linearmente de 0 a 1 no intervalo $[a, b]$.

## Exemplos

Considere o tempo $T$ que uma pessoa passa em uma fila, onde $T$ pode variar entre 0 e 30 minutos. A função densidade de probabilidade seria:

$$
f(t) =
\begin{cases}
\frac{1}{30-0} & \text{para } 0 \leq t \leq 30 \\
0 & \text{caso contrário}
\end{cases}
=

\begin{cases}

\frac{1}{30} & \text{para } 0 \leq t \leq 30 \\

0 & \text{caso contrário}

\end{cases}
$$
