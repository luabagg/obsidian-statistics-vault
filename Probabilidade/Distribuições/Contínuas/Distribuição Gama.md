---
dg-publish: true
---

A distribuição Gama é um método estatístico utilizado para descrever e analisar dados, especialmente em contextos onde se deseja entender a variabilidade dos dados. Esta distribuição é frequentemente aplicada em campos como medicina, engenharia, ciências sociais e economia.

## Características Principais

1. **Definição**:
   - A distribuição Gama é uma família de curvas contínuas que são usadas para modelar variáveis não negativas com variação proporcional.
   - É definida por dois parâmetros: o shape (forma) e o scale (escala).

2. **Forma da Distribuição**:
   - A forma da distribuição Gama pode variar significativamente dependendo dos valores de seus parâmetros.
   - Para valores baixos do parâmetro shape, a curva é assimétrica à direita e tem uma cauda longa.
   - À medida que o shape aumenta, a curva se torna mais simétrica e a cauda se torna menos pronunciada.

3. **Função de Densidade**:
$$
   f(x; k, \theta) = \frac{x^{k-1}e^{-\frac{x}{\theta}}}{\theta^k \Gamma(k)}
$$
   - Aqui, $k$ é o parâmetro shape e $\theta$ é o parâmetro scale.
   - $\Gamma(k)$ é a [[Função Gama]].

4. **Momentos**:
   - A esperança (média) da distribuição Gama é $E(X) = k\theta$.
   - O desvio padrão é $\sigma_X = \sqrt{k}\theta$.

5. **Aplicações**:
   - Em estatística, a distribuição Gama é usada para modelar variáveis que representam tempos de espera ou quantidades que não podem ser negativas.
   - Exemplos comuns incluem o tempo entre eventos em processos de Poisson, duração de falhas em componentes eletrônicos e volumes de vendas.

6. **Relação com Outras Distribuições**:
   - A distribuição Gama é uma generalização da [[Distribuição Exponencial]].
   - Quando $k = 1$, a distribuição Gama se torna a [[Distribuição Exponencial]].
   - Para valores inteiros de $k$, a distribuição Gama pode ser expressa como a soma de $k$ variáveis exponenciais independentes.

7. **Estimativa dos Parâmetros**:
   - Os parâmetros da distribuição Gama podem ser estimados usando métodos como o método dos momentos ou máxima verossimilhança.
   - Estas técnicas envolvem a utilização de dados observados para ajustar os parâmetros $k$ e $\theta$.

### Exemplo 1: Tempo de Recuperação Médica

**Contexto**: Em um estudo médico, os pesquisadores estão interessados no tempo até a recuperação completa dos pacientes após uma cirurgia. Suponha que o tempo de recuperação segue uma distribuição Gamma com parâmetros shape $k = 3$ e scale $\theta = 2$.

**Distribuição Gama**:
- **Parâmetro Shape ($k$)**: 3
- **Parâmetro Scale ($\theta$)**: 2

A função de densidade de probabilidade (PDF) para este caso é:

$$
f(x; 3, 2) = \frac{x^{3-1} e^{-\frac{x}{2}}}{2^3 \Gamma(3)} = \frac{x^2 e^{-\frac{x}{2}}}{8 \cdot 2!} = \frac{x^2 e^{-\frac{x}{2}}}{16}
$$
**Análise**:
- **Esperança (Média)**: $E(X) = k \theta = 3 \times 2 = 6$
- **Desvio Padrão**: $\sigma_X = \sqrt{k} \theta = \sqrt{3} \times 2 \approx 3.46$

**Interpretação**:
- A média de tempo de recuperação é 6 dias.
- O desvio padrão é aproximadamente 3.46 dias.

### Exemplo 2: Vida Útil de Componentes Eletrônicos

**Contexto**: Em engenharia, a vida útil de componentes eletrônicos pode ser modelada usando a distribuição Gamma. Suponha que a vida útil dos componentes segue uma distribuição Gamma com parâmetros shape $k = 5$ e scale $\theta = 10$.

**Distribuição Gama**:
- **Parâmetro Shape ($k$)**: 5
- **Parâmetro Scale ($\theta$)**: 10

A função de densidade de probabilidade (PDF) para este caso é:

$$
f(x; 5, 10) = \frac{x^{5-1} e^{-\frac{x}{10}}}{10^5 \Gamma(5)} = \frac{x^4 e^{-\frac{x}{10}}}{10^5 \cdot 24} = \frac{x^4 e^{-\frac{x}{10}}}{240000}
$$
**Análise**:
- **Esperança (Média)**: $E(X) = k \theta = 5 \times 10 = 50$
- **Desvio Padrão**: $\sigma_X = \sqrt{k} \theta = \sqrt{5} \times 10 \approx 22.36$

**Interpretação**:
- A média de vida útil dos componentes é 50 dias.
- O desvio padrão é aproximadamente 22.36 dias.

### Função Geradora de Momentos para Distribuição Gama

Para a distribuição Gama com parâmetros shape ($k$) e scale ($\theta$), a função geradora de momentos é dada por:

$$
M_X(t) = \left(1 - \frac{t}{\theta}\right)^{-k} \quad \text{para } t < \theta
$$

### Cálculo dos Momentos

Os momentos da distribuição podem ser obtidos a partir da FGM. O $n$-ésimo momento é dado pela derivada $n$-ésima de $M_X(t)$ avaliada em $t = 0$. Por exemplo:

1. **Esperança (Primeiro Momento)**:
   - A primeira derivada de $M_X(t)$ em $t = 0$ fornece a esperança da variável aleatória.
$$
M_X'(t) = k \left(1 - \frac{t}{\theta}\right)^{-k-1} \cdot \frac{1}{\theta}
$$

   Avaliando em $t = 0$:

$$
E(X) = M_X'(0) = k \cdot \frac{1}{\theta} = k \theta
$$
2. **Segundo Momento**:
   - A segunda derivada de $M_X(t)$ em $t = 0$ fornece o segundo momento.

$$
M_X''(t) = k(k+1) \left(1 - \frac{t}{\theta}\right)^{-k-2} \cdot \frac{1}{\theta^2}
$$

   Avaliando em $t = 0$:

$$
E(X^2) = M_X''(0) + M_X'(0) = k(k+1) \cdot \frac{1}{\theta^2} + k \cdot \frac{1}{\theta} = k(k+1) \cdot \frac{1}{\theta^2} + k \cdot \frac{1}{\theta}
$$
3. **Desvio Padrão**:
  - O desvio padrão é a raiz quadrada da variância, que pode ser calculada como $\sqrt{E(X^2) - (E(X))^2}$.

$$
\sigma_X = \sqrt{k(k+1)\theta^2 / \theta^2 + k\theta - (k\theta)^2} = \sqrt{k\theta^2} = \sqrt{k}\theta
$$

### Aplicações Práticas

A FGM é útil em várias aplicações, incluindo:

- **Estimação de Parâmetros**: Através da equação logarítmica da FGM, os parâmetros $k$ e $\theta$ podem ser estimados a partir dos dados observados.
- **Análise de Dados**: A FGM pode ser usada para verificar se uma amostra segue aproximadamente a distribuição Gama.

### Exemplo Prático

Considere um exemplo onde a vida útil de componentes eletrônicos segue uma distribuição Gamma com parâmetros $k = 5$ e $\theta = 10$. A FGM é:

$$
M_X(t) = \left(1 - \frac{t}{10}\right)^{-5} \quad \text{para } t < 10
$$

A esperança (média) pode ser calculada como:

$$
E(X) = M_X'(0) = 5 \cdot \frac{1}{10} = 50
$$

O desvio padrão é:

$$
\sigma_X = \sqrt{k}\theta = \sqrt{5} \times 10 \approx 22.36
$$
