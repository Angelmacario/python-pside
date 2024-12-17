import random

num_secreto = random.randint(1,20)
tentativa = 0

while True:
  chute = int(input("Coloque um número entre 1 e 20: "))
  tentativa +=1
  if chute < num_secreto:
    print("Tente um número maior!")
  elif chute > num_secreto:
    print("Tente um número menor!")
  else:
    print(f"Você acertou, com {tentativa} tentativas!!!")
    break


