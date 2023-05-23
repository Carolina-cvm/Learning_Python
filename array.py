colors = ["Marrom", "Vermelho", "Preto"]

print(colors) # Marrom Vermelho Preto

x = colors[0]
print(x) # marrom

y = len(colors)
print(y) # 3

for z in colors:
  print(z) # Marrom Vermelho Preto
  
colors.append("Roxo")
print(colors) # Marrom Vermelho Preto Roxo

colors.pop(1)
print(colors) # Marrom Preto Roxo

colors.remove("Preto")
print(colors) # Marrom Roxo
