from datetime import datetime, timedelta
#import datetime

data_atual = datetime.now()

print("Hoje é dia:", data_atual.date())
print("Estamos no ano de:", data_atual.year)
print("Estamos no mês de:", data_atual.month)

# de outra forma
print(data_atual.strftime("%A,"), data_atual.strftime("%B."))
print(data_atual.strftime("%x"), "-", data_atual.strftime("%X"))

# data futura
data_atual = datetime.now()
data_futura = data_atual + timedelta(2)
print("A data daqui dois dias é :", data_futura)
