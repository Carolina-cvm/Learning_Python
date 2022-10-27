name = input("Digit seu nome: ")

vogal = ["a", "e", "i", "o", "u"]
consoante = [ "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w","x", "y", "z"]

for i in vogal:
  if i in name:
    print("Seu nome tem a vogal:", i)
  else:
    print("Seu nome não tem a vogal:", i)


for i in consoante:
  if i in name:
    print("Seu nome tem a consoante:", i)
  else:
    print("Seu nome não tem a consoante:", i)
