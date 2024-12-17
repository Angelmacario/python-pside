def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}!")

exibir_mensagem_2("Angélica")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"seja bem vindo {nome}!")

exibir_mensagem_3("Kenai")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([1, 7, 9]))

print(retorna_antecessor_e_sucessor(10))

def funcao():
    print("Olá mundo!")

    # return None

print(funcao())

def salvar_carro(ano, modelo, marca , placa):
    print(f"Carro inserido com sucesso {marca}/{modelo}/{ano}/{placa}")

print(salvar_carro("Fiat", "Pálio", 1999, "ABC1234"))
print(salvar_carro(marca="Fiat", modelo="Pálio", ano=1999, placa="ABC1234"))