---
dg-publish: true
---

A função gama, denotada por $\Gamma(z)$, é uma extensão do conceito de fatorial para números complexos. Foi introduzida pelo matemático Leonhard Euler em 1729. A definição fundamental da função gama é dada pela integral:

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}\,dt,
$$

onde $z$ é um número complexo com parte real positiva.

## Propriedades Principais

1. **Relação com o Fatorial**:
   Para números inteiros positivos $n$, a função gama satisfaz $\Gamma(n) = (n-1)!$. Por exemplo, $\Gamma(5) = 4! = 24$.

2. **Recursividade**:
   A função gama também possui uma propriedade recursiva dada por:
$$
\Gamma(z+1) = z\Gamma(z).
$$
3. **Identidade de Euler**:
   Uma das identidades mais famosas envolvendo a função gama é a fórmula de Euler, que relaciona o valor da função gama em um número complexo $z$ com a constante de Euler-Mascheroni $\gamma$ e a série harmônica:

$$
\Gamma(z+1) = z\Gamma(z) = \frac{e^{-\gamma z}}{z}\prod_{n=1}^\infty \left(1 + \frac{z}{n}\right)^{-1}e^{z/n},
$$

   onde $\gamma$ é a constante de Euler-Mascheroni.

1. **Simetria**:
   A função gama possui uma simetria interessante em relação ao plano complexo, dada pela relação:
$$
\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}.
$$

2. **Valores Especiais**:
   Existem vários valores especiais da função gama que são úteis em aplicações práticas, como $\Gamma(1/2) = \sqrt{\pi}$.

3. **Convergência**:
   A integral definindo a função gama converge para todos os números complexos $z$ com parte real positiva. Para outros valores de $z$, a função é estendida por análise complexa, garantindo sua continuidade em todo o plano complexo exceto nos pontos negativos inteiros.

A função gama desempenha um papel crucial na matemática aplicada e teórica, aparecendo frequentemente em áreas como probabilidade, física teórica, e análise complexa.
