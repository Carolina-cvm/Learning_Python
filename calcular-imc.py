# >=	Maior ou igual que
# <=	Menor ou igual que

print("Cálculo de IMC")
peso = int(input(f'Digite seu peso em quilos: '))
altura = float(input(f'Digite sua altura em metros: '))

imc = (peso) / (altura * altura)
print(f'Seu IMC é: {round(imc,2)}')

if imc < 18.50:
  print(f'Classificação: Abaixo do peso')
elif 18.60 <= imc <= 24.90:
  print(f'Classificação: Peso ideial')
elif 25.00 <= imc <= 29.90:
  print(f'Classificação: Levemente acima do peso')
elif 30.00 <= imc <= 34.90:
  print(f'Classificação: Obesidade grau I')
elif 35.00 <= imc <= 39.90:
  print("Classificação: Obesidade grau II (severa)")
else: #acima de 40
  print("Classificação: Obesidade III (mórbida)")
