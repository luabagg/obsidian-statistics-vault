---
dg-publish: true
---

As coordenadas cilíndricas são um sistema de coordenadas ortogonais que estendem a ideia das coordenadas polares para três dimensões. Elas são úteis em situações onde a simetria do problema é melhor descrita em termos cíclicos, como em problemas de física e engenharia.

## Definição

Em um sistema de coordenadas cilíndricas $(r, \theta, z)$, cada ponto no espaço é especificado por três valores:

- **$r$**: A distância do ponto ao eixo $z$. É semelhante à coordenada radial em coordenadas polares.
- **$\theta$**: O ângulo entre o eixo $x$ positivo e a projeção do ponto no plano $xy$, medido em radianos. Geralmente, $\theta \in [0, 2\pi)$.
- **$z$**: A coordenada vertical, que é a mesma que na coordenada cartesiana.

## Relação com as Coordenadas Cartesianas

As coordenadas cilíndricas estão relacionadas às coordenadas cartesianas $(x, y, z)$ pelas seguintes equações:

$$
\begin{align*}
x &= r \cos(\theta) \\
y &= r \sin(\theta) \\
z &= z
\end{align*}
$$

Conversamente, as coordenadas cilíndricas podem ser expressas em termos de coordenadas cartesianas como:

$$
\begin{align*}
r &= \sqrt{x^2 + y^2} \\
\theta &= \arctan\left(\frac{y}{x}\right) \\
z &= z
\end{align*}
$$

## Aplicações Práticas

1. **Física**: Em problemas de física, as coordenadas cilíndricas são úteis para descrever sistemas com simetria axial, como em rotação ou fluxo de fluidos ao redor de um eixo.
2. **Engenharia**: Na engenharia mecânica, elas podem ser usadas para analisar estruturas cilíndricas, como tubos ou cilindros.
3. **Matemática Aplicada**: Em cálculos envolvendo integrais múltiplas em geometrias cilíndricas.

## Exemplo

Considere um ponto no espaço com coordenadas cartesianas $(x, y, z) = (2\sqrt{3}, 6, 4)$. Convertendo para coordenadas cilíndricas:

1. **$r$**:
   $$
   r = \sqrt{x^2 + y^2} = \sqrt{(2\sqrt{3})^2 + 6^2} = \sqrt{12 + 36} = \sqrt{48} = 4\sqrt{3}
   
$$
2. **$\theta$**:
   
$$

   \theta = \arctan\left(\frac{y}{x}\right) = \arctan\left(\frac{6}{2\sqrt{3}}\right) = \arctan(\sqrt{3}) = \frac{\pi}{3}

$$
3. **$z$**:
   
$$

   z = 4

$$
Portanto, as coordenadas cilíndricas do ponto são $(r, \theta, z) = (4\sqrt{3}, \frac{\pi}{3}, 4)$.

#### Derivadas Parciais e Gradiente

Em coordenadas cilíndricas, a forma das derivadas parciais é diferente daquela em coordenadas cartesianas. Por exemplo, o gradiente de uma função $f(r, \theta, z)$ é dado por:
$$

\nabla f = \frac{\partial f}{\partial r} \mathbf{e}_r + \frac{1}{r} \frac{\partial f}{\partial \theta} \mathbf{e}_{\theta} + \frac{\partial f}{\partial z} \mathbf{e}_z

$$

Onde $\mathbf{e}_r$, $\mathbf{e}_{\theta}$, e $\mathbf{e}_z$ são os vetores unitários na direção das coordenadas cilíndricas.
