---
dg-publish: true
---

A **Distribuição Binomial Negativa** é uma generalização da [[Distribuição Geométrica]] e descreve o número de **fracassos** até a ocorrência do **$r$-ésimo sucesso** em uma sequência de **ensaios de Bernoulli independentes**, nos quais cada tentativa resulta em sucesso com probabilidade $p$ e fracasso com probabilidade $q = 1 - p$.

## Definição e Parâmetros

A variável aleatória $X \sim \text{Binomial Negativa}(r, p)$ representa o número de **fracassos** antes de ocorrer o $r$-ésimo sucesso. Os parâmetros da distribuição são:

- **$r$**: número de sucessos desejados (inteiro positivo).
- **$p$**: probabilidade de sucesso em cada ensaio ($0 < p \leq 1$).

A função de massa de probabilidade é dada por:

$$
P(X = k) = \binom{k + r - 1}{k} p^r (1 - p)^k, \quad k = 0, 1, 2, \ldots
$$

> Observação: Algumas fontes definem $X$ como o número **total de ensaios até o $r$-ésimo sucesso**. Neste caso, $X$ assume valores $r, r+1, r+2, \ldots$ e a função de probabilidade se adapta para refletir isso.

## Características e Propriedades

- **Independência:** Cada ensaio é realizado de forma independente.
- **Probabilidade constante:** A chance de sucesso $p$ permanece inalterada em todos os ensaios.
- **Número de sucessos fixo:** A experiência prossegue até que ocorra exatamente $r$ sucessos, independentemente do número de fracassos.
- **Esperança (Média):**
$$
    E(X) = r \cdot \frac{1 - p}{p}
$$
- **Variância:**
$$
    \text{Var}(X) = r \cdot \frac{1 - p}{p^2}
$$

## Exemplos

**Exemplo 1: Lançamento de Moeda**

Suponha que uma moeda justa ($p = 0.5$) seja lançada repetidamente até obter **3 caras**. A distribuição binomial negativa modela a quantidade de **coroas (fracassos)** antes de obter essas 3 caras ($r = 3$). Aqui, $X$ conta o número de fracassos antes do terceiro sucesso.

**Exemplo 2: Processo Industrial**

Em uma linha de produção, cada peça tem 10% de chance de ser defeituosa ($p = 0.1$ para o “sucesso” = peça defeituosa). Queremos saber quantas peças boas serão produzidas **antes** que se observe a terceira peça defeituosa ($r = 3$). A variável aleatória $X$ segue uma distribuição binomial negativa e representa o número de peças boas (fracassos) antes do terceiro defeito.

## Relações com Outras Distribuições

- **[[Distribuição Geométrica]]:** Caso especial da binomial negativa com $r = 1$, modelando o número de fracassos até o **primeiro sucesso**.
- **[[Distribuição Binomial]]:** Modela o número de sucessos em um número **fixo** de ensaios. A binomial negativa, por outro lado, fixa o número de sucessos e deixa variável o número de fracassos (ou tentativas).
