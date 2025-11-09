
from funcao import registrar_receita, registrar_despesa, controle_financeiro
import sys
def menu():
   rodar = True
   while rodar == True:
    print("===== Bem vindo ao PersonalOrganizer =======")
    print("====== Escolha uma das opções abaixo: ======")
    print("=====  1 - Adicionar Receita  ==============")
    print("=====  2 - Adicionar Despesas ==============")
    print("=====  3 - Saldo              ==============")
    print("=====  4 - Relatório          ==============")
    print("=====  5 - Sair               ==============")
    sys.stdin.flush()
    escolha = input("== Escolha a opção desejada: ========\n")
    sys.stdin.flush()
    if escolha == "1":
        valor = float(input("Digite o valor da receita: ex: 2000.50 ou 10.00 \n"))
        descricao = input("Digite a descrição da receita: ")
        data = input("Digite a data da receita (DD/MM/AAAA): ex: 25/12/2023 \n")
        registrar_receita(valor, descricao, data)
        print("Receita registrada com sucesso!")
        print("Dejesa voltar ao menu principal?")
        if input("Digite 's' para sim ou qualquer outra tecla para sair: ").lower() != 's':
            print("Saindo do PersonalOrganizer...")
            rodar = False
        else:
            menu()

    elif escolha == "2":
        valor = float(input("Digite o valor da despesa: ex: 2500.50 ou 10.00 \n"))
        descricao = input("Digite a descrição da despesa: \n")
        data = input("Digite a data da despesa (DD/MM/AAAA): ex: 25/12/2023 \n")
        registrar_despesa(valor, descricao, data)
        print("Despesa registrada com sucesso!")
        if input("Digite 's' para sim ou qualquer outra tecla para sair: ").lower() != 's':
            print("Saindo do PersonalOrganizer...")
            rodar = False
            break
        else:
            menu()


    elif escolha == "3":
        print("Exibindo saldo...\n")
        receitas = controle_financeiro["saldo_receitas"]
        despesas = controle_financeiro["saldo_despesas"]
        print("Total de Receitas: R$ {:.2f}".format(receitas))
        print("Total de Despesas: R$ {:.2f}".format(despesas))
        print("Seu saldo atual é de: R$ {:.2f}".format(receitas - despesas))
        if input("Digite 's' para sim ou qualquer outra tecla para sair: ").lower() != 's':
            print("Saindo do PersonalOrganizer...")
            rodar = False
            break
        else:
            menu()
       
    elif escolha == "4":
        print("Exibindo relatório...\n")
        print("Receitas:")
        for receita in controle_financeiro["receitas"]:
            print(f"Data: {receita['data']}, Descrição: {receita['descricao']}, Valor: R$ {receita['valor']:.2f}")
        print("Despesas:")
        for despesa in controle_financeiro["despesas"]:
            print(f"Data: {despesa['data']}, Descrição: {despesa['descricao']}, Valor: R$ {despesa['valor']:.2f}")

        if input("Digite 's' para sim ou qualquer outra tecla para sair: ").lower() != 's':
            print("Saindo do PersonalOrganizer...")
            rodar = False
            break
        else:
            menu()  
          
    elif escolha == "5":
        print("Saindo do PersonalOrganizer...")
        rodar = False
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        menu()

