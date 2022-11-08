listanum = []
contador = 1
while contador < 6:
  listanum.append(int(input("Digite um número: ")))
  contador += 1

listanum.sort() 
print("Os números que voce digitou são:", listanum)
print(f'O menor número é: {listanum[-5]}')
print(f'O maior número é: {listanum[-1]}')

# de outra forma
#print("Menor número:", min(listanum))
#print("Maior número:", max(listanum))
