def tabuada():
  print("TABUADA DO",num)
  contador = 1
  while contador <= 10:
    conta = num * contador
    print(f'{num} x {contador} = {conta}')
    contador += 1

num = int(input("Tabuada de qual número? "))
tabuada()
    
