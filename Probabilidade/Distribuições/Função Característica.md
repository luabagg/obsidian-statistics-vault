---
dg-publish: true
---

Seja $X$ uma variável aleatória. A **função característica** de $X$ é definida como:

$$
\varphi_X(t) = \mathbb{E}[e^{itX}], \quad \text{para todo } t \in \mathbb{R}
$$

onde $i$ é a unidade imaginária tal que $i^2 = -1$, e $\mathbb{E}$ representa o valor esperado.

Propriedades Importantes

- Existência: A função característica sempre existe, pois $|e^{itX}| = 1$, logo $\mathbb{E}[|e^{itX}|] \leq 1$.
- Unicidade: A função característica determina de forma única a distribuição de $X$. Ou seja, se duas variáveis aleatórias têm a mesma função característica, então possuem a mesma distribuição.
- Continuidade: $\varphi_X(t)$ é uma função contínua em $t$.
- Em $t = 0$: Sempre temos $\varphi_X(0) = 1$.
- Simetria: $\varphi_X(-t) = \overline{\varphi_X(t)}$, onde $\overline{z}$ representa o conjugado complexo de $z$.
- Derivadas: Se $X$ tem momentos finitos, então $\varphi_X(t)$ é derivável, e:

$$
\varphi_X^{(k)}(0) = i^k \mathbb{E}[X^k]
$$

Assim, é possível obter os momentos de $X$ a partir das derivadas da função característica.

Exemplo: Variável Aleatória Uniforme

Se $X \sim \text{Uniforme}(a, b)$, então sua função característica é dada por:

$$
\varphi_X(t) = \mathbb{E}[e^{itX}] = \int_a^b e^{itx} \cdot \frac{1}{b - a} , dx = \frac{e^{itb} - e^{ita}}{it(b - a)}
$$

Utilização

- Teorema Central do Limite: A função característica é uma ferramenta essencial para demonstrar este teorema.
- Somas de Variáveis Aleatórias: Se $X$ e $Y$ são independentes, então $\varphi_{X+Y}(t) = \varphi_X(t) \cdot \varphi_Y(t)$.
- Estudo de Convergência: A convergência pontual de funções características pode implicar a convergência em distribuição das variáveis associadas.

