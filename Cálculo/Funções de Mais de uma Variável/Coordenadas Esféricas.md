---
dg-publish: true
---

As coordenadas esféricas são um sistema de coordenadas que permite descrever pontos em um espaço tridimensional. Elas são particularmente úteis em problemas que envolvem objetos com simetria esférica, como esferas, cilindros e cones.

## Definição

Dado um ponto P no espaço 3D, as coordenadas esféricas (ρ, θ, φ) são definidas da seguinte forma:

* ρ (rho): é a distância do ponto P ao origem O.
* θ (theta): é o ângulo entre o raio OP e o eixo x positivo.
* φ (phi): é o ângulo entre o raio OP e o plano xy.

**Relação com as coordenadas cartesianas**

As coordenadas esféricas podem ser relacionadas às coordenadas cartesianas (x, y, z) da seguinte forma:

$$
\begin{align}
x &= \rho \sin \phi \cos \theta \\
y &= \rho \sin \phi \sin \theta \\
z &= \rho \cos \phi
\end{align}
$$

**Derivadas em coordenadas esféricas**

As derivadas em coordenadas esféricas são importantes para resolver problemas de cálculo. A seguir, estão as fórmulas para as derivadas parciais das funções em coordenadas esféricas:

* $\frac{\partial}{\partial \rho}$
* $\frac{\partial}{\partial \theta}$
* $\frac{\partial}{\partial \phi}$

$$
\begin{align}
\frac{\partial}{\partial \rho} &= \sin \phi \cos \theta \frac{\partial}{\partial x} + \sin \phi \sin \theta \frac{\partial}{\partial y} + \cos \phi \frac{\partial}{\partial z} \\
\frac{\partial}{\partial \theta} &= -\rho \sin \phi \sin \theta \frac{\partial}{\partial x} + \rho \sin \phi \cos \theta \frac{\partial}{\partial y} \\
\frac{\partial}{\partial \phi} &= \rho \cos \phi \cos \theta \frac{\partial}{\partial x} + \rho \cos \phi \sin \theta \frac{\partial}{\partial y} - \rho \sin \phi \frac{\partial}{\partial z}
\end{align}
$$

Essas fórmulas permitem calcular as derivadas parciais de funções em coordenadas esféricas, o que é útil para resolver problemas de cálculo em espaços tridimensionais.

## Variáveis

**Variável Reta ($\rho$)**

A variável reta $\rho$ representa a distância do ponto ao origem. Ela pode variar entre $0$ e $\infty$. A variação máxima de $\rho$ é, portanto, $\boxed{\infty}$.

**Variável Circular ($\theta$)**

A variável circular $\theta$ representa o ângulo formado com o eixo x positivo. Ela pode variar entre $0$ e $2\pi$. A variação máxima de $\theta$ é, portanto, $\boxed{2\pi}$.

**Variável Polar ($\phi$)**

A variável polar $\phi$ representa o ângulo formado com o plano xy. Ela pode variar entre $0$ e $\pi$. A variação máxima de $\phi$ é, portanto, $\boxed{\pi}$.

### Relação do Phi Constante com um Cone

Quando $\phi$ é constante, isso significa que o ponto está localizado em uma superfície circular centrada no origem. Essa superfície é, na verdade, um cone com a direção de seu eixo sendo a direção do vetor $\rho$. O ângulo entre o eixo x positivo e o eixo do cone é exatamente $\phi$, que é constante.

**Exemplo**

Considere um ponto $(\rho, \theta, \phi) = (3, \frac{\pi}{4}, \frac{\pi}{3})$. Nesse caso, a variável reta $\rho$ tem valor $3$, a variável circular $\theta$ tem valor $\frac{\pi}{4}$ e a variável polar $\phi$ é constante com valor $\frac{\pi}{3}$. Isso significa que o ponto está localizado em um cone com direção do eixo $(\frac{1}{2}, \frac{1}{2}, \frac{\sqrt{3}}{2})$, que forma um ângulo de $\frac{\pi}{3}$ com o eixo x positivo.
