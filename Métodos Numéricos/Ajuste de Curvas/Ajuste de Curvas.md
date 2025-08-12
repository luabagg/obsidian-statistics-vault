---
dg-publish: true
---

%% Begin Waypoint %%

- [[Ajuste de Curvas]]
	- [[Mínimos Quadrados]]

%% End Waypoint %%

## Conceito Geral

O ajuste de curvas é um processo matemático que busca encontrar uma função **f(x)** que melhor se ajusta a um conjunto de dados experimentais $(x_i, y_i)$. Em métodos numéricos, esse ajuste é realizado por meio de algoritmos que minimizam a diferença entre os valores observados e os previstos pela função. A função pode ser linear, polinomial, exponencial, logarítmica ou qualquer outra forma que modele a relação entre variáveis.

---

## Método dos Mínimos Quadrados

O **método dos mínimos quadrados** é o algoritmo mais comum para ajuste de curvas. Ele minimiza a soma dos quadrados dos resíduos (diferenças entre os valores observados e os calculados).

### Fórmula Matemática

Para um modelo linear $y = a_0 + a_1x + \dots + a_nx^n$, os coeficientes $a_0, a_1, \dots, a_n$ são determinados resolvendo o sistema de equações:

$$
\mathbf{A}^T \mathbf{A} \mathbf{a} = \mathbf{A}^T \mathbf{y}
$$  

Onde:

- $\mathbf{A}$ é a matriz dos termos independentes (ex: $[1, x_i, x_i^2, \dots]$),
- $\mathbf{a}$ é o vetor de coeficientes,
- $\mathbf{y}$ é o vetor dos valores observados.

### Exemplo

Suponha dados $(x_i, y_i)$:

$$
(1, 2), (2, 3), (3, 5)
$$  

Para ajustar uma reta $y = ax + b$, o sistema se torna:

$$
\begin{cases}
3a + 6b = 10 \\
6a + 14b = 20
\end{cases}
$$  

Resolvendo, obtém-se $a = 1.5$ e $b = 0.5$, resultando em $y = 1.5x + 0.5$.

---

## Ajuste de Curvas Polinomiais

Para modelos não lineares, como polinômios de grau superior, o método dos mínimos quadrados também é aplicado.

### Exemplo: Ajuste Quadrático

Dado um conjunto de pontos, o ajuste de uma parábola $y = ax^2 + bx + c$ minimiza a soma dos quadrados dos erros.

- **Aplicação**: Modelagem de fenômenos físicos, como movimento de partículas.
- **Limitação**: Pode sobreajustar dados com ruído, exigindo técnicas de regularização (ex: Tikhonov).

---

## Ajuste de Curvas Não Lineares

Em casos onde a relação não é polinomial, métodos iterativos como **Newton-Raphson** ou **Gradiente Descendente** são usados.

### Exemplo: Exponencial $y = ae^{bx}$

- **Passo 1**: Transformar a equação em logaritmo: $\ln y = \ln a + bx$.
- **Passo 2**: Aplicar mínimos quadrados para estimar $b$, depois calcular $a = e^{\bar{\ln y} - b\bar{x}}$.
- **Aplicação**: Crescimento populacional, decaimento radioativo.

---

## Critérios de Avaliação

- **Resíduos**: Medição da diferença entre dados reais e ajustados.
- **Coeficiente de Determinação ($R^2$)**: Indica a proporção da variância explicada pelo modelo.
- **Validação Cruzada**: Testar o modelo com dados não usados para evitar sobreajuste.

---

## Técnicas de Regularização

Para evitar sobreajuste em modelos complexos:

- **Tikhonov**: Adiciona um termo penalizador à função de erro.
- **Lasso/Ridge**: Restringe os coeficientes para evitar valores extremos.

### Exemplo: Regularização L2

$$
\text{Minimizar} \sum (y_i - f(x_i))^2 + \lambda \sum a_j^2
$$  

Onde $\lambda$ controla a intensidade da penalização.

---

## Aplicações Práticas

- **Engenharia**: Análise de tensão em materiais.
- **Economia**: Previsão de tendências de mercado.
- **Biologia**: Modelagem de crescimento celular.

---

## Limitações

- **Sensibilidade a outliers**: Dados anômalos podem distorcer o ajuste.
- **Suposições de linearidade**: Modelos não lineares exigem métodos específicos.
- **Computação intensiva**: Ajustes de alta complexidade demandam algoritmos otimizados.

---

## Ferramentas e Bibliotecas

- **Python**: `numpy.polyfit`, `scipy.optimize.curve_fit`.
- **R**: Funções `lm()` e `nls()`.
- **MATLAB**: `fit()` e `lsqcurvefit()`.

---

## Conclusão

O ajuste de curvas é essencial para extrair padrões de dados experimentais. Em métodos numéricos, técnicas como mínimos quadrados e regularização permitem modelar fenômenos complexos com precisão, desde que os dados sejam adequados ao modelo escolhido.
