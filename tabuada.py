def tabuada():
  print(f'TABUADA DO {num}')
  contador = 1
  while contador <= 10:
    conta = num * contador
    print(f'{num} x {contador} = {conta}')
    contador += 1

num = int(input(f'Tabuada de qual número? '))
tabuada()
    
