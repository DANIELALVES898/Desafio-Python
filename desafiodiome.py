menu = """
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite_saque = 500.0
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! Valor do depósito deve ser positivo.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! Valor do saque deve ser positivo.")
        elif valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor > limite_saque:
            print("Operação falhou! Valor do saque excede o limite permitido.")
        elif numero_saques >= limite_saques:
            print("Operação falhou! Número máximo de saques já atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Saindo do sistema. Até a próxima!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção válida..")
