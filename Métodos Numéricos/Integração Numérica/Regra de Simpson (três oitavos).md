---
dg-publish: true
---
## Regra de Simpson de Três Oitavos

A regra de Simpson de três oitavos é uma fórmula numérica para aproximar a integral de uma função. Ela é usada quando não é possível encontrar a integral exata ou quando a função é complexa.

### Fórmula

$$
\int_{a}^{b} f(x) dx \approx \frac{h}{3} \left[ (y_0 + y_n) + 4(y_1 + y_2 + ... + y_{n-1}) \right]
$$

onde:

* $h = \frac{b-a}{n}$ é a largura da subintervalo
* $n$ é o número de subintervalos
* $y_i = f(x_i)$, onde $x_i = a + ih$

### Exemplo

Suponha que desejamos encontrar a integral de $f(x) = x^2$ entre 0 e 4. Se dividirmos o intervalo em 4 subintervalos iguais, teremos:

| $x_i$ | $y_i = f(x_i)$ |
| --- | --- |
| 0   | 0             |
| 1   | 1             |
| 2   | 4             |
| 3   | 9             |
| 4   | 16            |

Agora, podemos aplicar a regra de Simpson de três oitavos:

$$
\int_{0}^{4} x^2 dx \approx \frac{1}{3} \left[ (0 + 16) + 4(1 + 4 + 9) \right]
$$

$$
= \frac{1}{3} \left[ 16 + 4(14) \right]
$$

$$
= \frac{1}{3} \left[ 16 + 56 \right]
$$

$$
= \frac{72}{3}
$$

$$
= 24
$$

A integral exata é $\frac{x^3}{3}$ entre 0 e 4, que é igual a 64/3. A regra de Simpson de três oitavos nos deu uma aproximação de 24, que está longe da resposta correta.

### Observações

* A regra de Simpson de três oitavos é mais precisa do que a regra de Simpson de um terço, mas menos precisa do que a regra de Simpson de dois terços.
* Ela é usada quando não é possível encontrar a integral exata ou quando a função é complexa.
* A precisão da regra depende do número de subintervalos e da escolha dos pontos de divisão.
