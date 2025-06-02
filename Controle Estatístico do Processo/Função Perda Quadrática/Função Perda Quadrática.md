---
dg-publish: true
---

%% Begin Waypoint %%
- **[[Função Perda Quadrática]]**

%% End Waypoint %%

## Perda Quadrática no Controle Estatístico Do Processo

A **função de perda quadrática** foi proposta por **Genichi Taguchi** e é usada para quantificar a perda de qualidade causada por variações no processo, mesmo quando o produto está dentro das especificações. Diferente da abordagem tradicional do CEP, que considera um produto "bom" se ele estiver dentro dos limites de especificação, Taguchi defende que **qualquer desvio da meta (valor nominal)** implica em perda para o cliente ou para a sociedade.

### Forma da Função de Perda

A função de perda quadrática é expressa como:

$$
L(y) = k (y - T)^2
$$

Onde:

- $L(y)$: perda associada ao valor $y$
- $T$: valor-alvo ou valor nominal do processo (meta)
- $y$: valor real observado do processo
- $k$: constante de proporcionalidade (depende do custo associado à não conformidade)

Essa função mostra que a perda aumenta quadraticamente conforme o valor $y$ se afasta da meta $T$, independentemente de estar ou não dentro dos limites de especificação.

### Importância no Cep

A função de perda reforça a ideia de que a **melhoria contínua** deve ser um objetivo central. Mesmo pequenas variações dentro das especificações podem causar impacto no desempenho, custo ou satisfação do cliente. Assim, não basta manter o processo "dentro dos limites", é desejável que ele esteja **centrado na meta** e com **baixa variabilidade**.

### Exemplo de Aplicação

Suponha que o diâmetro ideal de uma peça seja $T = 10 \, \text{mm}$. Dois lotes produzem peças entre 9,8 mm e 10,2 mm, dentro dos limites aceitáveis. Porém:

- Lote A tem a maioria das peças em torno de 10 mm (bem centrado).
- Lote B tem grande variabilidade (mais peças afastadas de 10 mm).

Mesmo que ambos estejam "conformes", o Lote B gera maior perda (mais produtos com desempenho inferior), o que pode significar maior desgaste, falhas ou custo para o cliente.

### Conclusão

A perda quadrática reforça a visão de que a **qualidade deve ser medida em termos de desempenho em torno de uma meta**, e não apenas pela conformidade com limites. Essa abordagem incentiva a **redução da variabilidade** e o **aperfeiçoamento contínuo dos processos**.
