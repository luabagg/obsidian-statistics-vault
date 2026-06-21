---
dg-publish: true
---

O **método da bisseção** é um método numérico para encontrar uma raiz de uma função contínua $f(x)$ dentro de um intervalo $[a, b]$ onde ocorre uma mudança de sinal, ou seja, $f(a) \cdot f(b) < 0$. O método é baseado no [[Teorema De Bolzano]], que garante a existência de pelo menos uma raiz nesse intervalo.  

## Definição Formal

Seja $f: \mathbb{R} \to \mathbb{R}$ uma função contínua no intervalo $[a, b]$ tal que $f(a) \cdot f(b) < 0$. O método da bisseção segue os seguintes passos iterativos:  

1. **Calcular o ponto médio** do intervalo:
$$
c = \frac{a + b}{2}
$$
2. **Verificar a raiz**:
	- Se $f(c) = 0$, então $c$ é a raiz da equação.  
	- Se $f(a) \cdot f(c) < 0$, então a raiz está no intervalo $[a, c]$, e atualizamos $b = c$.  
	- Caso contrário, a raiz está no intervalo $[c, b]$, e atualizamos $a = c$.

3. **Repetir o processo** até que a diferença entre $a$ e $b$ seja menor que um critério de tolerância $\varepsilon$.

O método converge de forma garantida, pois a cada iteração o intervalo que contém a raiz é reduzido pela metade.  

---

## Código em Python

A implementação do método da bisseção pode ser feita da seguinte maneira:  

```python
def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Find a root of the function f(x) = 0 in the interval [a, b] using the Bisection method.

    Parameters:
    f        -- Continuous function for which the root is sought (callable)
    a, b     -- Interval endpoints (floats), must satisfy f(a)*f(b) < 0
    tol      -- Tolerance for stopping criterion (float, default 1e-6)
    max_iter -- Maximum number of iterations (int, default 100)

    Returns:
    result -- Dictionary with keys:
        'root'           : Approximated root (float)
        'function_value' : Value of f at the root (float)
        'iterations'     : Number of iterations performed (int)
        'converged'      : Boolean indicating if the method converged (bool)
    """
    if f(a) * f(b) >= 0:
        raise ValueError("Bolzano's Theorem is not guaranteed: f(a) and f(b) must have opposite signs.")

    for iteration in range(1, max_iter + 1):
        c = (a + b) / 2  # Midpoint
        fc = f(c)
        if abs(fc) < tol or (b - a) / 2 < tol:
            return {
                'root': c,
                'function_value': fc,
                'iterations': iteration,
                'converged': True
            }
        if f(a) * fc < 0:
            b = c  # Root is in [a, c]
        else:
            a = c  # Root is in [c, b]
# If max_iter Reached
    c = (a + b) / 2
    fc = f(c)
    return {
        'root': c,
        'function_value': fc,
        'iterations': max_iter,
        'converged': False
    }

# Example Usage
if __name__ == "__main__":
    f = lambda x: x**3 + x**2 - 10
    result = bisection(f, 0, 2, 1e-8)
    print(f"Approximate root: {result['root']:.10f}")
    print(f"Function value at the root: {result['function_value']}")
    print(f"Number of iterations: {result['iterations']}")
    print(f"Converged: {result['converged']}")
```

## Erros no Método da Bisseção

O método da bisseção, apesar de ser um método robusto e garantido para encontrar raízes de funções contínuas, apresenta algumas limitações e fontes de erro que devem ser consideradas.  

### Erro Absoluto e Erro Relativo

O erro absoluto em uma iteração do método pode ser estimado pelo tamanho do intervalo:  

$$
E_n = \frac{b_n - a_n}{2}
$$

onde $E_n$ representa o erro na $n$-ésima iteração. Como o método reduz o intervalo pela metade a cada passo, o erro diminui exponencialmente, sendo aproximadamente:  

$$
E_n = \frac{b - a}{2^n}
$$

onde $(b - a)$ é o tamanho inicial do intervalo.  

O erro relativo é dado por:  

$$
E_{rel} = \frac{|x_n - x_{n-1}|}{|x_n|}
$$

onde $x_n$ é a estimativa da raiz na $n$-ésima iteração.  

### Critério de Parada e Precisão

O método da bisseção é finalizado quando o erro absoluto $E_n$é menor que uma tolerância $\varepsilon$, isto é:  

$$
\frac{b_n - a_n}{2} < \varepsilon
$$

Se a tolerância for muito pequena, o número de iterações pode ser alto, aumentando o tempo de computação.  

### Erro de Arredondamento

Em implementações computacionais, os cálculos de ponto flutuante podem introduzir pequenos erros devido à precisão finita das representações numéricas. No entanto, como o método da bisseção não envolve operações como divisão sucessiva ou diferenciação, ele é relativamente menos sensível a erros de arredondamento do que outros métodos, como o de Newton-Raphson.  

### Erro Conceitual: Requisitos Do Teorema de Bolzano

O método da bisseção depende do **Teorema de Bolzano**, que exige que a função seja **contínua** e que os valores em $a$ e $b$ tenham sinais opostos. Se esses requisitos não forem atendidos:  

- Se $f(a)$ e $f(b)$ tiverem o mesmo sinal, o método falha.  
- Se houver múltiplas raízes no intervalo, o método pode convergir para qualquer uma delas sem garantir qual será encontrada.  
- Se a função não for contínua, a raiz pode ser perdida.  

### Lentidão na Convergência

O método da bisseção tem convergência **linear**, ou seja, reduz o erro pela metade a cada iteração. Comparado a métodos como Newton-Raphson, que tem convergência **quadrática**, a bisseção pode ser muito mais lenta.  

## Estimativa Do Número de Iterações

Para estimar o número de iterações necessárias no método da bisseção para garantir que a raiz esteja dentro de um intervalo tolerável, consideramos as seguintes etapas:

1. **Definição do Intervalo Inicial**: Suponha que temos um intervalo inicial $[a_0, b_0]$ onde a função $f(x)$ muda de sinal, indicando a presença de uma raiz.
2. **Formulando a Estimativa**:
   - A estimativa do número de iterações necessárias é dada pela fórmula:
$$
n \geq \frac{\log\left(\frac{b_0 - a_0}{\varepsilon}\right)}{\log(2)}
$$
    onde $n$ é o número mínimo de iterações, e $\varepsilon$ é a tolerância desejada para o erro.

3. **Exemplo**:
   - Considere uma função $f(x) = x^3 - 2x - 5$, com intervalo inicial $[1, 2]$. Aqui, $a_0 = 1$, $b_0 = 2$ e $\varepsilon = 0.001$.
   - Calculando:
$$
n \geq \frac{\log\left(\frac{2 - 1}{0.001}\right)}{\log(2)} = \frac{\log(1000)}{\log(2)} \approx \frac{3}{0.301} \approx 9.97
$$
   - Portanto, precisamos de pelo menos $10$ iterações para garantir que a raiz esteja dentro da tolerância $\varepsilon = 0.001$.

4. **Observações**:
   - O método da bisseção é garantido a convergir se a função for contínua no intervalo e mudar de sinal.
   - A estimativa acima é uma aproximação; na prática, pode ser necessário mais iterações para atingir a precisão desejada.

5. **Implementação**:
   - Em um algoritmo, após cada iteração, o intervalo é metade do anterior, garantindo que a raiz esteja sempre dentro de um subintervalo daquele tamanho.
   - A condição de parada pode ser definida como $|b_n - a_n| < \varepsilon$, onde $n$ é o número atual de iterações.
