---
dg-publish: true
---

Dizemos que a variável aleatória $X$ tem distribuição Weibull com parâmetros $\gamma > 0$ e $\epsilon > 0$, denotada por $X \sim \text{Weibull}(\gamma, \epsilon)$, se sua função de densidade estiver dada por:

$$
f(x; \gamma, \epsilon) = 
\begin{cases} 
\frac{\epsilon}{\gamma} \left( \frac{x}{\gamma} \right)^{\epsilon-1} e^{-(x/\gamma)^\epsilon}, & x \geq 0 \\
0, & x < 0
\end{cases}
$$

## Características da Distribuição Weibull

1. **Forma Flexível**: A distribuição Weibull é bastante flexível e pode modelar uma ampla variedade de formas de curva de densidade, desde distribuições unimodais até exponenciais.
2. **Parâmetros**:
   - $\gamma > 0$: Escala (ou forma). Alterações nesse parâmetro afetam a escala da variável aleatória.
   - $\epsilon > 0$: Forma. Alterações nesse parâmetro afetam a forma da distribuição, podendo modelar comportamentos de falha ou vida útil.

3. **Relação com Outras Distribuições**:
   - Para $\epsilon = 1$, a distribuição Weibull se torna uma distribuição exponencial.
   - Para $\gamma = 1$ e $\epsilon > 0$, a distribuição Weibull é conhecida como distribuição de Weibull padrão.

4. **Exemplo**:
   Considere uma situação onde se deseja modelar o tempo de vida de um componente eletrônico, com $\gamma = 2$ e $\epsilon = 3$. A função de densidade seria:

   $$
   f(x; 2, 3) = 
   \begin{cases} 
   \frac{3}{2} \left( \frac{x}{2} \right)^2 e^{-(x/2)^3}, & x \geq 0 \\
   0, & x < 0
   \end{cases}
   
$$

   Essa função descreveria a probabilidade de o componente falhar em diferentes instantes $x$.
