---
dg-publish: true
---

## Introdução

Integrais duplas em coordenadas polares são uma ferramenta poderosa para calcular áreas, volumes, e integrais de funções bidimensionais ou tridimensionais que têm simetria circular. As coordenadas polares consistem em um ponto no plano definido por um ângulo $\theta$ e uma distância $r$ do origem (polar), em vez das coordenadas retangulares $(x, y)$.

## Transformação de Coordenadas

A transformação entre as coordenadas retangulares $(x, y)$ e polares $(r, \theta)$ é dada por:

$$
x = r \cos(\theta)
$$

$$
y = r \sin(\theta)
$$

A área diferencial em coordenadas polares é dado por $dA = r \, dr \, d\theta$. Isso se deve ao fato de que a área de um pequeno círculo em coordenadas polares é aproximadamente igual à área do retângulo formado pelas diferenças nas coordenadas.

## Integrais Duplas

Para calcular uma integral dupla em coordenadas polares, primeiro expressamos a função $f(x, y)$ em termos de $r$ e $\theta$. Em seguida, substituímos as transformações de coordenadas na integral. A forma geral da integral dupla em coordenadas polares é:

$$
\iint_R f(x,y) \, dA = \iint_{R'} f(r \cos(\theta), r \sin(\theta)) \cdot r \, dr \, d\theta
$$

onde $R$ é a região no plano cartesiano e $R'$ é a correspondente região em coordenadas polares.

## Exemplo: Integral Dupla de Uma Função Simples

Considere a função $f(x,y) = x^2 + y^2$. Em coordenadas polares, esta se transforma em:

$$
f(r \cos(\theta), r \sin(\theta)) = (r \cos(\theta))^2 + (r \sin(\theta))^2 = r^2
$$

A integral dupla sobre uma região circular de raio $R$ centrada na origem é:

$$
\iint_R (x^2 + y^2) \, dA = \int_0^{2\pi} \int_0^R r^2 \cdot r \, dr \, d\theta = \int_0^{2\pi} \int_0^R r^3 \, dr \, d\theta
$$

Calculando a integral interna primeiro:

$$
\int_0^R r^3 \, dr = \left[ \frac{r^4}{4} \right]_0^R = \frac{R^4}{4}
$$

Então a integral externa é:

$$
\int_0^{2\pi} \frac{R^4}{4} \, d\theta = \frac{R^4}{4} \left[ \theta \right]_0^{2\pi} = \frac{\pi R^4}{2}
$$

## Retângulo Polar

Um "retângulo polar" é uma região no plano polares definida por um intervalo de $\theta$ e $r$. Por exemplo, o retângulo polar pode ser definido como:

$$
a \leq r \leq b, \quad c \leq \theta \leq d
$$

A área deste retângulo é calculada multiplicando a diferença entre os limites de $r$ e $\theta$ por $r$, conforme mencionado anteriormente.

## Aplicações Práticas

Integrais duplas em coordenadas polares são úteis para problemas com simetria circular, como cálculos de momentos de inércia ou áreas de regiões circulares. Por exemplo, a área de um círculo de raio $R$ pode ser calculada facilmente usando integrais polares:

$$
A = \int_0^{2\pi} \int_0^R r \, dr \, d\theta = 2\pi R^2
$$
