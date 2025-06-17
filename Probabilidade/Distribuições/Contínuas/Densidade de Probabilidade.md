

A densidade de probabilidade é uma medida importante em teoria da probabilidade que descreve a distribuição de probabilidade de uma variável aleatória contínua. Ela fornece informações sobre a probabilidade de que a variável aleatória assuma valores dentro de um intervalo específico.

## Definição

A densidade de probabilidade de uma variável aleatória contínua X é definida como:

$$
f(x) = \frac{d}{dx} F(x)
$$

onde F(x) é a função de distribuição acumulada (FAD) da variável aleatória X.

## Exemplo

Suponha que tenhamos uma variável aleatória X que segue uma distribuição normal com média μ = 0 e desvio padrão σ = 1. A FAD dessa distribuição é dada por:

$$
F(x) = \frac{1}{2} \left[ 1 + \text{erf} \left( \frac{x}{\sqrt{2}} \right) \right]
$$

onde erf é a função de erro.

A densidade de probabilidade dessa distribuição é então:

$$
f(x) = \frac{d}{dx} F(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
$$

**Relação com Funções de Probabilidade**
--------------------------------------

A densidade de probabilidade está relacionada às funções de probabilidade (FP) por meio da seguinte equação:

$$
P(a \leq X \leq b) = \int_{a}^{b} f(x) dx
$$

onde P(a ≤ X ≤ b) é a probabilidade de que a variável aleatória X assuma valores entre a e b.

**Caso Discreto**
-----------------

No caso de uma variável aleatória discreta, a densidade de probabilidade não existe. Em vez disso, usamos as funções de probabilidade (FP) para descrever a distribuição da variável aleatória. A FP é definida como:

$$
P(X = x_i) = p_i
$$

onde x_i são os valores possíveis da variável aleatória e p_i são as probabilidades associadas a esses valores.

A densidade de probabilidade pode ser vista como uma generalização das funções de probabilidade para o caso contínuo. Ela fornece informações sobre a distribuição da variável aleatória em um intervalo específico, enquanto as FP descrevem a distribuição da variável aleatória nos valores discretos.