---
dg-publish: true
---

## Valores Máximos e Mínimos de Funções de Duas Variáveis

Para entender os valores extremos (máximos e mínimos) de uma função de duas variáveis, consideremos a função $f(x, y)$.

### Pontos Críticos

Os pontos críticos são aqueles onde as derivadas parciais primeiras da função são nulas. Portanto, devemos resolver o sistema:

$$
\begin{cases}
\dfrac{\partial f}{\partial x} = 0 \\
\dfrac{\partial f}{\partial y} = 0
\end{cases}
$$

### Teste da Segunda Derivada

Para determinar se um ponto crítico $(x_0, y_0)$ é um máximo, mínimo ou ponto de sela, usamos o teste da segunda derivada. Definimos a matriz Hessiana $H$ como:

$$
H = \begin{pmatrix}
\dfrac{\partial^2 f}{\partial x^2} & \dfrac{\partial^2 f}{\partial x \partial y} \\
\dfrac{\partial^2 f}{\partial y \partial x} & \dfrac{\partial^2 f}{\partial y^2}
\end{pmatrix}
$$

A matriz Hessiana é simétrica, então podemos usar o determinante e a egunda derivada parcialpara classificar os pontos críticos:

1. **Determinante da Matriz Hessiana:**
$$
 D = \det(H) = \left( \dfrac{\partial^2 f}{\partial x^2} \right) \left( \dfrac{\partial^2 f}{\partial y^2} \right) - \left( \dfrac{\partial^2 f}{\partial x \partial y} \right)^2
$$
2. **Classificação:**
   - Se $D > 0$ e $\dfrac{\partial^2 f}{\partial x^2} > 0$, então $(x_0, y_0)$ é um mínimo local.
   - Se $D > 0$ e $\dfrac{\partial^2 f}{\partial x^2} < 0$, então $(x_0, y_0)$ é um máximo local.
   - Se $D < 0$, então $(x_0, y_0)$ é um ponto de sela.
   - Se $D = 0$, o teste é inconclusivo.

### Exemplo

Considere a função:

$$
 f(x, y) = x^2 + y^2 - 2x - 4y + 1
$$
1. **Encontrar os pontos críticos:**
$$
   \begin{cases}

   \dfrac{\partial f}{\partial x} = 2x - 2 = 0 \\

   \dfrac{\partial f}{\partial y} = 2y - 4 = 0

   \end{cases}
$$

   Resolvendo, obtemos $(1, 2)$.

2. **Matriz Hessiana:**
$$
   H = \begin{pmatrix}

   \dfrac{\partial^2 f}{\partial x^2} & \dfrac{\partial^2 f}{\partial x \partial y} \\

   \dfrac{\partial^2 f}{\partial y \partial x} & \dfrac{\partial^2 f}{\partial y^2}

   \end{pmatrix} = \begin{pmatrix}

   2 & 0 \\

   0 & 2

   \end{pmatrix}
$$
3. **Determinante da Matriz Hessiana:**
$$
   D = \det(H) = (2)(2) - (0)^2 = 4 > 0
$$

   E $\dfrac{\partial^2 f}{\partial x^2} = 2 > 0$.

Portanto, $(1, 2)$ é um mínimo local.
