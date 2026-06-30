# Sistema de Gerenciamento de Ocorrências

Este projeto é um sistema simples em Python para cadastrar, listar, buscar,
ordenar e atender ocorrências/chamados.

O programa carrega uma base inicial de ocorrências a partir do arquivo
`wiwiwi.json` e organiza esses dados usando diferentes estruturas:

- lista, para armazenar todas as ocorrências;
- fila, para atendimento por ordem de chegada;
- fila de prioridade com `heapq`, para atender a maior prioridade primeiro;
- árvore binária, para busca por ID;
- tabela hash manual, para busca por nome e tipo;
- histórico, para registrar algumas ações feitas no sistema.

## Arquivos do projeto

- `teste.py`: arquivo principal do programa.
- `wiwiwi.json`: base inicial de ocorrências.
- `testeste.excalidraw`: rascunho/diagrama visual da ideia do projeto.
- `README.md`: explicação do projeto e instruções de uso.

## Como executar

1. Clone o repositório do GitHub.

```bash
git clone https://github.com/Nath4n-Bandeira/GPI-AED2PR
```

2. Entre na pasta do projeto.

```bash
cd GPI-AED2PR
```

3. Execute o programa com Python.

```bash
python teste.py
```

4. Escolha uma opção no menu.

```text
1 - Cadastrar ocorrência
2 - Listar ocorrências
3 - Buscar ocorrências por nome ou tipo
4 - Buscar ocorrência por ID
5 - Atender por ordem de chegada
6 - Atender maior prioridade
7 - Mostrar histórico
8 - Ordenar por prioridade
9 - Desfazer última ação
0 - Sair
```

## Como funciona

Quando o programa é iniciado, ele lê o arquivo `wiwiwi.json`. Cada ocorrência
recebe automaticamente um ID, uma ordem de chegada e um status inicial chamado
`Aberto`.

Depois disso, cada ocorrência é preparada para diferentes operações:

- entra na lista geral de ocorrências;
- entra na fila comum de atendimento;
- entra na fila de prioridade;
- entra na árvore binária para busca por ID;
- entra na tabela hash de nomes;
- entra na tabela hash de tipos.

## Estruturas utilizadas

### Lista

A lista `ocorrencias` armazena todas as ocorrências cadastradas no sistema.
Ela é usada para listar todos os chamados e para criar novas cópias quando o
programa precisa ordenar por prioridade.

### Fila

A fila `fila` usa `deque` e serve para atender as ocorrências por ordem de
chegada. A primeira ocorrência que entra é a primeira a ser atendida.

### Fila de prioridade

A fila de prioridade `heap` usa o módulo `heapq`. Ela permite atender primeiro
a ocorrência com maior prioridade. Como o `heapq` do Python trabalha com o menor
valor no topo, o programa usa a prioridade negativa para simular o atendimento
da maior prioridade primeiro.

### Árvore binária

A árvore binária é usada para buscar ocorrências pelo ID. IDs menores vão para
a esquerda e IDs maiores vão para a direita.

### Tabela hash

As tabelas `nomes` e `tipos` são usadas para busca por nome e por tipo. O
programa possui uma função de hash chamada `hash133`, que transforma o texto em
uma posição da tabela.

## Principais funções

- `chave(texto)`: padroniza textos para busca.
- `hash133(texto)`: calcula a posição de uma palavra na tabela hash.
- `botarhash(tabela, palavra, ocorrencia)`: insere uma ocorrência na tabela hash.
- `pegarhash(tabela, palavra)`: busca ocorrências dentro da tabela hash.
- `inserirarvore(raiz, ocorrencia)`: insere uma ocorrência na árvore binária.
- `buscararvore(raiz, idbusca)`: busca uma ocorrência pelo ID.
- `adicionaindices(ocorrencia)`: adiciona a ocorrência nos índices de nome e tipo.
- `preparar(ocorrencia)`: coloca a ocorrência em todas as estruturas do sistema.
- `mostrar(ocorrencia)`: exibe os dados de uma ocorrência.
- `cadastrar()`: cadastra uma nova ocorrência.
- `listar()`: lista todas as ocorrências.
- `buscar()`: busca ocorrências por nome ou tipo.
- `buscarid()`: busca uma ocorrência por ID.
- `atenderfila()`: atende a próxima ocorrência da fila comum.
- `atenderprioridade()`: atende a ocorrência de maior prioridade.
- `mostrarhistorico()`: mostra o histórico de ações.
- `desfazerultimaacao()`: remove a última ação registrada no histórico.
- `ordenarprioridade()`: mostra as ocorrências ordenadas por prioridade.
- `menu()`: exibe o menu principal e controla o fluxo do programa.

## Observações

As novas ocorrências cadastradas durante a execução ficam apenas na memória.
Ao fechar o programa, elas não são salvas automaticamente no arquivo
`wiwiwi.json`.

A opção de ordenar por prioridade apenas mostra as ocorrências ordenadas. Ela
não altera a fila comum de atendimento.

A opção de desfazer última ação remove apenas o último registro do histórico.
Ela não desfaz a alteração real feita na ocorrência.