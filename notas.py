notas = []

nota1 = int(input(f'Digite a primeira nota: '))
nota2 = int(input(f'Digite a segunda nota: '))
nota3 = int(input(f'Digite a terceira nota: '))
nota4 = int(input(f'Digite a quarta nota: '))

notas.append(nota1, nota2, nota3, nota4)

media = sum(notas) / len(notas)
print("Sua média final foi:", media)

if media >= 7:
  print("Voce está aprovado")
else:
  print("Voce está reprovado")

"""
# de outra forma
notas = []
contador = 1

while contador < 5:
    notas.append(int(input(f'Informe a {contador}ª nota: ')))
    contador += 1
"""
