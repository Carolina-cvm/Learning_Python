notas = []
contador = 1

while contador < 5:
    notas.append(int(input(f'Informe a {contador}ª nota: ')))
    contador += 1

media = sum(notas) / len(notas)
print("Sua média final foi:", media)

if media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')
    
"""
nota1 = int(input("Digite a nota:"))
nota2 = int(input("Digite a nota:"))
nota3 = int(input("Digite a nota:"))
nota4 = int(input("Digite a nota:"))

notas = [nota1,nota2,nota3,nota4]

media = sum(notas) / len(notas)
print("Sua média final foi:", media)

if media >= 7:
    print("Voce está aprovado")
else:
    print("Voce está reprovado")
"""
