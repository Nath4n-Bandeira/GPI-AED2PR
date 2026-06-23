import json
from collections import deque


with open("wiwiwi.json", "r", encoding="utf-8") as arq:
    dados = json.load(arq)


ocorrencias = []
fila = deque()
arvore = None
nomes = {}
tipos = {}
historico = []


def chave(texto):
    return texto.strip().casefold()


def inserirarvore(raiz, ocorrencia):
    if raiz is None:
        return {
            "ocorrencia": ocorrencia,
            "esquerda": None,
            "direita": None,
        }

    if ocorrencia["id"] < raiz["ocorrencia"]["id"]:
        raiz["esquerda"] = inserirarvore(raiz["esquerda"], ocorrencia)
    elif ocorrencia["id"] > raiz["ocorrencia"]["id"]:
        raiz["direita"] = inserirarvore(raiz["direita"], ocorrencia)

    return raiz


def buscararvore(raiz, idbusca):
    if raiz is None:
        return None

    idatual = raiz["ocorrencia"]["id"]

    if idbusca == idatual:
        return raiz["ocorrencia"]
    if idbusca < idatual:
        return buscararvore(raiz["esquerda"], idbusca)

    return buscararvore(raiz["direita"], idbusca)


def adicionarindices(ocorrencia):
    nome = chave(ocorrencia["nome"])
    tipo = chave(ocorrencia["tipo"])

    if nome not in nomes:
        nomes[nome] = []
    nomes[nome].append(ocorrencia)

    if tipo not in tipos:
        tipos[tipo] = []
    tipos[tipo].append(ocorrencia)


def preparar(ocorrencia):
    global arvore

    ocorrencia["status"] = ocorrencia.get("status", "Aberto")
    ocorrencias.append(ocorrencia)
    fila.append(ocorrencia)
    arvore = inserirarvore(arvore, ocorrencia)
    adicionarindices(ocorrencia)


for pos, item in enumerate(dados, start=1):
    registro = item.copy()
    registro["id"] = pos
    preparar(registro)


def mostrar(ocorrencia):
    print("ID:", ocorrencia["id"])
    print("Nome:", ocorrencia["nome"])
    print("Tipo:", ocorrencia["tipo"])
    print("Descrição:", ocorrencia["descricao"])
    print("Prioridade:", ocorrencia["prioridade"])
    print("Status:", ocorrencia["status"])


def cadastrar():
    print("\nCADASTRO")

    nome = input("Nome do requisitante: ")
    tipo = input("Tipo da ocorrência: ")
    descricao = input("Descrição: ")

    while True:
        prioridade = input("Prioridade de 1 a 5: ").strip()
        if prioridade in ["1", "2", "3", "4", "5"]:
            break
        print("Prioridade inválida")

    ocorrencia = {
        "id": len(ocorrencias) + 1,
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Aberto",
    }

    preparar(ocorrencia)
    historico.append(f"Cadastro da ocorrência ID {ocorrencia['id']}")

    print("\nOcorrência cadastrada")
    mostrar(ocorrencia)


def listar():
    print("\nOCORRÊNCIAS")

    if not ocorrencias:
        print("Nenhuma ocorrência cadastrada.")
        return

    for ocorrencia in ocorrencias:
        mostrar(ocorrencia)
        print("-" * 20)


def buscar():
    print("\nBUSCA")
    print("1 - Nome")
    print("2 - Tipo")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        termo = chave(input("Digite o nome do solicitante: "))
        resultados = nomes.get(termo, [])
    elif opcao == "2":
        termo = chave(input("Digite o tipo da ocorrência: "))
        resultados = tipos.get(termo, [])
    else:
        print("Opção inválida")
        return []

    if not resultados:
        print("Nenhuma ocorrência encontrada")
        return []

    print(f"\n{len(resultados)} ocorrência(s) encontrada(s):")
    for ocorrencia in resultados:
        print("-" * 20)
        mostrar(ocorrencia)

    return resultados


def buscarid():
    print("\nBUSCA POR ID")

    try:
        idbusca = int(input("Digite o ID da ocorrência: "))
    except ValueError:
        print("Digite um número")
        return None

    resultado = buscararvore(arvore, idbusca)

    if resultado is None:
        print("Ocorrência não encontrada")
        return None

    print("\nOcorrência encontrada")
    mostrar(resultado)
    return resultado


def atenderfila():
    print("\nATENDIMENTO POR FILA")

    while fila and fila[0]["status"] == "Atendido":
        fila.popleft()

    if not fila:
        print("A fila está vazia")
        return None

    ocorrencia = fila.popleft()
    ocorrencia["status"] = "Atendido"
    historico.append(f"Atendimento da ocorrência ID {ocorrencia['id']} pela fila")

    print("\nOcorrência atendida")
    mostrar(ocorrencia)
    return ocorrencia


def mostrarhistorico():
    print("\nHISTÓRICO")

    if not historico:
        print("Histórico vazio")
        return []

    for pos, acao in enumerate(reversed(historico), start=1):
        print(f"{pos} - {acao}")

    return historico


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar ocorrência")
        print("2 - Listar ocorrências")
        print("3 - Buscar ocorrências por nome ou tipo")
        print("4 - Buscar ocorrência por ID")
        print("5 - Atender por ordem de chegada")
        print("6 - Mostrar histórico")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            buscarid()
        elif opcao == "5":
            atenderfila()
        elif opcao == "6":
            mostrarhistorico()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
