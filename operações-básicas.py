def soma():
  contasoma = x + y
  print("Você escolheu soma:", x, "+", y, "=", contasoma)


def subtracao():
  contasubtracao = x - y
  print("Você escolheu subtração:", x, "-", y, "=", contasubtracao)


def divisao():
  contadivisao = x / y
  print("Você escolheu divisão:", x, "/", y, "=", contadivisao)


def multiplicacao():
  contamultiplicacao = x * y
  print("Você escolheu multiplicação:", x, "*", y, "=", contamultiplicacao)


conta = input("Qual operação básica? Ex: soma, subtração, multiplicação ou divisão ")
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

try:
  x = int(num1)
  y = int(num2)
except ValueError:
  while num1.isdigit() == False or num2.isdigit() == False:
    print("Digite apenas números!")
    num1 = input("Digite o primeiro número novamente: ")
    num2 = input("Digite o segundo número novamente: ")
    x = int(num1)
    y = int(num2)
  

if conta == "soma" or conta == "Soma":
  soma()
elif conta == "subtracao" or conta == "Subtração" or conta == "subtração":
  subtracao()
elif conta == "divisao" or conta == "Divisão" or conta == "divisão":
  divisao()
elif conta == "multiplicacao" or conta == "Multiplicação" or conta == "multiplicação":
  multiplicacao()
else:
  print("Digite o tipo de conta novamente ")

