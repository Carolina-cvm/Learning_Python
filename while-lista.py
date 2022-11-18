listanum = []
contador = 1
while contador < 6:
  listanum.append(int(input(f'Digite um número: ')))
  contador += 1

listanum.sort() 
print(f'Os números que voce digitou são: {listanum}')
print(f'O menor número é: {listanum[-5]}')
print(f'O maior número é: {listanum[-1]}')

# de outra forma
#print(f'Menor número: {min(listanum)}')
#print("Maior número:", max(listanum))
