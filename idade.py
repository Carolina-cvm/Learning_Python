idade = int(input(f'Digite sua idade: '))

if 0 <= idade < 12:
  print("De acordo com o Estatuto da Criança e do Adolescente, voce é criança pois sua idade é", idade)
elif 12 <= idade < 18:
  print("De acordo com o Estatuto da Criança e do Adolescente, voce é adolescente pois sua idade é", idade)
elif 18 <= idade <= 29:
  print("De acordo com o Estatuto da Juventude, voce é jovem, pois sua idade é", idade)
elif 30<= idade <=59:
  print("Voce é adulto, pois sua idade é", idade)
else: 
  print("Voce é idoso")
