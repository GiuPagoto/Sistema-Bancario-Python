menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        valor_depositado = int(input("Informe o valor que deseja depositar em sua conta: R$ "))

        if valor_depositado > 0:
            saldo = saldo + valor_depositado
            print("Depósito realizado com sucesso!")

        else:
            print("Não é possível depositar valores negativos.")
    
    elif opcao == "s":
        print("Saque")

        valor_saque = int(input("Informe o valor que deseja sacar da sua conta: R$ "))

        if (saldo >= valor_saque) and (limite >= valor_saque) and (LIMITE_SAQUES >= numero_saques):
            print("Saque realizado com sucesso!")
            numero_saques += 1
            LIMITE_SAQUES -= 1

        elif valor_saque > saldo:
            print("Não foi possível realizar o saque, pois não há saldo suficiente.")
    
    elif opcao == "e":
        print("Extrato")

        print(f"Saldo: {saldo:.2f} Depósito: {valor_depositado:.2f} Saque:{valor_saque:.2f}")

    elif opcao == "q":
        break 

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")