menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao  = input(menu)
    if opcao == "d":
        deposito = float(input("Valor do Deposito:"))
        if deposito > 0:
            saldo  += deposito
            extrato += f"\n Deposito: R$ {deposito:.2f}".center(25," ") 
            print(f"Depositado: R$ {deposito:.2f}")
        else:
            print("Operação não realizada Deposito deve ser maior que 0!!")

    elif opcao == "s":
        saque = float(input("Valor do Saque:"))
        if saque > limite:
            print("Operação não realizada limite do Saque é: R# 500,00!!")
        elif saldo < saque:
            print(f"Operação não realizada Sem saldo Suficiente: Saldo R$ {saldo:.2f}")

        elif numero_saques >= LIMITE_SAQUES :
            print("Operação não realizada núnmero de saques diário já efetuados!")
        else:
            numero_saques+=1
            saldo -= saque
            extrato += f"\n Saque: R$ {saque:.2f}".center(25," ") 


    elif opcao == "e":
        print("Extrato".center(25,"="))
        print(extrato + f"\n Saldo: R$ {saldo:.2f}".center(25," ")) 
        print("".center(25,"="))
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")       