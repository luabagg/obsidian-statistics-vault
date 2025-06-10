---
dg-publish: true
---

## Ajuste de Curvas - Método dos Mínimos Quadrados

O **método dos mínimos quadrados** é uma técnica fundamental para o ajuste de curvas a conjuntos de dados experimentais. Ele consiste em encontrar uma função que represente da melhor forma os dados disponíveis, minimizando a soma dos **quadrados dos erros**, ou seja, a diferença entre os valores observados e os valores estimados pela função.

Esse método é amplamente utilizado em estatística, física, engenharia, economia e outras áreas que envolvem análise de dados e modelagem de relações entre variáveis.

### Objetivo

Dado um conjunto de dados experimentais $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$, buscamos uma função $f(x)$ dentro de uma família predefinida (reta, polinômio, exponencial etc.) que minimize o **erro quadrático total**:

$$
E(a_0, a_1, \dots, a_k) = \sum_{i=1}^n \left[y_i - f(x_i)\right]^2
$$

### Caso Mais Comum: Ajuste de Uma Reta ($f(x) = a + bx$)

Desejamos encontrar os coeficientes $a$ e $b$ da função linear que melhor se ajusta aos dados. Para isso, minimizamos:

$$
E(a, b) = \sum_{i=1}^n \left[y_i - (a + bx_i)\right]^2
$$

#### Sistema Normal

Derivando o erro em relação a $a$ e $b$, e igualando as derivadas a zero (condição de mínimo), obtemos o **sistema normal**:

$$
\begin{cases}

n a + b \sum x_i = \sum y_i \

a \sum x_i + b \sum x_i^2 = \sum x_i y_i

\end{cases}
$$

Esse sistema pode ser resolvido por métodos algébricos tradicionais ou por métodos matriciais.

### Forma Matricial Do Sistema

O sistema pode ser representado na forma matricial:

$$
\begin{pmatrix}
N & \sum x_i \\
\sum x_i & \sum x_i^2
\end{pmatrix}

\begin{pmatrix}
A \\
B
\end{pmatrix}

\begin{pmatrix}
\sum y_i \
\sum x_i y_i

\end{pmatrix}
$$

### Exemplo Numérico: Ajuste de Reta

Dado o conjunto de pontos:

|**$x$**|**$y$**|
|---|---|
|1|2|
|2|3|
|3|5|
|4|4|

Calculamos:

- $n = 4$
- $\sum x_i = 10$
- $\sum y_i = 14$
- $\sum x_i^2 = 30$
- $\sum x_i y_i = 39$

Sistema:

$$
\begin{pmatrix}

4 & 10 \\ \\

10 & 30

\end{pmatrix}

\begin{pmatrix}

A \\

B

\end{pmatrix}

\begin{pmatrix}

14 \\

39

\end{pmatrix}
$$

Resolvendo:

Multiplicando a primeira equação por 3:

$$
12a + 30b = 42
$$

Subtraindo da segunda equação:

$$
(12a + 30b) - (10a + 30b) = 42 - 39 \Rightarrow 2a = 3 \Rightarrow a = \frac{3}{2}
$$

Substituindo:

$$
4 \cdot \frac{3}{2} + 10b = 14 \Rightarrow 6 + 10b = 14 \Rightarrow b = \frac{8}{10} = 0{,}8
$$
**Função ajustada**:
$$
f(x) = \frac{3}{2} + 0{,}8x
$$

### Caso Geral: Ajuste de um Polinômio de Grau $k$

Quando se deseja ajustar um polinômio de grau $k$:

$$
f(x) = a_0 + a_1 x + a_2 x^2 + \dots + a_k x^k
$$

O objetivo continua sendo minimizar:

$$
E(a_0, \dots, a_k) = \sum_{i=1}^n \left[y_i - f(x_i)\right]^2
$$

Isso gera um sistema linear de $k+1$ equações, cujos coeficientes são obtidos com base nas somas dos termos das potências de $x$ e produtos $x^j y_i$. O sistema gerado também pode ser resolvido por métodos matriciais:

$$
A \mathbf{a} = \mathbf{b}
$$

Onde:

- $A$ é a matriz dos somatórios das potências de $x$.
- $\mathbf{a}$ é o vetor dos coeficientes $(a_0, a_1, \dots, a_k)^T$
- $\mathbf{b}$ é o vetor com os somatórios dos produtos $x_i^j y_i$.

### Exemplo Numérico: Ajuste Quadrático

Dado o mesmo conjunto de pontos:

|**$x$**|**$y$**|
|---|---|
|1|2|
|2|3|
|3|5|
|4|4|

Desejamos ajustar um polinômio de grau 2: $f(x) = a_0 + a_1 x + a_2 x^2$

Calculamos:

- $n = 4$
- $\sum x_i = 10$
- $\sum x_i^2 = 30$
- $\sum x_i^3 = 100$
- $\sum x_i^4 = 354$
- $\sum y_i = 14$
- $\sum x_i y_i = 39$
- $\sum x_i^2 y_i = 137$

Sistema matricial:

$$
\begin{pmatrix}

4 & 10 & 30 \\

10 & 30 & 100 \\

30 & 100 & 354

\end{pmatrix}

\begin{pmatrix}

a_0 \\

a_1 \\

a_2

\end{pmatrix}

\begin{pmatrix}

14 \\

39 \\

137

\end{pmatrix}
$$

Esse sistema pode ser resolvido por métodos diretos (eliminação de Gauss, decomposição LU) ou computacionalmente.

### Considerações Finais

- O método dos mínimos quadrados fornece uma **solução ótima** (em termos de erro quadrático) para funções lineares nos parâmetros.
- O ajuste é sensível a **valores atípicos** (outliers), pois penaliza fortemente erros grandes.
- É possível aplicar transformações aos dados para ajustar modelos não lineares.
- Para polinômios de grau alto, pode ocorrer **sobreajuste** — o modelo se ajusta muito bem aos dados amostrados, mas generaliza mal.

### Aplicações

- Modelagem de fenômenos físicos (como movimento, crescimento populacional)
- Previsão de tendências em séries temporais
- Análise estatística e regressão
- Engenharia e controle de processos

---

## Arquivo Extra

![[Ajuste de Curvas - Quadrados Mínimos.pdf]]
