---
dg-publish: true
---

Considere que vamos realizar ensaios independentes de Bernoulli até a ocorrência do primeiro sucesso. Cada ensaio é um experimento binomial, onde há apenas dois possíveis resultados: sucesso ou fracasso. A probabilidade de sucesso em cada ensaio é denotada por $p$, e consequentemente, a probabilidade de fracasso é $1 - p = q$.

## Distribuição Geométrica

A distribuição geométrica descreve o número de ensaios necessários para obter o primeiro sucesso. Seja $X$ a variável aleatória que representa o número de ensaios até o primeiro sucesso. A função de probabilidade da distribuição geométrica é dada por:

$$
P(X = k) = (1 - p)^{k-1}p, \quad k = 1, 2, 3, \ldots
$$

Onde:

- $k$ é o número de ensaios até o primeiro sucesso.
- $p$ é a probabilidade de sucesso em cada ensaio.

## Exemplo

Suponha que uma moeda justa seja lançada repetidamente até obter a primeira cabeça (sucesso). A probabilidade de obter uma cabeça ($p = 0.5$) e a probabilidade de obter uma coroa ($q = 0.5$) são iguais.

- A probabilidade de obter o primeiro sucesso no primeiro lançamento é:
$$
  P(X = 1) = (1 - 0.5)^{1-1} \cdot 0.5 = 0.5
$$
- A probabilidade de obter o primeiro sucesso no segundo lançamento é:
$$
  P(X = 2) = (1 - 0.5)^{2-1} \cdot 0.5 = 0.5^2 \cdot 0.5 = 0.25
$$

## Parâmetros e Propriedades

A distribuição geométrica é completamente determinada pelo único parâmetro $p$, que representa a probabilidade de sucesso em cada ensaio.

- **Esperança (Média):** A esperança da variável aleatória $X$ é:
$$
  E(X) = \frac{1}{p}
$$
- **Variação:** A variância da variável aleatória $X$ é:
$$
  Var(X) = \frac{q}{p^2} = \frac{1 - p}{p^2}
$$

## Aplicações Práticas

A distribuição geométrica tem diversas aplicações em problemas reais, como:

- **Probabilidade de obter o primeiro sucesso em experimentos repetidos:** Por exemplo, a probabilidade de um jogador de basquete marcar seu primeiro arremesso no jogo.
- **Tempo até a ocorrência do primeiro evento específico:** Como o tempo até que um cliente entre em uma loja após o início da operação.

## Cálculo da Esperança a Partir da Função Geradora de Momentos

A **função geradora de momentos (FGM)** de uma variável aleatória discreta $X$ é definida como:

$$
M_X(t) = E[e^{tX}]
$$

Para a distribuição geométrica, onde $X$ representa o número de ensaios até o primeiro sucesso, com $P(X = k) = (1 - p)^{k-1}p$, temos:

$$
M_X(t) = \sum_{k=1}^{\infty} e^{tk} (1 - p)^{k-1} p
$$

Essa soma pode ser manipulada como uma série geométrica. Reescrevendo:

$$
M_X(t) = p e^t \sum_{k=0}^{\infty} \left[(1 - p)e^t\right]^k = \frac{p e^t}{1 - (1 - p)e^t}, \quad \text{para } e^t < \frac{1}{1 - p}
$$

Para obter a esperança $E(X)$ a partir da FGM, basta derivar $M_X(t)$ em relação a $t$ e avaliar em $t = 0$:

$$
E(X) = M_X’(0)
$$

Calculando a derivada de $M_X(t)$:

Seja

$$
M_X(t) = \frac{p e^t}{1 - (1 - p)e^t}
$$

Derivando com a regra do quociente:

$$
M_X’(t) = \frac{[p e^t][1 - (1 - p)e^t] + [p e^t (1 - p) e^t]}{[1 - (1 - p)e^t]^2}
$$

Simplificando e substituindo $t = 0$:

$$
M_X’(0) = \frac{p}{(1 - (1 - p))^2} = \frac{p}{p^2} = \frac{1}{p}
$$

Portanto, como esperado:

$$
E(X) = \frac{1}{p}
$$

## Observações Finais

- A distribuição geométrica é **sem memória**, ou seja, a probabilidade de obter um sucesso nos próximos ensaios **não depende** de quantos fracassos já ocorreram. Formalmente:
$$
    P(X > m + n \mid X > m) = P(X > n)
$$
- Essa propriedade a torna especialmente útil em processos de **espera** e em **modelagens com tempo até o primeiro evento**, principalmente quando os eventos são independentes e ocorrem com a mesma probabilidade.
