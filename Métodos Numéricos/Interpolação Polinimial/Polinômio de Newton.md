---
dg-publish: true
---

## Definição

O polinômio de Newton é definido como:

$$
P(x) = y_0 + \frac{x - x_0}{x_1 - x_0} (y_1 - y_0) + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_1 - x_0)} (y_2 - y_0 - \frac{x_2 - x_0}{x_1 - x_0} (y_1 - y_0)) + ...
$$

onde $x_i$ são os pontos de interpolação e $y_i$ são as respectivas funções.

## Cálculo Do Polinômio

Para calcular o polinômio de Newton, é necessário seguir os seguintes passos:

1. **Defina os pontos de interpolação**: Escolha os pontos $x_0, x_1, …, x_n$ onde deseja realizar a interpolação.
2. **Calcule as diferenças divididas**: Calcule as diferenças divididas $\frac{x_i - x_j}{x_k - x_j}$ para cada par de pontos $(x_i, x_j)$ e $(x_k, x_j)$.
3. **Calcule os coeficientes do polinômio**: Utilize as diferenças divididas para calcular os coeficientes do polinômio $P(x)$.

## Exemplos

### Interpolação de Funções

Suponha que deseja interpolar a função $f(x) = x^2 + 1$ nos pontos $x_0 = -1, x_1 = 0, x_2 = 1$. O polinômio de Newton pode ser calculado como:

$$
P(x) = f(-1) + \frac{x + 1}{1 - (-1)} (f(0) - f(-1)) + \frac{(x + 1)(x - 1)}{1 - (-1)^2} (f(1) - f(-1) - \frac{1 - (-1)}{1 - (-1)} (f(0) - f(-1)))
$$

### Interpolação de Dados

Suponha que deseja interpolar os dados $(x_0, y_0) = (2, 3), (x_1, y_1) = (4, 5), (x_2, y_2) = (6, 7)$. O polinômio de Newton pode ser calculado como:

$$
P(x) = y_0 + \frac{x - x_0}{x_1 - x_0} (y_1 - y_0) + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_1 - x_0)} (y_2 - y_0 - \frac{x_2 - x_0}{x_1 - x_0} (y_1 - y_0))
$$

### Propriedades Do Polinômio de Newton

* O polinômio de Newton é uma ferramenta matemática utilizada para aproximar funções e realizar interpolação.
* Ele é nomeado em homenagem ao matemático inglês Isaac Newton.
* O polinômio de Newton pode ser utilizado para interpolar funções e dados.

### Aplicações Do Polinômio de Newton

* A interpolação de funções: o polinômio de Newton pode ser utilizado para aproximar funções em pontos específicos.
* A interpolação de dados: o polinômio de Newton pode ser utilizado para interpolar dados em pontos específicos.

### Limitações Do Polinômio de Newton

* O polinômio de Newton é uma ferramenta matemática que tem limitações, como a necessidade de escolher os pontos de interpolação corretamente.
* Além disso, o polinômio de Newton pode não ser preciso em todos os casos.

## Erro na Interpolação Polinomial de Newton

Dado um conjunto de pontos $x_0, x_1, \dots, x_n$ distintos, e uma função $f$ interpolada por um polinômio de Newton $P_n(x)$, o **erro** da interpolação em um ponto $x$ (não necessariamente um dos $x_i$) é dado por:

$$
f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \cdot (x - x_0)(x - x_1) \cdots (x - x_n)
$$

com:

* $\xi \in [a, b]$, onde $x_0, x_1, \dots, x_n, x \in [a, b]$,
* $f^{(n+1)}(\xi)$ é a derivada de ordem $(n+1)$ da função $f$ avaliada em algum ponto $\xi$ desconhecido.

## Derivação Do Erro em Newton

A fórmula de Newton baseia-se em **diferenças divididas**:

$$
P_n(x) = f[x_0] + f[x_0, x_1](x - x_0) + \dots + f[x_0, \dots, x_n](x - x_0)\cdots(x - x_{n-1})
$$

Mas existe um resultado teórico importante:

A diferença dividida de ordem $n+1$, $f[x_0, x_1, \dots, x_n, x]$, está relacionada com a derivada de ordem $(n+1)$ da função:

 $$
f[x_0, x_1, \dots, x_n, x] = \frac{f^{(n+1)}(\xi)}{(n+1)!}
$$

Assim, adicionando esse termo ao polinômio de grau $n$, temos a forma completa com erro:

$$
f(x) = P_n(x) + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - x_0)(x - x_1) \cdots (x - x_n)
$$

## Estimativa Do Erro (limitante superior)

Se $|f^{(n+1)}(t)| \le M$ em todo $t \in [a, b]$, então o erro máximo possível em $x$ é:

$$
|f(x) - P_n(x)| \le \frac{M}{(n+1)!} \cdot |(x - x_0)(x - x_1)\cdots(x - x_n)|
$$

## Exemplo

Interpole $f(x) = \cos(x)$ em $[0, \pi/2]$ com os pontos $x_0 = 0$, $x_1 = \pi/4$, $x_2 = \pi/2$.

Derivadas de $f(x)$:

* $f’(x) = -\sin(x)$
* $f’’(x) = -\cos(x)$
* $f^{(3)}(x) = \sin(x)$

Logo, $|f^{(3)}(x)| \le 1$ para todo $x \in [0, \pi/2]$, então $M = 1$.

Erro em $x = \pi/3$:

* $\omega(x) = (x - x_0)(x - x_1)(x - x_2)$
* Com $x = \pi/3$:

$$
    
    \omega(x) = \left(\frac{\pi}{3} - 0\right)\left(\frac{\pi}{3} - \frac{\pi}{4}\right)\left(\frac{\pi}{3} - \frac{\pi}{2}\right) = \frac{\pi}{3} \cdot \frac{\pi}{12} \cdot \left(-\frac{\pi}{6}\right)
    
    
$$

Então:

$$
|f(x) - P_2(x)| \le \frac{1}{3!} \cdot \left|\frac{\pi^3}{3 \cdot 12 \cdot 6}\right| = \frac{1}{6} \cdot \left|\frac{\pi^3}{216}\right| = \frac{\pi^3}{1296}
$$
