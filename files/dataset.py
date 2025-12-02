import os
import csv
import pandas as pd
from funcao import salvar_registro, cadastrar_categoria

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")

def escolher_ou_criar_categoria():
    arquivo_categorias = os.path.join(DATASETS_DIR, "categorias.csv")

    # Se não existir, cria
    if not os.path.exists(arquivo_categorias):
        with open(arquivo_categorias, "w", newline="", encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(["categoria"])

    # Carregar categorias existentes
    categorias = []
    with open(arquivo_categorias, "r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        next(leitor)
        for linha in leitor:
            categorias.append(linha[0])

    print("\n📂 Categorias disponíveis:")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i} - {cat}")
    print("0 - Cadastrar nova categoria")

    escolha = input("Escolha uma categoria: ")

    if escolha == "0":
        cadastrar_categoria(arquivo_categorias)
        return escolher_ou_criar_categoria()  # Recarrega a lista atualizada

    try:
        escolha = int(escolha)
        return categorias[escolha - 1]
    except:
        print("⚠️ Opção inválida! Tente novamente.")
        return escolher_ou_criar_categoria()

def cadastrar_despesa():
    print("\n💸 Cadastro de Despesa")
    descricao = input("Descrição da despesa: ")
    valor = float(input("Valor da despesa: "))
    data = input("Data (DD/MM/AAAA): ")

    categoria = escolher_ou_criar_categoria()

    salvar_registro("despesa", f"{descricao} ({categoria})", valor, data)

def cadastrar_receita():
    print("\n💰 Cadastro de Receita")
    descricao = input("Descrição da receita: ")
    valor = float(input("Valor da receita: "))
    data = input("Data (DD/MM/AAAA): ")

    categoria = escolher_ou_criar_categoria()

    salvar_registro("receita", f"{descricao} ({categoria})", valor, data)

