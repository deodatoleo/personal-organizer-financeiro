import pandas as pd
import os

# Caminho base (sobe uma pasta e entra em datasets)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")

# Garante que a pasta datasets exista
os.makedirs(DATASETS_DIR, exist_ok=True)


# -----------------------------
# Função genérica para salvar dados
# -----------------------------
def salvar_registro(tipo: str, descricao: str, valor: float, data: str):
    """
    Salva um novo registro de receita ou despesa no CSV dentro da pasta datasets.
    """
    # Define o caminho completo do arquivo (datasets/receitas.csv ou datasets/despesas.csv)
    arquivo = os.path.join(DATASETS_DIR, f"{tipo}s.csv")

    # Cria o DataFrame com o novo registro
    novo_registro = pd.DataFrame([{
        "Descrição": descricao,
        "Valor": valor,
        "Data": data
    }])

    # Se o arquivo já existir, adiciona no final
    if os.path.exists(arquivo):
        novo_registro.to_csv(arquivo, mode='a', header=False, index=False, encoding='utf-8')
        print(f"✅ Novo registro de {tipo} adicionado com sucesso.")
    else:
        # Cria o arquivo com cabeçalho
        novo_registro.to_csv(arquivo, index=False, encoding='utf-8')
        print(f"🆕 Arquivo '{tipo}s.csv' criado e {tipo} registrada.")


# -----------------------------
# Função para calcular totais
# -----------------------------
def calcular_saldo():
    """
    Lê os arquivos CSV de receitas e despesas dentro da pasta datasets e calcula o saldo atual.
    """
    # Caminhos dos arquivos
    caminho_receitas = os.path.join(DATASETS_DIR, "receitas.csv")
    caminho_despesas = os.path.join(DATASETS_DIR, "despesas.csv")

    # Se existirem, lê os dados; caso contrário, cria DataFrames vazios
    receitas = pd.read_csv(caminho_receitas) if os.path.exists(caminho_receitas) else pd.DataFrame(columns=["Descrição", "Valor", "Data"])
    despesas = pd.read_csv(caminho_despesas) if os.path.exists(caminho_despesas) else pd.DataFrame(columns=["Descrição", "Valor", "Data"])

    # Calcula os totais
    total_receitas = receitas["Valor"].sum()
    total_despesas = despesas["Valor"].sum()
    saldo = total_receitas - total_despesas

    print("\n📊 --- Resumo Financeiro ---")
    print(f"Total de Receitas: R$ {total_receitas:.2f}")
    print(f"Total de Despesas: R$ {total_despesas:.2f}")
    print(f"💰 Saldo Atual: R$ {saldo:.2f}\n")


# -----------------------------
# Menu interativo
# -----------------------------
def menu():
    while True:
        print("=== CONTROLE FINANCEIRO ===")
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Ver Saldo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da receita: ")
            valor = float(input("Valor: "))
            data = input("Data (YYYY-MM-DD): ")
            salvar_registro("receita", descricao, valor, data)

        elif opcao == "2":
            descricao = input("Descrição da despesa: ")
            valor = float(input("Valor: "))
            data = input("Data (YYYY-MM-DD): ")
            salvar_registro("despesa", descricao, valor, data)

        elif opcao == "3":
            calcular_saldo()

        elif opcao == "0":
            print("Saindo... 👋")
            break

        else:
            print("⚠️ Opção inválida! Tente novamente.")


# -----------------------------
# Execução principal
# -----------------------------
if __name__ == "__main__":
    menu()
