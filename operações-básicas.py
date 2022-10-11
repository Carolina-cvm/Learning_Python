def soma():
  x = num1
  y = num2
  contasoma = x + y
  print("Você escolheu soma:", x, "+", y, "=", contasoma)
  
def subtracao():
  x = num1
  y = num2
  contasubtracao = x - y
  print("Você escolheu subtração:", x, "-", y, "=", contasubtracao)

def divisao():
  x = num1
  y = num2
  contadivisao = x / y
  print("Você escolheu divisão:", x, "/", y, "=", contadivisao)

def multiplicacao():
  x = num1
  y = num2
  contamultiplicacao = x * y
  print("Você escolheu multiplicação:", x, "*", y, "=", contamultiplicacao)
  
conta = input("Qual operação básica? Ex: soma, subtração, multiplicação ou divisão ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

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


