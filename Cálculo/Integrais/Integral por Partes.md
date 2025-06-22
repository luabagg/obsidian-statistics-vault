---
dg-publish: true
---
A integral por partes é uma técnica utilizada para resolver integrais difíceis de calcular diretamente. Ela se baseia na regra do produto da derivada e é fundamental em muitas áreas da matemática.

## Regra Do Produto da Derivada

A regra do produto da derivada estabelece que, se $f(x)$ e $g(x)$ são funções contínuas no intervalo $[a,b]$, então:

$$
\frac{d}{dx} (f(x) \cdot g(x)) = f'(x) \cdot g(x) + f(x) \cdot g'(x)
$$

## Aplicação da Integral por Partes

A integral por partes é uma generalização da regra do produto da derivada para integrais. Ela estabelece que, se $f(x)$ e $g(x)$ são funções contínuas no intervalo $[a,b]$, então:

$$
\int f(x) \cdot g'(x) dx = F(x) \cdot G(x) - \int F'(x) \cdot G(x) dx
$$

onde $F(x)$ é a integral de $f(x)$ e $G(x)$ é a integral de $g(x)$.

## Exemplo

Considere o seguinte exemplo:

$$
\int x^2 \cdot e^{x^3} dx
$$

Aqui, podemos escolher $f(x) = x^2$ e $g(x) = e^{x^3}$. A integral de $f(x)$ é $F(x) = \frac{x^3}{3}$ e a integral de $g(x)$ é $G(x) = \frac{1}{3}e^{x^3}$.

Aplicando a fórmula da integral por partes, obtemos:

$$
\int x^2 \cdot e^{x^3} dx = \frac{x^3}{3} \cdot \frac{1}{3}e^{x^3} - \int \frac{3x^2}{3} \cdot \frac{1}{3}e^{x^3} dx
$$

Simplificando, obtemos:

$$
\int x^2 \cdot e^{x^3} dx = \frac{x^6}{27}e^{x^3} - \int xe^{x^3} dx
$$

Agora, podemos aplicar a fórmula da integral por partes novamente para resolver a integral restante.

