def adicionar_num():
  lista.append(adc_num)
  print(f'Agora esta é a lista de números: {lista}')

def excluir_num():
  del(lista[exc_num])
  print(f'Agora esta é a lista de números: {lista}')

lista = [1,2,3,4,5]
print(f'Esta é a lista de números: {lista}')

alterar = input(f'Quer adicionar ou excluir um número? ')

if alterar == 'adicionar':
  adc_num = int(input(f'Qual numero voce quer adicionar? '))
  adicionar_num()
elif alterar == 'excluir':
  exc_num = int(input(f'Qual a posição do numero que voce quer excluir? '))
  excluir_num()
else:
  print(f'Algo deu errado, tente novamente mais tarde!')
