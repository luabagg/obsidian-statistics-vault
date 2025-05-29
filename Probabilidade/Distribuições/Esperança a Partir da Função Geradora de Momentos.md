---
dg-publish: true
---

Para calcular a esperança (ou valor esperado) de uma variável aleatória $X$ a partir da função geradora de momentos, denotada por $M_X(t)$, podemos seguir os passos abaixo:

1. **Definição da Função Geradora de Momentos**:
   A função geradora de momentos é definida como:
$$
   M_X(t) = E[e^{tX}] = \sum_{k=0}^{\infty} \frac{E[X^k]}{k!} t^k
$$

   para uma variável aleatória discreta, ou

$$
   M_X(t) = E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} f(x) dx
$$

   para uma variável aleatória contínua, onde $f(x)$ é a função de densidade de probabilidade.

1. **Calculando a Esperança**:
   A esperança $E[X]$ pode ser obtida derivando a função geradora de momentos em relação ao parâmetro $t$ e avaliando no ponto $t = 0$. Isso se deve à propriedade da função geradora de momentos que relaciona os momentos da variável aleatória com suas derivadas.

   - **Derivada Primeira**:
$$
     M_X'(t) = \frac{d}{dt} E[e^{tX}] = E[Xe^{tX}]
$$
     Avaliando em $t = 0$:
$$
     M_X'(0) = E[X]
$$
   - **Derivada Segunda**:
$$
     M_X''(t) = \frac{d^2}{dt^2} E[e^{tX}] = E[X^2e^{tX}]
$$
     Avaliando em $t = 0$:
$$
     M_X''(0) = E[X^2]
$$
2. **Exemplo**:
   Considere uma variável aleatória discreta $X$ com [[Distribuição de Bernoulli]], onde $P(X=1) = p$ e $P(X=0) = 1-p$. A função geradora de momentos é:
$$
   M_X(t) = E[e^{tX}] = (1-p) + pe^t
$$

   Derivando em relação a $t$:

$$
   M_X'(t) = pe^t
$$

   Avaliando em $t = 0$:

$$
   M_X'(0) = p
$$

   Portanto, a esperança é:

$$
   E[X] = p
$$
