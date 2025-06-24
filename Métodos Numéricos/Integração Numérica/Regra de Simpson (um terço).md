---
dg-publish: true
---
A regra de Simpson de um terço é uma técnica numérica utilizada para aproximar integrais. Ela é baseada na ideia de dividir o intervalo de integração em três partes iguais e usar uma combinação de pontos finais e médios para calcular a integral.

## Formula

A fórmula da regra de Simpson de um terço é dada por:

$$
\int_{a}^{b} f(x) dx \approx \frac{h}{3} \left[ f(a) + 4f\left(\frac{a+b}{2}\right) + f(b) \right]
$$

onde $h = \frac{b-a}{3}$ é a largura da subintervala.

## Exemplo

Suponha que desejamos calcular a integral de $f(x) = x^2$ entre os limites $a=0$ e $b=1$. Usando a regra de Simpson de um terço, temos:

$$
\int_{0}^{1} x^2 dx \approx \frac{h}{3} \left[ f(0) + 4f\left(\frac{0+1}{2}\right) + f(1) \right]
$$

$$
= \frac{\frac{1-0}{3}}{3} \left[ 0^2 + 4\left(\frac{1}{2}\right)^2 + 1^2 \right]
$$

$$
= \frac{1}{9} \left[ 0 + 4\left(\frac{1}{4}\right) + 1 \right]
$$

$$
= \frac{1}{9} \left[ \frac{1}{1} + 1 \right]
$$

$$
= \frac{2}{9}
$$

## Observações

* A regra de Simpson de um terço é uma técnica numérica que pode ser usada para aproximar integrais.
* Ela é baseada na ideia de dividir o intervalo de integração em três partes iguais e usar uma combinação de pontos finais e médios para calcular a integral.
* A fórmula da regra de Simpson de um terço é dada por $\frac{h}{3} \left[ f(a) + 4f\left(\frac{a+b}{2}\right) + f(b) \right]$.
* A regra de Simpson de um terço pode ser usada para calcular integrais de funções polinomiais.
