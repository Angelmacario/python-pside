nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(nome)

palavra = "Python"
for letra in palavra:
    print(letra)

texto = input("Informe um texto: ")
VOGAIS = "AEIOU" #Constante

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="") # o and não deixa pular para proxima linha

print()