import os
import csv
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")

os.makedirs(DATASETS_DIR, exist_ok=True)


def salvar_registro(tipo: str, descricao: str, valor: float, data: str):
    arquivo = os.path.join(DATASETS_DIR, f"{tipo}s.csv")

    novo_registro = pd.DataFrame([{
        "Descrição": descricao,
        "Valor": valor,
        "Data": data
    }])

    if os.path.exists(arquivo):
        novo_registro.to_csv(arquivo, mode='a', header=False, index=False, encoding='utf-8')
        print(f"✅ Novo registro de {tipo} adicionado com sucesso.")
    else:
        novo_registro.to_csv(arquivo, index=False, encoding='utf-8')
        print(f"🆕 Arquivo '{tipo}s.csv' criado e {tipo} registrada.")


def calcular_saldo():
    arquivo_receitas = os.path.join(DATASETS_DIR, "receitas.csv")
    arquivo_despesas = os.path.join(DATASETS_DIR, "despesas.csv")

    receitas = pd.read_csv(arquivo_receitas) if os.path.exists(arquivo_receitas) else pd.DataFrame(columns=["Descrição", "Valor", "Data"])
    despesas = pd.read_csv(arquivo_despesas) if os.path.exists(arquivo_despesas) else pd.DataFrame(columns=["Descrição", "Valor", "Data"])

    total_receitas = receitas["Valor"].sum()
    total_despesas = despesas["Valor"].sum()
    saldo = total_receitas - total_despesas

    print("\n📊 --- Resumo Financeiro ---")
    print(f"Total de Receitas: R$ {total_receitas:.2f}")
    print(f"Total de Despesas: R$ {total_despesas:.2f}")
    print(f"💰 Saldo Atual: R$ {saldo:.2f}\n")



def cadastrar_categoria():
    arquivo_categorias = os.path.join(DATASETS_DIR, "categorias.csv")

    if not os.path.exists(arquivo_categorias):
        with open(arquivo_categorias, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["categoria"])

    nova_categoria = input("Digite o nome da nova categoria: ").strip()

    categorias_existentes = []

    with open(arquivo_categorias, "r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        next(leitor)
        for linha in leitor:
            if linha:
                categorias_existentes.append(linha[0].lower())

    if nova_categoria.lower() in categorias_existentes:
        print("❌ Categoria já cadastrada!")
        return

    with open(arquivo_categorias, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow([nova_categoria])

    print(f"✅ Categoria '{nova_categoria}' cadastrada com sucesso!")


def escolher_categoria():
    arquivo_categorias = os.path.join(DATASETS_DIR, "categorias.csv")

    if not os.path.exists(arquivo_categorias):
        with open(arquivo_categorias, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(["categoria"])

    categorias = []

    with open(arquivo_categorias, "r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        next(leitor)
        for linha in leitor:
            categorias.append(linha[0])

    print("\n📂 Categorias:")
    for i, c in enumerate(categorias, start=1):
        print(f"{i} - {c}")
    print("0 - Cadastrar nova categoria")

    escolha = input("Escolha uma categoria: ")

    if escolha == "0":
        cadastrar_categoria()
        return escolher_categoria()

    try:
        escolha = int(escolha)
        return categorias[escolha - 1]
    except:
        print("⚠️ Opção inválida!")
        return escolher_categoria()

def cadastrar_receita():
    print("\n💰 Cadastro de Receita")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    data = input("Data (DD/MM/AAAA): ")

    categoria = escolher_categoria()

    salvar_registro("receita", f"{descricao} ({categoria})", valor, data)


def cadastrar_despesa():
    print("\n💸 Cadastro de Despesa")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    data = input("Data (DD/MM/AAAA): ")

    categoria = escolher_categoria()

    salvar_registro("despesa", f"{descricao} ({categoria})", valor, data)
