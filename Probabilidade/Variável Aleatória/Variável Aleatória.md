---
dg-publish: true
dg-show-local-graph: true
---

%% Begin Waypoint %%
- **[[Variável Aleatória]]**
	- [[Espaço de Probabilidade Produzido por Variável Aleatória]]
	- [[Esperança de uma Variável Aleatória]]
	- [[Funções de Variáveis Aleatórias]]
	- [[Funções Geradoras de Momento]]
	- [[Variância de uma Variável Aleatória]]
	- [[Variável Aleatória Contínua]]
	- [[Variável Aleatória Discreta]]
	- [[Variável Aleatória Mista]]

%% End Waypoint %%

## Introdução às Variáveis Aleatórias

As variáveis aleatórias são fundamentais na teoria da probabilidade e estatística, servindo como a ponte entre o mundo dos números determinísticos e o dos eventos incertos. Elas permitem modelar situações onde os resultados não são conhecidos com certeza antes de ocorrerem.

### Definição

Uma variável aleatória é uma função que associa um valor numérico a cada resultado possível em um espaço amostral $\Omega$. Em notação matemática, se $X$ for uma variável aleatória e $\omega \in \Omega$, então $X(\omega)$ representa o valor numérico associado ao resultado $\omega$.

### Exemplos

1. **Tirar um Dado**: Considere o espaço amostral $\Omega = \{1, 2, 3, 4, 5, 6\}$, onde cada número representa a face de um dado que pode aparecer ao lançá-lo. Se $X$ for a variável aleatória que representa o valor do resultado, então $X(\omega) = \omega$, para $\omega \in \Omega$. Por exemplo, se $\omega = 3$, então $X(3) = 3$.
2. **Tempo de Chegada**: Considere um sistema onde os clientes chegam a uma loja com tempos variáveis. Se $T$ for a variável aleatória que representa o tempo de chegada do próximo cliente, então $T(\omega)$ pode assumir qualquer valor numérico positivo dependendo da situação.
3. **Temperatura**: Suponha que estamos interessados na temperatura diária em um determinado local. Se $Y$ for a variável aleatória que representa a temperatura no dia $\omega$, então $Y(\omega)$ pode assumir qualquer valor numérico dentro de uma faixa específica, dependendo das condições climáticas.

### Tipos de Variáveis Aleatórias

- **Discretas**: Têm um número contável de valores possíveis. Por exemplo, o número de carros vendidos em um dia.
$$
X(\omega) = \begin{cases}

  0 & \text{se não vendeu nenhum carro} \\

  1 & \text{se vendeu um carro} \\

  2 & \text{se vendeu dois carros} \\

  \vdots

  \end{cases}
$$
- **Contínuas**: Podem assumir qualquer valor numérico dentro de um intervalo. Por exemplo, a altura de uma pessoa.
$$
Y(\omega) = \text{altura da pessoa em metros}
$$

### Função de Distribuição Acumulada (FDA)

A função de distribuição acumulada $F_X(x)$ de uma variável aleatória discreta $X$ é definida como:

$$
F_X(x) = P(X \leq x)
$$

Para a variável aleatória contínua $Y$, a FDA é dada por:

$$
F_Y(y) = P(Y \leq y)
$$

Essa função descreve a probabilidade de que o valor da variável aleatória seja menor ou igual a um certo ponto.

### Esperança e Variância

- **Esperança**: É a média esperada dos valores que uma variável aleatória pode assumir. Para uma variável discreta $X$, é dada por:
$$
E[X] = \sum_{x} x \cdot P(X = x)
$$

  Para uma variável contínua $Y$, é dada por:

$$
E[Y] = \int_{-\infty}^{\infty} y \cdot f_Y(y) \, dy
$$
- **Variância**: Mede a dispersão dos valores em torno da média. É definida como o quadrado da desvio padrão e para uma variável discreta $X$ é:
$$
\text{Var}(X) = E[(X - E[X])^2] = \sum_{x} (x - E[X])^2 \cdot P(X = x)
$$

  Para uma variável contínua $Y$, a variância é:

$$
\text{Var}(Y) = E[(Y - E[Y])^2] = \int_{-\infty}^{\infty} (y - E[Y])^2 \cdot f_Y(y) \, dy
$$

Essas medidas são essenciais para entender e quantificar a tendência central e a dispersão dos dados associados às variáveis aleatórias.
