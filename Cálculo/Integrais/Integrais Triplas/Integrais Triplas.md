---
dg-publish: true
---
%% Begin Waypoint %%

- [[Integrais Triplas]]

%% End Waypoint %%

## Introdução às Integrais Triplas

As integrais triplas são uma extensão natural das integrais duplas para o espaço tridimensional. Elas permitem a integração de funções de três variáveis sobre um volume no espaço $\mathbb{R}^3$. A integral tripla é representada por:

$$
\iiint_V f(x, y, z) \, dV
$$

onde $f(x, y, z)$ é uma função contínua em um domínio tridimensional $V$.

## Exemplos de Integrais Triplas

1. **Volume de um Sólido**: O volume de um sólido pode ser calculado usando a integral tripla da função constante 1 sobre o volume do sólido:

   $$
 
   V = \iiint_V 1 \, dV
   
$$

2. **Massa de um Sólido com Densidade Variável**: Se uma densidade $\rho(x, y, z)$ varia no espaço tridimensional, a massa total do sólido pode ser calculada pela integral tripla da função densidade:

   $$

   M = \iiint_V \rho(x, y, z) \, dV

$$

### Como Calcular Integrais Triplas

Para calcular uma integral tripla, é necessário definir os limites de integração. Isso pode ser feito em diferentes sistemas coordenados: cartesianos, cilíndricos ou esféricos.

1. **Coordenadas Cartesianas**: A integral tripla em coordenadas cartesianas é dada por:

   $$

   \iiint_V f(x, y, z) \, dx \, dy \, dz

$$

   onde os limites de integração são definidos pelo volume $V$.

2. **Coordenadas Cilíndricas**: Em coordenadas cilíndricas $(r, \theta, z)$, a integral tripla é:

   $$

   \iiint_V f(r, \theta, z) \, r \, dr \, d\theta \, dz

$$

3. **Coordenadas Esféricas**: Em coordenadas esféricas $(\rho, \phi, \theta)$, a integral tripla é:

   $$

   \iiint_V f(\rho, \phi, \theta) \, \rho^2 \sin(\phi) \, d\rho \, d\phi \, d\theta

$$

### Exemplo de Cálculo

Suponha que queremos calcular a integral tripla da função $f(x, y, z) = x + y + z$ sobre o cubo unitário $0 \leq x \leq 1$, $0 \leq y \leq 1$, e $0 \leq z \leq 1$. A integral é:

$$

\iiint_V (x + y + z) \, dx \, dy \, dz = \int_0^1 \int_0^1 \int_0^1 (x + y + z) \, dx \, dy \, dz

$$

Primeiro integramos em relação a $x$:

$$

\int_0^1 (x + y + z) \, dx = \left[ \frac{x^2}{2} + xy + xz \right]_0^1 = \frac{1}{2} + y + z

$$

Em seguida, integramos em relação a $y$:

$$

\int_0^1 \left( \frac{1}{2} + y + z \right) dy = \left[ \frac{y}{2} + \frac{y^2}{2} + yz \right]_0^1 = \frac{1}{2} + \frac{1}{2} + z = 1 + z

$$

Finalmente, integramos em relação a $z$:

$$

\int_0^1 (1 + z) dz = \left[ z + \frac{z^2}{2} \right]_0^1 = 1 + \frac{1}{2} = \frac{3}{2}

$$

Portanto, o valor da integral tripla é $\frac{3}{2}$.
