def adicionar_fruta():
  frutas.append(adc_fruta)
  print(f'Voce adicionou {adc_fruta}, esta é a lista de frutas {frutas}')

frutas = ["morango", "uva", "melancia"]
print(f'Esta é a lista de frutas: {frutas}')

escolha = input(f'Quer adicionar uma fruta? ')

if escolha == 'adicionar' or escolha == 'sim':
  adc_fruta = input(f'Qual fruta voce quer adicionar? ')
  adicionar_fruta()
else:
  print(f'Algo deu errado, tente novamente mais tarde!')
