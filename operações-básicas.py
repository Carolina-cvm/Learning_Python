def soma():
  contasoma = x + y
  print(f'Voce escolheu soma: {x} + {y} = {contasoma}')


def subtracao():
  contasubtracao = x - y
  print(f'Voce escolheu subtração: {x} - {y} = {contasubtracao}')



def divisao():
  contadivisao = x / y
  print(f'Voce escolheu divisão: {x} / {y} = {contadivisao}')


def multiplicacao():
  contamultiplicacao = x * y
  print(f'Voce escolheu multiplicação: {x} * {y} = {contamultiplicacao}')

def fazconta():
  if conta == "soma" or conta == "Soma":
    soma()
  elif conta == "subtracao" or conta == "Subtração" or conta == "subtração":
    subtracao()
  elif conta == "divisao" or conta == "Divisão" or conta == "divisão":
    divisao()
  elif conta == "multiplicacao" or conta == "Multiplicação" or conta == "multiplicação":
    multiplicacao()
  else:
    print(f'Algo deu errado!')

conta = input("Qual operação básica? Ex: soma, subtração, multiplicação ou divisão ")
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

while num1 != 0 and num2 != 0:
  try:
    x = int(num1)
    y = int(num2)
  except:
    print("---Digite apenas números!---")
    num1 = input(f'Digite o primeiro numero: ')
    num2 = input(f'Digite o segundo numero: ')
  else:
    fazconta()
    break
