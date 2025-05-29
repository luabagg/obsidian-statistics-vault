---
dg-publish: true
---

A **distribuição de Bernoulli** é uma distribuição de probabilidade discreta que descreve experimentos com apenas dois resultados possíveis: sucesso ou fracasso. Um exemplo clássico é o lançamento de uma moeda, onde a face "cara" pode ser considerada um sucesso e a face "coroa" um fracasso.

- **Parâmetro**: A distribuição de Bernoulli é definida por um único parâmetro, que é a probabilidade de sucesso, denotado por $p$.
  - Se o experimento resultar em sucesso, a variável aleatória assume o valor 1.
  - Se o experimento resultar em fracasso, a variável aleatória assume o valor 0.
- **Função de Probabilidade**:
  $$

 P(X = k) = p^k (1-p)^{1-k}

$$
  
  onde $X$ é a variável aleatória e $k \in \{0, 1\}$.

- **Esperança**:
  
$$

 E[X] = p

$$
  
  A esperança de uma distribuição de Bernoulli é simplesmente a probabilidade de sucesso.

- **Variação**:
  
$$

 Var(X) = p(1-p)

$$
  
  A variação (ou variância) mede o desvio dos valores da variável aleatória em relação à sua esperança. Para uma distribuição de Bernoulli, a variação é dada pela expressão acima.

### Função de Distribuição de Probabilidade Múltipla (FGM)

A **Função de Distribuição de Probabilidade Múltipla** (FGM) é um conceito mais avançado que generaliza a distribuição binomial para múltiplos experimentos. É frequentemente usada em teoria estatística e probabilidade.

- **Definição**: A FGM é uma função que descreve a probabilidade conjunta de vários eventos ocorrendo simultaneamente.
  
  - Se $X_1, X_2, \ldots, X_n$ são variáveis aleatórias binomiais independentes, a FGM pode ser usada para calcular a probabilidade de um conjunto específico dessas variáveis ocorrerem.

- **Forma Geral**:
  
$$

 P(X_1 = x_1, X_2 = x_2, \ldots, X_n = x_n)

$$
  
  onde $x_i \in \{0, 1\}$.

### Esperança e Variação

- **Esperança**: A esperança é uma medida de localização que representa o valor médio esperado da variável aleatória. Para uma distribuição de Bernoulli, a esperança é $E[X] = p$. Em geral, para qualquer variável aleatória discreta $X$ com função de probabilidade $P(X = x_i) = p_i$, a esperança é dada por:
  
$$

 E[X] = \sum_{i} x_i p_i

$$
  
- **Variação**: A variação (ou variância) mede o desvio dos valores da variável aleatória em relação à sua esperança. Para uma distribuição de Bernoulli, a variação é $Var(X) = p(1-p)$. Em geral, para qualquer variável aleatória discreta $X$, a variação é dada por:
  
$$

 Var(X) = E[X^2] - (E[X])^2

$$
  
  onde $E[X^2] = \sum_{i} x_i^2 p_i$.

### Exemplo

Considere um experimento em que uma moeda justa é lançada duas vezes. A variável aleatória $X$ representa o número de caras obtidas.

- **Distribuição de Bernoulli**: Para cada lançamento, a distribuição de Bernoulli tem parâmetro $p = 0.5$.
  
- **FGM**: Se $X_1$ e $X_2$ representam os resultados dos dois lançamentos (cara ou coroa), a FGM pode ser usada para calcular a probabilidade conjunta de ambos os eventos ocorrerem.

- **Esperança e Variação**:
  - Esperança: $E[X] = 1 \cdot P(X=1) + 0 \cdot P(X=0) = p(1-p) + p^2 = 2p - p^2$
  - Variação: $Var(X) = (1-2p+p^2) - (2p-p^2)^2 = p(1-p)$
