O **método da bisseção** é um método numérico para encontrar uma raiz de uma função contínua $f(x)$ dentro de um intervalo $[a, b]$ onde ocorre uma mudança de sinal, ou seja, $f(a) \cdot f(b) < 0$. O método é baseado no **Teorema de Bolzano**, que garante a existência de pelo menos uma raiz nesse intervalo.  

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

2. **Repetir o processo** até que a diferença entre $a$ e $b$ seja menor que um critério de tolerância $\varepsilon$.  

O método converge de forma garantida, pois a cada iteração o intervalo que contém a raiz é reduzido pela metade.  

---

## Código Em Python

A implementação do método da bisseção pode ser feita da seguinte maneira:  

```python

def bissecao(f, a, b, tol=1e-6, max_iter=100):
    """
    Método da Bisseção para encontrar um zero de f(x) no intervalo [a, b].
    
    Parâmetros:
    f        -- Função contínua f(x)

    a, b     -- Intervalo inicial [a, b] tal que f(a) * f(b) < 0

    tol      -- Critério de parada (erro máximo permitido)

    max_iter -- Número máximo de iterações

    Retorna:

    Raiz aproximada de f(x)

    """

    if f(a) * f(b) >= 0:
        raise ValueError("O Teorema de Bolzano não é garantido: f(a) e f(b) devem ter sinais opostos.")

    for _ in range(max_iter):
        c = (a + b) / 2  # Ponto médio
        if abs(f(c)) < tol or (b - a) / 2 < tol:  # Critério de convergência
            return c

        elif f(a) * f(c) < 0:
            b = c  # Raiz está em [a, c]
        else:
            a = c  # Raiz está em [c, b]

    return (a + b) / 2  # Aproximação final da raiz

# Exemplo de uso
f = lambda x: x**3 - 4*x + 1  # Definição da função

raiz = bissecao(f, 0, 2)  # Chamada do método

print(f"Raiz aproximada: {raiz:.6f}")

```

## Erros No Método Da Bisseção

O método da bisseção, apesar de ser um método robusto e garantido para encontrar raízes de funções contínuas, apresenta algumas limitações e fontes de erro que devem ser consideradas.  

### 1. **Erro Absoluto E Erro Relativo**

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

### 2. **Critério De Parada E Precisão**

O método da bisseção é finalizado quando o erro absoluto $E_n$é menor que uma tolerância $\varepsilon$, isto é:  

$$
\frac{b_n - a_n}{2} < \varepsilon
$$

Se a tolerância for muito pequena, o número de iterações pode ser alto, aumentando o tempo de computação.  

### 3. **Erro De Arredondamento**

Em implementações computacionais, os cálculos de ponto flutuante podem introduzir pequenos erros devido à precisão finita das representações numéricas. No entanto, como o método da bisseção não envolve operações como divisão sucessiva ou diferenciação, ele é relativamente menos sensível a erros de arredondamento do que outros métodos, como o de Newton-Raphson.  

### 4. **Erro Conceitual: Requisitos Do Teorema De Bolzano**

O método da bisseção depende do **Teorema de Bolzano**, que exige que a função seja **contínua** e que os valores em $a$ e $b$ tenham sinais opostos. Se esses requisitos não forem atendidos:  

- Se $f(a)$ e $f(b)$ tiverem o mesmo sinal, o método falha.  
- Se houver múltiplas raízes no intervalo, o método pode convergir para qualquer uma delas sem garantir qual será encontrada.  
- Se a função não for contínua, a raiz pode ser perdida.  

### 5. **Lentidão Na Convergência**

O método da bisseção tem convergência **linear**, ou seja, reduz o erro pela metade a cada iteração. Comparado a métodos como Newton-Raphson, que tem convergência **quadrática**, a bisseção pode ser muito mais lenta.  

## Estimativa Do Número De Iterações

Para estimar o número de iterações necessárias no método da bisseção para garantir que a raiz esteja dentro de um intervalo tolerável, consideramos as seguintes etapas:

1. **Definição do Intervalo Inicial**: Suponha que temos um intervalo inicial $[a_0, b_0]$ onde a função $f(x)$ muda de sinal, indicando a presença de uma raiz.
2. **Formulando a Estimativa**:
   - A estimativa do número de iterações necessárias é dada pela fórmula:
     \[
     n \geq \frac{\log\left(\frac{b_0 - a_0}{\varepsilon}\right)}{\log(2)}
     \]
     onde $n$ é o número mínimo de iterações, e $\varepsilon$ é a tolerância desejada para o erro.

3. **Exemplo**:
   - Considere uma função $f(x) = x^3 - 2x - 5$, com intervalo inicial $[1, 2]$. Aqui, $a_0 = 1$, $b_0 = 2$ e $\varepsilon = 0.001$.
   - Calculando:
     \[
     n \geq \frac{\log\left(\frac{2 - 1}{0.001}\right)}{\log(2)} = \frac{\log(1000)}{\log(2)} \approx \frac{3}{0.301} \approx 9.97
     \]
   - Portanto, precisamos de pelo menos $10$ iterações para garantir que a raiz esteja dentro da tolerância $\varepsilon = 0.001$.

4. **Observações**:
   - O método da bisseção é garantido a convergir se a função for contínua no intervalo e mudar de sinal.
   - A estimativa acima é uma aproximação; na prática, pode ser necessário mais iterações para atingir a precisão desejada.

5. **Implementação**:
   - Em um algoritmo, após cada iteração, o intervalo é metade do anterior, garantindo que a raiz esteja sempre dentro de um subintervalo daquele tamanho.
   - A condição de parada pode ser definida como $|b_n - a_n| < \varepsilon$, onde $n$ é o número atual de iterações.
