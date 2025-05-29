---
dg-publish: true
---
A **distribuição normal** (também conhecida como distribuição gaussiana) é uma das distribuições de probabilidade mais importantes e amplamente utilizadas na estatística. Ela descreve a distribuição de frequência de um grande número de fenômenos naturais e sociais que são influenciados por muitas variáveis independentes.

## Características da Distribuição Normal

1. **Simetria**:
   - A distribuição normal é simétrica em torno do seu valor médio (ou média), denotado como $\mu$.
   - Isso significa que a curva de probabilidade é simétrica ao redor do eixo vertical passando por $\mu$.

2. **Curva da Distribuição**:
   - A função densidade de probabilidade (PDF) da distribuição normal é dada pela expressão:
     $$
     f(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
     
$$
   - Aqui, $\sigma$ é a desvio padrão da distribuição.

3. **Valores Padrão**:
   - A distribuição normal padrão ocorre quando $\mu = 0$ e $\sigma = 1$. Sua PDF simplifica para:
     $$
     f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}
     
$$

3. **Área Total**:
   - A área total sob a curva da distribuição normal é igual a 1, representando a probabilidade total de todos os possíveis valores.

## Derivação da Distribuição Normal

A derivada da distribuição normal pode ser entendida a partir do limite de outras distribuições. Uma das maneiras mais comuns de derivar a distribuição normal é através do **Teorema Central do Limite** (TCL).

1. **Teorema Central do Limite**:
   - O TCL afirma que, para uma grande amostra, a média amostral de um conjunto de variáveis aleatórias independentes tende a seguir uma distribuição normal, independente da distribuição original das variáveis.

2. **Derivação a Partir de Distribuições Exponenciais**:
   - Considere uma sequência de variáveis aleatórias $X_1, X_2, \ldots, X_n$ independentes e identicamente distribuídas (i.i.d.) com média $\mu$ e desvio padrão $\sigma$. A soma dessas variáveis pode ser normalizada para formar uma nova variável:
     $$
     Z = \frac{\sum_{i=1}^{n} X_i - n\mu}{\sqrt{n}\sigma}
     
$$
   - À medida que $n$ aumenta, a distribuição de $Z$ converge para uma distribuição normal com média 0 e desvio padrão 1.

3. **Derivação a Partir de Distribuições Uniformes**:
   - Outra forma é considerar a soma de variáveis uniformemente distribuídas. A transformação adequada resulta em uma distribuição aproximadamente normal para grandes $n$.

#### Exemplos

- **Exemplo 1: Média de Notas Acadêmicas**:
  - Suponha que as notas dos alunos em um exame são distribuídas normalmente com média $\mu = 70$ e desvio padrão $\sigma = 15$. A probabilidade de um aluno tirar uma nota entre 60 e 80 pode ser calculada usando a função PDF da distribuição normal.

- **Exemplo 2: Medidas Físicas**:
  - As medidas físicas, como o comprimento de folhas de papel, tendem a seguir uma distribuição normal. Se a média do comprimento é $\mu = 21$ cm e o desvio padrão é $\sigma = 0.5$ cm, podemos usar a distribuição normal para calcular probabilidades específicas.
