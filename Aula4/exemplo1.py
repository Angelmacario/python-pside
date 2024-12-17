saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

# if saldo <= saque:
else:
    print("Saldo insuficiente!")

opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque"))

elif opcao == 2:
    print("Exibindo o extrato...")

else: 
    sys.exit("Opção inválida")

status = "Sucesso" if saldo >= saque else "Falsa"

print(f"{status} ao realizar o saque!")