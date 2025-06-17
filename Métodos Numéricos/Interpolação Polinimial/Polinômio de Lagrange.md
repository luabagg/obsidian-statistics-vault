---
dg-publish: true
---

## Definição Do Polinômio de Lagrange

Dado um conjunto de pontos $(x_1, y_1), (x_2, y_2), …, (x_n, y_n)$, o polinômio de Lagrange é definido como:

$$
P(x) = \sum_{i=1}^{n} y_i L_i(x)
$$

onde $L_i(x)$ é o polinômio de Lagrange associado ao ponto $(x_i, y_i)$. O polinômio de Lagrange é uma técnica matemática utilizada para interpolar pontos dados em um espaço bidimensional. Foi desenvolvido pelo matemático francês Joseph-Louis Lagrange no século XVIII.

## Polinômio de Lagrange Individual

O polinômio de Lagrange individual é definido como:

$$
L_i(x) = \prod_{j=1}^{n} \frac{x - x_j}{x_i - x_j}
$$

para $i \neq j$ e $0$ para $i=j$. Isso garante que o polinômio seja igual a 1 no ponto $(x_i, y_i)$ e zero em todos os outros pontos.

## Exemplo de Cálculo Do Polinômio de Lagrange

Suponha que tenhamos os seguintes pontos: $(0,2), (1,3), (2,5)$. O polinômio de Lagrange pode ser calculado como:

$$
\begin{align*}
L_1(x) &= \frac{(x-1)(x-2)}{(0-1)(0-2)} = -\frac{x^2}{2} + 3x - 2 \\
L_2(x) &= \frac{(x-0)(x-2)}{(1-0)(1-2)} = x^2 - 2x \\
P(x) &= L_1(x) + L_2(x) + L_3(x) \\
&= -\frac{x^2}{2} + 3x - 2 + x^2 - 2x + \left(\frac{(x-0)(x-1)}{(2-0)(2-1)}\right) \\
&= \frac{5x^2}{2} - 4x + 2
\end{align*}
$$

## Interpolação com o Polinômio de Lagrange

O polinômio de Lagrange pode ser utilizado para interpolar os pontos dados. Para encontrar a interseção do gráfico da função $P(x)$ e o eixo y, basta calcular $P(0)$. Além disso, podemos encontrar as raízes do polinômio calculando $x$ tal que $P(x)=0$.

## Exemplo de Interpolação

Suponha que desejamos interpolar os pontos $(0,2), (1,3), (2,5)$. O polinômio de Lagrange foi calculado anteriormente como:

$$
\frac{5x^2}{2} - 4x + 2
$$

Para encontrar a interseção com o eixo y, basta calcular $P(0)$:

$$
P(0) = \frac{5(0)^2}{2} - 4(0) + 2 = 2
$$

Portanto, a interseção do gráfico da função $P(x)$ e o eixo y é $(0,2)$.

## Aplicação Prática Do Polinômio de Lagrange

O polinômio de Lagrange tem diversas aplicações práticas em áreas como:

* Interpolação de dados: O polinômio de Lagrange pode ser utilizado para interpolar pontos dados e encontrar a função que os relaciona.
* Aproximação de funções: O polinômio de Lagrange pode ser utilizado para aproximar funções complexas por meio da interpolação de pontos dados.
* Análise de dados: O polinômio de Lagrange pode ser utilizado para analisar dados e encontrar padrões ou tendências.

## Limitações Do Polinômio de Lagrange

O polinômio de Lagrange tem algumas limitações, como:

* Só é válido para interpolação de pontos finitos: O polinômio de Lagrange só é válido para interpolar pontos finitos e não pode ser utilizado para interpolar funções contínuas.
* Pode ter problemas de estabilidade: O polinômio de Lagrange pode ter problemas de estabilidade, especialmente quando o número de pontos a serem interpolados é grande.

### Erro de Interpolação (Forma de Lagrange)

Dado um polinômio de interpolação P_n(x) que interpola f(x) nos pontos x_0, x_1, \dots, x_n, o **erro de interpolação** em um ponto x (não necessariamente um dos x_i) é dado por:

$$
f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \cdot \omega_{n+1}(x)
$$

onde:

* $\omega_{n+1}(x) = \prod_{i=0}^{n}(x - x_i)$
* $\xi \in (a, b), com a \le x_i \le b e x \in [a, b]$
* $f^{(n+1)}(\xi)$ é a derivada de ordem n+1 da função f, avaliada em algum ponto \xi desconhecido dentro do intervalo.

---

### Estimativa Do Limitante Superior Do Erro

Se for possível limitar $|f^{(n+1)}(t)| \le M$ para todo $t \in [a, b]$, então o erro máximo (limitante superior) satisfaz:

$$
|f(x) - P_n(x)| \le \frac{M}{(n+1)!} \cdot |(x - x_0)(x - x_1)\cdots(x - x_n)|
$$

---

### Interpretação

* O erro depende da regularidade da função (via a derivada f^{(n+1)}) e da **distribuição dos pontos de interpolação**.
* Quanto mais suave for a função e mais bem distribuídos forem os pontos x_i, menor tende a ser o erro.
* O termo $\omega_{n+1}(x)$ cresce com a distância de x aos nós $x_i$, aumentando o erro fora do intervalo dos dados (extrapolação).

---

### Exemplo

Seja f(x) = \ln(x), e queremos interpolar em [1, 2] com 3 pontos:

* $x_0 = 1, x_1 = 1.5, x_2 = 2$
* Então $n = 2$, e estamos usando um polinômio de grau 2.

A derivada de ordem 3 de $\ln(x)$ é:

$$
f’’’(x) = \frac{2}{x^3}
$$

Em $[1, 2]$, temos:

$$
\max_{x \in [1, 2]} |f’’’(x)| = f’’’(1) = 2
$$

Logo, para estimar o erro em $x = 1.3$:

* $\omega_3(1.3) = (1.3 - 1)(1.3 - 1.5)(1.3 - 2) = (0.3)(-0.2)(-0.7) = 0.042$
* $M = 2, (n+1)! = $3! = 6$*

Erro estimado:

$$
|f(1.3) - P_2(1.3)| \le \frac{2}{6} \cdot 0.042 = \frac{1}{3} \cdot 0.042 = 0.014
$$
