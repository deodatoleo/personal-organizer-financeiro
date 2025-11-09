import pandas as pd
import plotly.graph_objects as go
import os

# Caminhos das pastas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS_DIR = os.path.join(BASE_DIR, "datasets")

# Caminhos dos arquivos CSV
caminho_receitas = os.path.join(DATASETS_DIR, "receitas.csv")
caminho_despesas = os.path.join(DATASETS_DIR, "despesas.csv")

# --- Leitura segura dos CSVs ---
def carregar_dados():
    receitas = pd.read_csv(caminho_receitas) if os.path.exists(caminho_receitas) else pd.DataFrame(columns=["Descrição", "Valor", "Data"])
    despesas = pd.read_csv(caminho_despesas) if os.path.exists(caminho_despesas) else pd.DataFrame(columns=["Descrição", "Valor", "Data"])

    # Converte Data em formato datetime (para ordenação correta no gráfico)
    if not receitas.empty:
        receitas["Data"] = pd.to_datetime(receitas["Data"])
    if not despesas.empty:
        despesas["Data"] = pd.to_datetime(despesas["Data"])
    
    return receitas, despesas


# --- Cria o gráfico interativo ---
def gerar_grafico(receitas, despesas):
    fig = go.Figure()

    if not receitas.empty:
        fig.add_trace(go.Scatter(
            x=receitas["Data"],
            y=receitas["Valor"],
            mode="lines+markers",
            name="Receitas",
            line=dict(color="green")
        ))

    if not despesas.empty:
        fig.add_trace(go.Scatter(
            x=despesas["Data"],
            y=despesas["Valor"],
            mode="lines+markers",
            name="Despesas",
            line=dict(color="red")
        ))

    fig.update_layout(
        title="📊 Evolução Financeira - Receitas x Despesas",
        xaxis_title="Data",
        yaxis_title="Valor (R$)",
        template="plotly_white",
        hovermode="x unified"
    )

    fig.show()


# --- Execução principal ---
if __name__ == "__main__":
    receitas, despesas = carregar_dados()
    gerar_grafico(receitas, despesas)
