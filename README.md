# Sistema de Gerenciamento de Ocorrências

Este projeto é um sistema simples em Python para cadastrar, listar, buscar,
ordenar e atender ocorrências/chamados.

O programa carrega uma base inicial de ocorrências a partir do arquivo
`wiwiwi.json` e organiza esses dados em diferentes estruturas:

- lista, para armazenar todas as ocorrências;
- fila, para atendimento por ordem de chegada;
- árvore binária, para busca por ID;
- dicionários, para busca por nome e tipo;
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
6 - Mostrar histórico
7 - Ordenar por prioridade
0 - Sair
```

## Como funciona

Quando o programa é iniciado, ele lê o arquivo `wiwiwi.json`. Cada ocorrência
recebe automaticamente um ID e um status inicial chamado `Aberto`.

Depois disso, cada ocorrência é preparada para diferentes operações:

- entra na lista geral de ocorrências;
- entra na fila de atendimento;
- entra na árvore binária para busca por ID;
- entra nos índices de busca por nome e tipo.

## Principais funções

- `chave(texto)`: padroniza textos para busca.
- `inserir_arvore(raiz, ocorrencia)`: insere uma ocorrência na árvore binária.
- `buscar_arvore(raiz, idbusca)`: busca uma ocorrência pelo ID.
- `adicionar_indices(ocorrencia)`: adiciona a ocorrência nos índices de nome e tipo.
- `preparar(ocorrencia)`: coloca a ocorrência em todas as estruturas do sistema.
- `mostrar(ocorrencia)`: exibe os dados de uma ocorrência.
- `cadastrar()`: cadastra uma nova ocorrência.
- `listar()`: lista todas as ocorrências.
- `buscar()`: busca ocorrências por nome ou tipo.
- `buscar_id()`: busca uma ocorrência por ID.
- `atender_fila()`: atende a próxima ocorrência da fila.
- `mostrar_historico()`: mostra o histórico de ações.
- `ordenar_por_prioridade()`: mostra as ocorrências ordenadas por prioridade.
- `menu()`: exibe o menu principal e controla o fluxo do programa.

## Observações

As novas ocorrências cadastradas durante a execução ficam apenas na memória.
Ao fechar o programa, elas não são salvas automaticamente no arquivo
`wiwiwi.json`.

A ordenação por prioridade apenas mostra as ocorrências ordenadas. Ela não
altera a fila de atendimento.