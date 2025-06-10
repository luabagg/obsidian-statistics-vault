---
dg-publish: true
---

A **fatoração LU** é um método direto para resolver sistemas lineares, calcular determinantes e inverter matrizes. Consiste em decompor uma matriz quadrada $A$ como o produto de duas matrizes triangulares:

$$
A = LU
$$

onde:

- $L$ é uma **matriz triangular inferior**, com 1s na diagonal principal ($l_{ii} = 1$);
- $U$ é uma **matriz triangular superior** (pode conter qualquer valor na diagonal).

Essa fatoração permite reescrever o sistema $Ax = b$ como:

$$
LUx = b \Rightarrow Ly = b \Rightarrow Ux = y
$$

resolvendo-se primeiro por **substituição direta** ($Ly = b$) e depois por **substituição retroativa** ($Ux = y$).

---

## Requisitos para a Fatoração Lu

A fatoração LU **sem pivoteamento** só é possível se todos os **pivôs parciais** (valores $U[i, i]$) forem **não nulos**. Caso contrário, é necessário realizar **pivoteamento parcial** para garantir a estabilidade numérica e evitar divisões por zero.

A **fatoração LU** é um método que decompõe uma matriz quadrada $A$ como o produto de duas matrizes triangulares:

$$
A = LU
$$

onde:

- $L$ é uma **matriz triangular inferior** com 1s na diagonal principal.
- $U$ é uma **matriz triangular superior**.

---

## Passo a Passo da Fatoração Lu (sem pivoteamento)

Seja $A$ uma matriz quadrada de ordem $n$.

### Eliminação de Gauss para Formar $U$ e Preencher $L$

Para cada linha $i = 0$ até $n - 1$:

- Para cada linha $j = i + 1$ até $n - 1$:
  1. Calcule o **fator multiplicador**:
$$
m = \frac{U[j, i]}{U[i, i]}
$$
  2. Subtraia $m$ vezes a linha $i$ da linha $j$ em $U$:
$$
U[j] \leftarrow U[j] - m \cdot U[i]
$$
  3. Atribua esse multiplicador à posição $L[j, i]$:
$$
L[j, i] = m
$$

### Exemplo Numérico

Considere a matriz $A$:

$$
A = \begin{pmatrix}
2 & 3 & 1 \\
4 & 7 & 7 \\
6 & 18 & 22
\end{pmatrix}
$$

#### Iteração $i = 0$

- $m_{10} = 4/2 = 2$
- Linha 1: $U[1] = U[1] - 2 \cdot U[0]$
- $L[1, 0] = 2$
- $m_{20} = 6/2 = 3$
- Linha 2: $U[2] = U[2] - 3 \cdot U[0]$
- $L[2, 0] = 3$

#### Iteração $i = 1$

- $m_{21} = (U[2, 1]) / (U[1, 1]) = 9 / 1 = 9$
- Linha 2: $U[2] = U[2] - 9 \cdot U[1]$
- $L[2, 1] = 9$

#### Resultado Final

$$
L = \begin{pmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
3 & 9 & 1
\end{pmatrix}
$$

$$
U = \begin{pmatrix}
2 & 3 & 1 \\
0 & 1 & 5 \\
0 & 0 & 2
\end{pmatrix}
$$

## Pivoteamento Parcial na Fatoração Lu

O **pivoteamento parcial** é uma técnica utilizada na fatoração LU para **evitar divisões por zero** e **minimizar erros numéricos** causados por pivôs pequenos. Ele consiste em **trocar linhas da matriz** $A$ (e consequentemente de $L$ e $b$, se estiver resolvendo $Ax = b$) de modo que o maior valor absoluto na coluna corrente seja usado como pivô.

### Passo a Passo com Pivoteamento Parcial

Dado $A \in \mathbb{R}^{n \times n}$, o algoritmo com pivoteamento parcial segue:

#### 1. Inicialização

- Crie $L = I_n$ (matriz identidade), $U = A.copy()$, e $P = I_n$ (matriz de permutação).

#### 2. Para Cada Coluna $i$ de $0$ Até $n-1$

1. **Escolha do Pivô:**

   - Encontre o índice da linha com o maior valor absoluto na coluna $i$, a partir da linha $i$:
$$
p = \arg\max_{k \geq i} |U[k, i]|
$$
1. **Troque as linhas $i$ e $p$ de $U$ e $P$:**

   - $U[[i, p], :] \leftarrow U[[p, i], :]$

   - $P[[i, p], :] \leftarrow P[[p, i], :]$

   - Se $i > 0$, troque as linhas anteriores de $L$ também:

     - $L[[i, p], :i] \leftarrow L[[p, i], :i]$

1. **Eliminação de Gauss como antes:**

   - Para cada linha $j > i$:

     - $m = U[j, i] / U[i, i]$

     - $U[j] = U[j] - m \cdot U[i]$

     - $L[j, i] = m$

### Forma Final da Decomposição com Pivoteamento

A fatoração LU com pivoteamento parcial produz:

$$
PA = LU
$$
- $P$ é a **matriz de permutação** que representa as trocas de linha.
- $L$ é a matriz triangular inferior com 1s na diagonal.
- $U$ é a matriz triangular superior.

---

## Validação da Fatoração

A multiplicação $LU$ deve recuperar a matriz original:

$$
LU = \begin{pmatrix}

1 & 0 & 0 \\

2 & 1 & 0 \\

3 & 9 & 1

\end{pmatrix}

\begin{pmatrix}

2 & 3 & 1 \\

0 & 1 & 5 \\

0 & 0 & 2

\end{pmatrix}

= A
$$

## Observações

- A fatoração LU **não é única** se não houver restrição em $L$ ou $U$.
- A convenção comum é impor que $L$ tenha 1s na diagonal.
- O método **é eficiente** para sistemas lineares com múltiplos vetores $b$, pois o custo da fatoração ($O(n^3)$) é feito uma única vez

## Exemplo em Python com Pivoteamento

```python
import numpy as np

def lu_decomposition_pivot(A):
    """
    Perform LU decomposition with partial pivoting on matrix A.
    Decomposes PA = LU, where P is a permutation matrix, L is lower triangular, and U is upper triangular.

    Parameters:
    A -- Square matrix (numpy.ndarray)

    Returns:
    P -- Permutation matrix (numpy.ndarray)
    L -- Lower triangular matrix (numpy.ndarray)
    U -- Upper triangular matrix (numpy.ndarray)
    """
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy().astype(float)
    P = np.eye(n)

    for i in range(n):
		# Find The Index Of The Row With The Largest Absolute Value In Column I
        pivot = np.argmax(np.abs(U[i:, i])) + i
        if U[pivot, i] == 0:
            raise ValueError("Singular matrix.")
		# Swap Rows In U
        U[[i, pivot]] = U[[pivot, i]]
		# Swap Rows In P
        P[[i, pivot]] = P[[pivot, i]]
		# Swap Rows In L (only For Previously Computed columns)
        if i > 0:
            L[[i, pivot], :i] = L[[pivot, i], :i]
		# Elimination Process
        for j in range(i+1, n):
            m = U[j, i] / U[i, i]
            L[j, i] = m
            U[j] = U[j] - m * U[i]
    return P, L, U

def solve_with_lu(P, L, U, b):
    """
    Solve the linear system Ax = b using LU decomposition with pivoting.

    Parameters:
    P, L, U -- The factors of A such that PA = LU
    b -- The right-hand side vector

    Returns:
    result -- Dictionary with keys:
        'solution'   : Solution vector (numpy.ndarray)
        'residual'   : Final residual norm (float)
    """
	# Step 1: Apply The Permutation To B
    Pb = np.dot(P, b)

	# Step 2: Forward Substitution To Solve Ly = Pb
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = Pb[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]

	# Step 3: Back Substitution To Solve Ux = Y
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    residual = np.linalg.norm(np.dot(A, x) - b, ord=np.inf) if 'A' in globals() else None
    return {'solution': x, 'residual': residual}

if __name__ == "__main__":
	# Example Usage
    A = np.array([
        [0, 3, 1],
        [4, 7, 7],
        [6, 18, 22]
    ], dtype=float)
    P, L, U = lu_decomposition_pivot(A)
    print("P =\n", P)
    print("\nL =\n", L)
    print("\nU =\n", U)
    print("\nVerification: P·A =\n", np.dot(P, A))
    print("\nL·U =\n", np.dot(L, U))
	# Define a Right-hand Side Vector B
    b = np.array([2, 4, 3], dtype=float)
	# Solve The System Ax = B
    result = solve_with_lu(P, L, U, b)
    print("\nSolution x =\n", result['solution'])
    print("\nFinal residual norm =", result['residual'])
    print("\nVerification: A·x =\n", np.dot(A, result['solution']))
```

## Resolução de Sistemas com Fatoração Lu

Após decompor a matriz $A$ em $A = LU$, podemos resolver o sistema linear $Ax = b$ em **duas etapas**:

1. Resolver o sistema intermediário $Ly = b$ (**substituição para frente**)
2. Resolver o sistema $Ux = y$ (**substituição para trás**)

Esse processo é eficiente porque $L$ e $U$ são matrizes triangulares, o que permite resolver os sistemas de forma sequencial, sem necessidade de inversão de matrizes.

---

### 1. Resolver $Ly = b$ (Substituição para Frente)

Seja $L$ uma matriz triangular inferior com 1s na diagonal:

$$
L = \begin{pmatrix}
1 & 0 & 0 \\
\ell_{21} & 1 & 0 \\
\ell_{31} & \ell_{32} & 1
\end{pmatrix}, \quad
b = \begin{pmatrix}
b_1 \\
b_2 \\
b_3
\end{pmatrix}
$$

Resolvemos sequencialmente:

- $y_1 = b_1$
- $y_2 = b_2 - \ell_{21} y_1$
- $y_3 = b_3 - \ell_{31} y_1 - \ell_{32} y_2$

Mais genericamente:

$$
y_i = b_i - \sum_{j=1}^{i-1} L_{i,j} y_j
$$

---

### 2. Resolver $Ux = y$ (Substituição para Trás)

Seja $U$ uma matriz triangular superior:

$$
U = \begin{pmatrix}
u_{11} & u_{12} & u_{13} \\
0 & u_{22} & u_{23} \\
0 & 0 & u_{33}
\end{pmatrix}, \quad
y = \begin{pmatrix}
y_1 \\
y_2 \\
y_3
\end{pmatrix}
$$

Resolvemos de trás para frente:

- $x_3 = y_3 / u_{33}$
- $x_2 = (y_2 - u_{23} x_3) / u_{22}$
- $x_1 = (y_1 - u_{12} x_2 - u_{13} x_3) / u_{11}$

Mais genericamente:

$$
x_i = \frac{1}{U_{i,i}} \left( y_i - \sum_{j=i+1}^{n} U_{i,j} x_j \right)
$$

---

### Exemplo Numérico

Considere a decomposição:

$$
L = \begin{pmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
3 & 9 & 1
\end{pmatrix}, \quad
U = \begin{pmatrix}
2 & 3 & 1 \\
0 & 1 & 5 \\
0 & 0 & 2
\end{pmatrix}, \quad
b = \begin{pmatrix}
1 \\
2 \\
3
\end{pmatrix}
$$

#### Etapa 1: Resolver $Ly = b$

- $y_1 = 1$
- $y_2 = 2 - 2 \cdot 1 = 0$
- $y_3 = 3 - 3 \cdot 1 - 9 \cdot 0 = 0$

Logo,

$$
y = \begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix}
$$

#### Etapa 2: Resolver $Ux = y$

- $x_3 = 0 / 2 = 0$
- $x_2 = (0 - 5 \cdot 0) / 1 = 0$
- $x_1 = (1 - 3 \cdot 0 - 1 \cdot 0) / 2 = 0.5$

Logo,

$$
x = \begin{pmatrix}
0.5 \\
0 \\
0
\end{pmatrix}
$$

