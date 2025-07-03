---
dg-publish: true
---

A regra dos trapezios é uma técnica de integração numérica utilizada para aproximar a área sob uma curva. Ela consiste em dividir o intervalo de integração em subintervalos menores, chamados de trapézios, e calcular a área de cada um desses trapézios.

## Fórmula da Regra dos Trapezios

A fórmula da regra dos trapezios é dada por:

$$
\int_{a}^{b} f(x) dx \approx \frac{h}{2} \left[ f(a) + 2f(a+h) + 2f(a+2h) + ... + 2f(b-h) + f(b) \right]
$$

onde $h$ é a largura do trapézio e $n$ é o número de subintervalos.

## Exemplo

Suponha que desejamos calcular a área sob a curva $y = x^2$ no intervalo $[0, 2]$ com uma precisão de $10^{-3}$.

### Passo 1: Dividir o Intervalo em Subintervalos

Dividimos o intervalo $[0, 2]$ em subintervalos de largura $h = \frac{2-0}{n} = \frac{2}{n}$.

### Passo 2: Calcular a Área de Cada Trapézio

Calculamos a área de cada trapézio usando a fórmula:

$$
\text{Área do trapézio } i = \frac{h}{2} \left[ f(a+(i-1)h) + f(a+ih) \right]
$$

### Passo 3: Somar as Áreas dos Trapézios

Somamos as áreas dos trapézios para obter a área aproximada:

$$
\text{Área aproximada} = \sum_{i=1}^{n} \text{Área do trapézio } i
$$

## Precisão da Regra dos Trapezios

A precisão da regra dos trapezios depende do número de subintervalos $n$. Quanto maior for $n$, mais precisa será a aproximação.

### Tabela de Erro

A tabela de erro para a regra dos trapezios é dada por:

$$
E \leq \frac{b-a}{12} h^2 f''(\xi)
$$

onde $\xi$ está no intervalo $[a, b]$.

## Exemplo Implementado em Python

```python
import numpy as np

def regra_dos_trapezios(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)

    area = 0.5 * h * (y[0] + y[-1])
    for i in range(1, n):
        area += h * y[i]

    return area

# Defina a função f
def f(x):
    return x**2

# Calcule a área aproximada
a = 0
b = 2
n = 1000
area_aproximada = regra_dos_trapezios(f, a, b, n)

print("Área aproximada:", area_aproximada)
```

Essa implementação calcula a área aproximada sob a curva $y = x^2$ no intervalo $[0, 2]$ com uma precisão de $10^{-3}$ utilizando a regra dos trapezios.

## Arquivo Adicional

![[Regra dos Trapézios.pdf]]
