---
dg-publish: true
dg-show-local-graph: true
---

%% Begin Waypoint %%
- **[[Limites]]**
	- [[Limites e Continuidade de Funções de 2 Variáveis]]
	- [[Limites Fundamentais do Cálculo]]
	- [[Teorema do Confronto]]

%% End Waypoint %%

## Introdução aos Limites no Cálculo

Os **limites** são conceitos fundamentais na matemática, especialmente no cálculo. Eles desempenham um papel crucial na definição de derivadas e integrais, permitindo a análise do comportamento de funções em pontos próximos a certos valores.

### Definição Formal

Um **limite** é a ideia de que uma função pode se aproximar arbitrariamente próximo a um valor específico à medida que o argumento da função se aproxima de um ponto. Matematicamente, dizemos que $\lim_{x \to a} f(x) = L$ se e somente se para todo $\epsilon > 0$, existe um $\delta > 0$ tal que $|f(x) - L| < \epsilon$ sempre que $0 < |x - a| < \delta$. Isto é, o valor da função $f(x)$ pode ficar tão próximo quanto desejarmos do número $L$ quando $x$ estiver suficientemente perto de $a$, mas não igual a $a$.

### Exemplos

1. **Exemplo 1:**
   Considere a função $f(x) = x^2$. Queremos encontrar $\lim_{x \to 3} f(x)$.
$$
\lim_{x \to 3} x^2 = 9
$$

   Isto é, conforme $x$ se aproxima de 3, o valor de $f(x) = x^2$ se aproxima de 9.

2. **Exemplo 2:**
   Para a função $g(x) = \frac{x^2 - 1}{x - 1}$, queremos encontrar $\lim_{x \to 1} g(x)$.
$$
\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} (x + 1) = 2
$$

   Embora $g(1)$ não esteja definida, o limite existe e é igual a 2.

### Aplicações

Os limites são essenciais para entender comportamentos de funções em pontos onde podem ocorrer singularidades ou descontinuidades. Eles também são fundamentais na definição das derivadas, que medem a taxa de mudança instantânea de uma função.
