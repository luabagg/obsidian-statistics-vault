---
dg-publish: true
---

A distribuição hipergeométrica é uma distribuição de probabilidade discreta que descreve o número de sucessos em um conjunto finito de experimentos sem reposição. É frequentemente usada quando se tem um total fixo de itens e se deseja saber a probabilidade de obter um certo número desses itens.

## Definição

Considere um conjunto com $N$ elementos, onde $K$ são considerados "sucessos" (ou itens desejados) e $N - K$ são "fracassos". Se realizarmos uma amostragem sem reposição de tamanho $n$, a distribuição hipergeométrica fornece a probabilidade de obter exatamente $k$ sucessos.

## Fórmula

A função de probabilidade da distribuição hipergeométrica é dada por:

$$
P(X = k) = \frac{\binom{K}{k} \binom{N-K}{n-k}}{\binom{N}{n}}
$$

onde:

- $X$ é a variável aleatória que representa o número de sucessos.
- $N$ é o tamanho total da população.
- $K$ é o número de itens desejados na população.
- $n$ é o tamanho da amostra.
- $k$ é o número de sucessos observado.

## Exemplo

Suponha que temos uma urna com 50 bolas, sendo 20 vermelhas (sucessos) e 30 brancas (fracassos). Se tirarmos uma amostra de tamanho 10 sem reposição, qual é a probabilidade de obtermos exatamente 4 bolas vermelhas?

- $N = 50$
- $K = 20$
- $n = 10$
- $k = 4$

A probabilidade é calculada como:

$$
P(X = 4) = \frac{\binom{20}{4} \binom{30}{6}}{\binom{50}{10}}
$$

## Características Principais

1. **Sem Reposição**: A amostragem é feita sem reposição, o que significa que uma vez que um item é selecionado, ele não pode ser escolhido novamente.
2. **População Finita**: O tamanho da população $N$ é finito e conhecido.
3. **Sucessos e Fracassos**: A amostragem envolve apenas dois tipos de resultados: sucessos (desejados) e fracassos (não desejados).

## Aplicações

A distribuição hipergeométrica tem várias aplicações práticas, como:

- **Estatística Médica**: Avaliar a probabilidade de encontrar um certo número de pacientes com uma certa condição em um estudo.
- **Estatística Industrial**: Verificar a qualidade de lotes de produtos.
- **Ciência da Computação**: Análise de amostras em bancos de dados.
