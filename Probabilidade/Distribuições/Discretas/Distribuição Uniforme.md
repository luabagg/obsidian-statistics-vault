---
dg-publish: true
---

A **distribuição uniforme** é uma das distribuições de probabilidade mais simples. Ela descreve um cenário onde cada valor dentro de um intervalo específico tem a mesma probabilidade de ocorrer.

## Casos Discretos

- **Definição**: Em casos discretos, a distribuição uniforme se aplica quando há um conjunto finito e igualmente provável de resultados. Por exemplo, o lançamento de um dado justo (6 faces) é um caso clássico.
  - **Exemplo**:
    $$

    P(X = x_i) = \frac{1}{n}
    
$$
    onde $n$ é o número total de possíveis resultados e $x_i$ representa cada resultado possível.

- **Características**:
  - Todos os valores possíveis têm a mesma probabilidade.
  - A função de probabilidade é constante entre os limites do intervalo.

### Casos Continuos

- **Definição**: Em casos continuos, a distribuição uniforme se aplica quando o valor pode assumir qualquer número dentro de um intervalo. Por exemplo, o tempo que uma pessoa passa em uma fila no supermercado pode ser modelado por uma distribuição uniforme.
  - **Exemplo**:
    
$$
    f(x) = 
    \begin{cases} 
    \frac{1}{b-a} & \text{para } a \leq x \leq b \\
    0 & \text{caso contrário}
    \end{cases}
    
$$
    onde $a$ e $b$ são os limites inferiores e superiores do intervalo, respectivamente.

- **Características**:
  - A função densidade de probabilidade é constante entre $a$ e $b$.
  - A área sob a curva da função densidade de probabilidade é igual a 1.

## Exemplos

### Caso Discreto

Suponha que um dado justo seja lançado. Cada face tem uma probabilidade uniforme de $\frac{1}{6}$.
$$

P(X = 1) = P(X = 2) = P(X = 3) = P(X = 4) = P(X = 5) = P(X = 6) = \frac{1}{6}

$$
### Caso Contínuo

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
