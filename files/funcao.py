import pandas as pd
import os
df = pd.DataFrame(columns=["Descrição", "Valor", "Data", "Saldo"])


def registrar_receita(Descrição, Valor, Data):
    
    novo_registro = {
        "Descrição": Descrição,
        "Valor": Valor,
        "Data": Data,
        "Saldo": Valor
    }

    df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
    df.to_csv("registros_financeiros.csv", index = False)
    print("Receita registrada com sucesso!")

    return registros_financeiros.    
    

    

def registrar_despesa(valor, descricao, data):
    global controle_financeiro
    controle_financeiro["saldo_despesas"]+= valor
    controle_financeiro["despesas"].append({

        "valor": valor,
        "descricao": descricao,
        "data": data
    })
    return controle_financeiro["despesas"], controle_financeiro["saldo_despesas"]