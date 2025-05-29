---
dg-publish: true
---

A **distribuição binomial** é um conceito fundamental na teoria das probabilidades, utilizado para modelar experimentos aleatórios com duas possíveis saídas: sucesso ou fracasso. Este modelo é amplamente aplicado em diversas áreas, como estatística, ciências sociais e engenharia.

## Definição Formal

Seja $X$ uma variável aleatória que representa o número de sucessos em $n$ experimentos independentes. Se a probabilidade de sucesso em cada experimento é $p$, então $X$ segue uma distribuição binomial com parâmetros $n$ e $p$. Isto é, $X \sim B(n, p)$.

A função de probabilidade da variável aleatória $X$ é dada por:

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

onde:

- $\binom{n}{k}$ é o coeficiente binomial, que representa o número de maneiras de escolher $k$ sucessos em $n$ tentativas.
- $p$ é a probabilidade de sucesso em cada tentativa.
- $1-p$ é a probabilidade de fracasso.

## Características Principais

1. **Experimento Independente**: Cada tentativa do experimento é independente das outras. O resultado de uma tentativa não afeta o resultado das demais.
2. **Dois Únicos Resultados Possíveis**: Em cada tentativa, há apenas dois resultados possíveis: sucesso (com probabilidade $p$) ou fracasso (com probabilidade $q = 1 - p$).
3. **Número Fixo de Tentativas**: O experimento é composto por um número fixo $n$ de tentativas.

## Exemplo de Cálculo

Suponha que uma moeda justa seja lançada 5 vezes e queremos calcular a probabilidade de obter exatamente 3 caras. Aqui, $n = 5$, $k = 3$ e $p = 0.5$.

A probabilidade é calculada como:

$$
P(X = 3) = \binom{5}{3} (0.5)^3 (1-0.5)^{5-3}
$$

Calculando o coeficiente binomial:

$$
\binom{5}{3} = \frac{5!}{3!(5-3)!} = 10
$$

Então, a probabilidade é:

$$
P(X = 3) = 10 \cdot (0.5)^3 \cdot (0.5)^2 = 10 \cdot 0.125 \cdot 0.25 = 0.3125
$$

Portanto, a probabilidade de obter exatamente 3 caras em 5 lançamentos é $0.3125$.

## Propriedades

- **Esperança (E(X))**: A esperança da variável binomial $X$ é dada por:
$$
 E(X) = np
$$

  Isso significa que, no longo prazo, a média dos resultados de $n$ tentativas será aproximadamente igual a $np$.

- **Variância (Var(x))**: A variância da variável binomial $X$ é dada por:
$$
 Var(X) = np(1-p)
$$

  Isso indica que a dispersão dos resultados em torno da média diminui à medida que $n$ aumenta, mas o efeito de $p$ (probabilidade de sucesso) também deve ser considerado.

- **Momento Gerador (Mx(t))**: A função geradora de momentos da variável binomial $X$ é dada por:
$$
 M_X(t) = (1-p + pe^t)^n
$$

  Esta função pode ser usada para calcular outros momentos estatísticos, como a esperança e a variância.

## Aplicações Práticas

A distribuição binomial tem diversas aplicações práticas. Por exemplo:

- **Estatística Médica**: Para avaliar a eficácia de um medicamento em uma amostra de pacientes.
- **Ciências Sociais**: Para estudar comportamentos sociais, como o voto em eleições.
- **Engenharia de Qualidade**: Para controlar a qualidade de produtos em uma linha de produção.
