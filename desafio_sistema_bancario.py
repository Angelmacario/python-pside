# Operação de Depósito

# Deve ser possível depositar valores positivos nas contas bancárias. A versão 1 desse projeto 
# trabalha com apenas um usuário, então não é necessário se preocupar em identificar o número 
# da agência e conta bancária (faça isso apenas se quiser implementar funções extras em seu projeto, 
# mas não é obrigatório). Todos os depósitos devem ser armazenados em uma variável e exibidos 
# na operação de extrato.

# Menu Principal
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis e Configurações Iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# estrutura principal: 
while True:                      # Mantém o programa aberto para entrada do usuario
    opcao = input(menu) #.lower # letras minusculas

# Opção de Depósito:

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: 
            saldo += valor # soma o valor no saldo
            extrato += f"Depósito: R$ {valor:.2f}\n" # atualiza o extrato
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        
        else: 
            print("Valor inválido. Por favor insira um valor positivo.")

# Opção de Saque:
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo: 
            print("Saldo insuficiente!")

        elif valor > limite:
            print(f"O valor excede o limite de saque de R$ {limite:.2f}!")

        elif numero_saques >= LIMITE_SAQUES:
            print("Você atingiu seu limite de saques diários!")
        
        elif valor > 0:
            saldo -= valor # subtrai o valor no saldo
            extrato += f"Saque: R${valor:.2f}\n" # atualiza o extrato
            numero_saques += 1 # adiciona um contrato ao saque diario
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            
        else:
            print("Valor inválido. Por favor, insira um valor positivo.")

# Opção de Extrato:
    elif opcao == "e":
        print("\n ====================== EXTRATO ========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    if opcao == "q":
        print("Obrigada por usar o sitema bancário. Até logo!")
        break

