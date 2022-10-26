def antecessor():
  conta = num - 1
  print("O antecessor de", num, "é:", conta)

def sucessor():
  conta = num + 1
  print("O sucessor de", num, "é:", conta)

num = int(input("Digite um número: "))
antecessor()
sucessor()

# de outra forma
#print(f'O antecessor do número {num} é {num - 1}, e seu sucessor é {num + 1}')