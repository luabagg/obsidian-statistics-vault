---
dg-publish: true
---
A função de distribuição acumulada (CDF) para variáveis contínuas, como a normal, é uma ferramenta fundamental em estatística que permite determinar a probabilidade de uma variável aleatória contínua assumir valores menores ou iguais a um valor específico.

## Definição Formal

A CDF, denotada por $F(x)$, é definida como:

$$


F(x) = P(X \leq x)


$$

para todo $x \in \mathbb{R}$. Ela representa a probabilidade acumulada até o ponto $x$.

## Relação com a Função de Densidade de Probabilidade (PDF)

A CDF é obtida integrando a função densidade de probabilidade (PDF) da variável contínua do ponto negativo infinito ao ponto $x$:

$$


F(x) = \int_{-\infty}^{x} f(t) \, dt


$$

Onde $f(t)$ é a PDF.

## Caso da Distribuição Normal

Para a distribuição normal padrão ($N(\mu, \sigma^2)$), a CDF não possui uma expressão fechada simples. No entanto, ela pode ser calculada usando métodos numéricos ou referringindo-se à tabela de valores padronizados.

## Exemplo Prático

Considerando uma variável $X \sim N(8, 4)$, para calcular $P(X \leq 10)$:

$$


P(X \leq 10) = F(10)


$$

Isso pode ser determinado usando a CDF da distribuição normal, que geralmente é implementada em softwares estatísticos ou calculadoras.

## Características Importantes

- A CDF é uma função não-decrescente.
- Ela é contínua para variáveis contínuas.
- Valores da CDF variam de 0 a 1.

A CDF é essencial em aplicativos estatísticos, como testes de hipótese e cálculos de intervalos de confiança.
