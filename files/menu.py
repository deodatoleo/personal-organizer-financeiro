from funcao import (
    cadastrar_receita,
    cadastrar_despesa,
    cadastrar_categoria,
    calcular_saldo
)

def menu():
    while True:
        print("\n===== PERSONAL ORGANIZER =====")
        print("1 - Cadastrar Receita")
        print("2 - Cadastrar Despesa")
        print("3 - Cadastrar Categoria")
        print("4 - Ver Saldo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_receita()
        elif opcao == "2":
            cadastrar_despesa()
        elif opcao == "3":
            cadastrar_categoria()
        elif opcao == "4":
            calcular_saldo()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")
