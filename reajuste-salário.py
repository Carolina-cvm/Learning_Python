print('----Calcular o valor do novo salário ---- ')
salario_atual = float(input(f'Informe o salario atual: '))

if (salario_atual < 500):
  salario_novo = salario_atual + (salario_atual * 0.15)
  print(f'Salario com reajuste = {salario_novo}')
  
elif ((salario_atual >= 500) and (salario_atual <= 1000)):
  salario_novo = salario_atual + (salario_atual * 0.10)
  print(f'Salario com reajuste = {salario_novo}')

else: # (salario_atual > 1000)
  salario_novo = salario_atual + (salario_atual * 0.05)
  print(f'Salario com reajuste = {salario_novo}')
