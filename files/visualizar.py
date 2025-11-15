import streamlit as st
import pandas as pd
import os

DATASETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "datasets")

def carregar_arquivo(nome):
    caminho = os.path.join(DATASETS_DIR, nome)
    if os.path.exists(caminho):
        return pd.read_csv(caminho)
    return pd.DataFrame()



def main():

    st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

    st.title("📊 Dashboard Financeiro – Personal Organizer")


    receitas = carregar_arquivo("receitas.csv")
    despesas = carregar_arquivo("despesas.csv")

    
    for df in [receitas, despesas]:
        if df.empty:
            continue
        if "Categoria" not in df.columns:
            df["Categoria"] = "Sem categoria"

    
    total_receitas = receitas["Valor"].sum() if not receitas.empty else 0
    total_despesas = despesas["Valor"].sum() if not despesas.empty else 0
    saldo = total_receitas - total_despesas

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Receitas", f"R$ {total_receitas:.2f}")
    col2.metric("Total Despesas", f"R$ {total_despesas:.2f}")
    col3.metric("Saldo Atual", f"R$ {saldo:.2f}")

    st.divider()

    

    if not despesas.empty:
        categorias = sorted(despesas["Categoria"].unique())
        categoria_selecionada = st.selectbox("Filtrar despesas por categoria:", ["Todas"] + categorias)

        if categoria_selecionada != "Todas":
            despesas_filtradas = despesas[despesas["Categoria"] == categoria_selecionada]
        else:
            despesas_filtradas = despesas
    else:
        despesas_filtradas = pd.DataFrame()

    

    st.subheader(" Tabela de Receitas")
    st.dataframe(receitas if not receitas.empty else pd.DataFrame({"Mensagem": ["Nenhuma receita cadastrada"]}))

    st.subheader(" Tabela de Despesas")
    st.dataframe(despesas_filtradas if not despesas_filtradas.empty else pd.DataFrame({"Mensagem": ["Nenhuma despesa cadastrada"]}))

    st.divider()

    

    if not receitas.empty and not despesas.empty:
        import plotly.express as px

        receitas["Tipo"] = "Receita"
        despesas["Tipo"] = "Despesa"

        df_comb = pd.concat([receitas, despesas])

        fig = px.bar(df_comb, x="Data", y="Valor", color="Tipo", barmode="group",
                     title="Comparativo Receitas x Despesas")

        st.plotly_chart(fig, use_container_width=True)

    

    if not despesas.empty:
        st.subheader(" Gastos por Categoria")

        df_cat = despesas.groupby("Categoria")["Valor"].sum().reset_index()

        fig2 = px.pie(df_cat, names="Categoria", values="Valor", title="Distribuição de Gastos por Categoria")
        st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("Nenhuma despesa cadastrada para gerar gráficos.")


if __name__ == "__main__":
    main()
