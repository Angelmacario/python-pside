num = int(input("Dígite um número: "))
num_primo = True

for teste in range(2, num):
    if num % teste == 0:
        num_primo = False
        break
if num_primo: 
    print(f"{num} é número primo")
else:
    print(f"{num} não é um número primo")
