---
dg-publish: true
dg-show-local-graph:
---

%% Begin Waypoint %%
- **[[Integrais]]**
	- [[Integrais Duplas em Coordenadas Polares]]
	- [[Integrais Duplas Sobre Regiões Gerais]]
	- [[Integrais Duplas]]
	- [[Soma de Riemann]]
	- [[Teorema de Fubini]]

%% End Waypoint %%

Integrais são um conceito fundamental na matemática e no cálculo, essencial para a modelagem de fenômenos físicos, econômicos e biológicos. Existem dois tipos principais de integrais: as integrais definidas e as indefinidas.

## Integrais Indefinidas

As integrais indefinidas são expressões que representam uma família de funções. Elas são escritas na forma:

$$
 \int f(x) \, dx = F(x) + C 
$$

onde $F(x)$ é a antiderivada de $f(x)$, e $C$ é a constante de integração.

**Exemplo:**
Calcule a integral indefinida de $f(x) = 3x^2$.
$$
 \int 3x^2 \, dx = x^3 + C 
$$

## Integrais Definidas

As integrais definidas são usadas para calcular áreas sob curvas e volumes de revolução. Elas são representadas por:

$$
 \int_{a}^{b} f(x) \, dx 
$$

onde $a$ é o limite inferior e $b$ é o limite superior da integral.

**Exemplo:**
Calcule a área sob a curva $f(x) = x^2$ entre $x=0$ e $x=1$.
$$
 \int_{0}^{1} x^2 \, dx = \left[ \frac{x^3}{3} \right]_0^1 = \frac{1}{3} - 0 = \frac{1}{3} 
$$

## Regras de Integração

Existem várias regras e métodos para calcular integrais. Algumas delas incluem:

- **Integração por Substituição:** Utilizada quando a função pode ser simplificada através de uma substituição.
$$
 \int f(g(x))g'(x) \, dx = \int f(u) \, du
$$
- **Integração por Partes:** Útil para integrais do tipo $\int u \, dv$.
$$
 \int u \, dv = uv - \int v \, du
$$

## Aplicações Práticas

As integrais são amplamente utilizadas em diversas áreas:

- **Física:** Para calcular trabalho, energia potencial e movimento.
- **Economia:** Para determinar fluxo de caixa e valor presente.
- **Biologia:** Para modelar crescimento populacional.

## Exemplo Prático

Considere a função $f(x) = 2x + 1$. Calcule o trabalho realizado ao mover uma carga em um campo elétrico descrito por essa função, entre os pontos $x=0$ e $x=3$.

O trabalho é dado pela integral definida:

$$
 W = \int_{0}^{3} (2x + 1) \, dx
$$

Calculando a integral:

$$
 W = \left[ x^2 + x \right]_0^3 = (9 + 3) - (0 + 0) = 12
$$

Portanto, o trabalho realizado é $12$ unidades de energia.
