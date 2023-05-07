saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    
    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: "))
        if numero_saques < LIMITE_SAQUES:
            if valor_saque > 0 and valor_saque <= limite and saldo >= valor_saque:
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
            elif valor_saque > limite:
                print(f"O valor máximo por saque é R$ {limite:.2f}.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Limite diário de saques atingido.")
    
    elif opcao == "e":
        print("--- Extrato ---")
        if extrato:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")
    
    elif opcao == "q":
        break 
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
