## Método Gráfico

O método gráfico consiste em esboçar o gráfico da função e observar os pontos onde ela cruza o eixo $x$. Se a curva intercepta o eixo $x$ em algum ponto, isso indica a presença de uma raiz. Esse método é útil para ter uma noção inicial sobre a existência e localização dos zeros, mas não fornece uma resposta precisa, apenas uma estimativa visual.

## Teorema De Bolzano

O **Teorema de Bolzano** fornece um critério rigoroso para a existência de pelo menos um zero de uma função contínua em um intervalo. Ele afirma que:

Se uma função $f(x)$ é contínua em um intervalo fechado $[a, b]$ e os valores da função nos extremos do intervalo possuem sinais opostos, ou seja,

$$
 f(a) \cdot f(b) < 0, 
$$

então existe pelo menos um número $c \in (a, b)$ tal que $f(c) = 0$.

Esse teorema é a base para o **método da bisseção**, um dos métodos numéricos para encontrar zeros de funções.

### Uso De Técnicas De Cálculo no Teorema De Bolzano

O **Teorema de Bolzano** garante a existência de pelo menos um zero de uma função contínua em um intervalo $[a, b]$ se $f(a) \cdot f(b) < 0$. No entanto, o teorema não nos fornece a localização exata desse zero nem a quantidade de raízes dentro do intervalo. Para uma análise mais detalhada, utilizamos técnicas do cálculo, como a **derivada**, para entender melhor o comportamento da função.

#### Continuidade E Diferenciabilidade

• O Teorema de Bolzano exige que $f(x)$ seja **contínua** no intervalo $[a, b]$.

• Se a função for também **diferenciável** (ou seja, tiver derivada contínua em $(a, b)$), podemos usar ferramentas como o **Teorema de Rolle** e o **Teorema do Valor Médio** para obter mais informações sobre a existência e multiplicidade de raízes.

#### Derivadas E Mudança De Sinal

Se a função $f(x)$ é diferenciável, sua derivada $f’(x)$ pode ser usada para analisar:

• **Comportamento crescente ou decrescente:** Se $f’(x) > 0$ em $(a, b)$, a função é crescente; se $f’(x) < 0$, é decrescente. Isso ajuda a verificar se a raiz é única.

• **Pontos críticos:** Se há um ponto crítico dentro de $(a, b)$ (onde $f’(x) = 0$), podemos avaliar se há mais de um zero no intervalo.

• **Concavidade e Ponto de Inflexão:** A segunda derivada $f’’(x)$ pode indicar se há mudanças na curvatura da função, ajudando a prever se os zeros são isolados ou múltiplos.

#### Aplicação Prática – Refinamento Do Intervalo

Podemos usar técnicas como o **método da bisseção**, que combina o Teorema de Bolzano com um processo iterativo para refinar um intervalo onde a raiz está localizada. Esse método consiste em:

1. Escolher um intervalo inicial $[a, b]$ onde $f(a) \cdot f(b) < 0$.

2. Calcular o ponto médio $c = \frac{a + b}{2}$.

3. Verificar o sinal de $f(c)$ e reduzir o intervalo de busca mantendo um subintervalo onde $f(x)$ muda de sinal.

4. Repetir o processo até alcançar uma precisão desejada.

#### Exemplo

Considere a função $f(x) = x^3 - 4x + 1$. Queremos verificar se há pelo menos um zero no intervalo $[0,2]$.

1. **Verificação pelo Teorema de Bolzano**:

$$
 f(0) = 0^3 - 4(0) + 1 = 1, \quad f(2) = 2^3 - 4(2) + 1 = -3. 
$$

Como $f(0) \cdot f(2) < 0$, existe pelo menos uma raiz em $(0,2)$.

2. **Uso da Derivada para Análise Adicional**:

Derivamos $f(x)$:

$$
 f’(x) = 3x^2 - 4. 
$$

Igualando a zero, encontramos os pontos críticos:

$$
 3x^2 - 4 = 0 \Rightarrow x = \pm \frac{2}{\sqrt{3}} \approx \pm 1.15. 
$$

Como $x = 1.15$ está dentro de $(0,2)$, podemos verificar que a função tem uma mudança no crescimento e pode haver apenas um zero nesse intervalo.

Essas técnicas refinam nossa análise do Teorema de Bolzano, garantindo a existência da raiz e fornecendo ferramentas para localizá-la de forma mais precisa.

3. **Uso de Zeros de Funções para Cálculo de Erro em Redes Neurais**

Em redes neurais, encontrar os zeros de uma função é essencial para minimizar o erro do modelo. Durante o treinamento, buscamos os pontos onde a derivada da função de erro é zero, indicando um possível mínimo. Métodos numéricos, como a descida do gradiente, são usados para ajustar os pesos da rede e reduzir esse erro progressivamente, tornando as previsões mais precisas.
