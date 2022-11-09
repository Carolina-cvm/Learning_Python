name = input("Digite seu nome em letras minúsculas: ")

vogal = ["a", "e", "i", "o", "u"]
consoante = [ "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w","x", "y", "z"]

print("--- VOGAIS ---")
for i in vogal:
  if i in name:
    print(f'Seu nome tem a vogal: {i}')
  else:
    continue

print("--- CONSOANTE ---")
for i in consoante:
  if i in name:
    print(f'Seu nome tem a consoante: {i}')
  else:
    continue
