def adicionar_fruta():
  frutas.append(adc_fruta)
  print(frutas)

def excluir_fruta():
  del(frutas[alterar]) # nao funciona string
  print(frutas)

frutas = ["morango", "uva","melancia"]
print("Esta é a lista de frutas:", frutas)

alterar = input("Quer adicionar ou excluir uma fruta? ")

if alterar == 'adicionar':
  adc_fruta = input("Qual fruta voce quer adicionar? ")
  adicionar_fruta()
elif alterar == 'excluir':
  exc_fruta = input("Qual fruta voce quer excluir? ")
  excluir_fruta()
else:
  print("Algo deu errado, tente novamente mais tarde!")