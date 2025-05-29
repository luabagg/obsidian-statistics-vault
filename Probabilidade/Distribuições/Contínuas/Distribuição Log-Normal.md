---
dg-publish: true
---
Seja $X \sim N(\mu, \sigma^2)$. Considere uma nova variável aleatória $Y = e^X$, dizemos que $Y$ tem distribuição log-normal com parâmetros $m$ (o valor médio do logaritmo de $Y$) e $r$ (a desvio padrão do logaritmo de $Y$), onde $\sigma > 0$. A notação para essa distribuição é $Y \sim \text{Log-Normal}(m, r^2)$.

A função de densidade de probabilidade (f.d.p.) da variável aleatória $Y$ log-normal é dada por:

$$
f_Y(y) = \frac{1}{y\sigma\sqrt{2\pi}} e^{-\frac{(\ln y - m)^2}{2r^2}}, \quad y > 0.
$$

## Propriedades da Distribuição Log-normal

1. **Esperança**:
   A esperança de $Y$ é dada por:
   $$
   E[Y] = e^{m + \frac{\sigma^2}{2}}.
   
$$

2. **Variância**:
   A variância de $Y$ é dada por:
   $$

   \text{Var}(Y) = (e^{\sigma^2} - 1)e^{2m + \sigma^2}.

$$

3. **Mediana**:
   A mediana da distribuição log-normal é igual ao parâmetro $m$:
   $$

   \text{Med}(Y) = e^m.

$$

4. **Moda**:
   A moda da distribuição log-normal ocorre no ponto:
   $$

   y_{\text{mod}} = e^{m - \sigma^2}.

$$

5. **Função de Distribuição Cumulativa (FDC)**:
   A função de distribuição cumulativa $F_Y(y)$ é dada por:
   $$

   F_Y(y) = \Phi\left(\frac{\ln y - m}{r}\right),

$$
   onde $\Phi(z)$ é a função de distribuição acumulada da distribuição normal padrão.

### Exemplos

1. **Aplicação em Finanças**:
   A distribuição log-normal é frequentemente usada para modelar os retornos financeiros, pois esses retornos são positivos e tendem a seguir uma distribuição não simétrica.

2. **Exemplo de Cálculo**:
   Se $X \sim N(0, 1)$, então $Y = e^X$ segue uma distribuição log-normal com parâmetros $m = 0$ e $r = 1$. A f.d.p. de $Y$ é:
   $$

   f_Y(y) = \frac{1}{y\sqrt{2\pi}} e^{-\frac{\ln^2 y}{2}}, \quad y > 0.

$$

3. **Cálculo da Esperança**:
   Para o exemplo acima, a esperança de $Y$ é:
   $$

   E[Y] = e^{0 + \frac{1^2}{2}} = e^{0.5} \approx 1.6487.

$$

### Condições de Existência

A distribuição log-normal existe se $m - r^2 < 0$, ou seja, se o parâmetro $m$ é menor que a variância $r^2$. Isso garante que a esperança e a variância existam.
