import random
import string

# Define o conjunto de caracteres permitidos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Define o comprimento da senha
comprimento = 8

# Gera a senha
senha = ''.join(random.choice(caracteres) for i in range(comprimento))

# Exibe a senha
print(senha)
