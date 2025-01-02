# Operação de Depósito

# Deve ser possível depositar valores positivos nas contas bancárias. A versão 1 desse projeto 
# trabalha com apenas um usuário, então não é necessário se preocupar em identificar o número 
# da agência e conta bancária (faça isso apenas se quiser implementar funções extras em seu projeto, 
# mas não é obrigatório). Todos os depósitos devem ser armazenados em uma variável e exibidos 
# na operação de extrato.
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 3
LIMITE_SAQUES = 3
