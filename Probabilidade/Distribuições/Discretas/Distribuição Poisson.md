---
dg-publish: true
---

A **distribuição Poisson** é uma importante distribuição de probabilidade discreta que descreve o número de eventos ocorridos em um intervalo de tempo ou espaço, dado que esses eventos ocorrem com uma taxa constante e independentemente do tempo desde o último evento. Esta distribuição é frequentemente utilizada para modelar fenômenos como a chegada de clientes em um estabelecimento comercial, a ocorrência de defeitos em um processo industrial, ou até mesmo a quantidade de chuva caindo em uma área durante um determinado período.

## Definição e Parâmetros

A distribuição Poisson é definida por uma única parâmetro, que é a **taxa média** (ou taxa esperada) de ocorrência do evento no intervalo considerado. Denotamos esta taxa por $\lambda > 0$. A função de probabilidade da distribuição Poisson para um número inteiro $k \geq 0$ é dada pela expressão:

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

Aqui, $X$ representa a variável aleatória que segue a distribuição Poisson.

## Exemplos de Aplicações

1. **Chamadas Telefônicas em um Call Center**: Suponha que o número médio de chamadas telefônicas recebidas por minuto é $\lambda = 5$. A probabilidade de receber exatamente $k$ chamadas no próximo minuto pode ser calculada usando a distribuição Poisson.
2. **Defeitos em um Processo Industrial**: Considere que o número médio de defeitos em uma linha de produção por hora é $\lambda = 3$. A probabilidade de ocorrerem exatamente $k$ defeitos em uma hora pode ser determinada usando a distribuição Poisson.

## Função de Probabilidade

A função de probabilidade da distribuição Poisson é:

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

onde:

- $X$ é a variável aleatória que segue a distribuição Poisson.
- $\lambda > 0$ é a taxa média de ocorrência do evento no intervalo considerado.
- $k \geq 0$ é um número inteiro representando o número de eventos.

## Função de Distribuição Cumulativa

A função de distribuição cumulativa (FDC) da distribuição Poisson, que denotamos por $F(k)$, é a probabilidade de que o número de eventos seja menor ou igual a $k$:

$$
F(k) = P(X \leq k) = \sum_{i=0}^{k} \frac{\lambda^i e^{-\lambda}}{i!}
$$

## Exemplo de Cálculo

Suponha que $\lambda = 4$. A probabilidade de ocorrerem exatamente $3$ eventos (por exemplo, defeitos em uma linha de produção) é:

$$
P(X = 3) = \frac{4^3 e^{-4}}{3!} = \frac{64 e^{-4}}{6} \approx 0.1956
$$

## Média e Variância

A **média** (esperança matemática) da distribuição Poisson é igual ao seu parâmetro $\lambda$:

$$
E[X] = \lambda
$$

A **variação** (variância) também é igual a $\lambda$:

$$
\text{Var}(X) = \lambda
$$
