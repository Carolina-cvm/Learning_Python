def par_ou_impar():
  if numero % 2 == 0:
    print(f'{numero} é número par')
  else:
    print(f'{numero} é número impar')

numero = int(input(f'Informe um número inteiro qualquer: '))
par_ou_impar()

