import datetime

x = datetime.datetime.now()

print("Hoje é dia:", x.date())
print("Estamos no ano de:", x.year)
print("Estamos no mês de:", x.month)

print(x.strftime("%A,"), x.strftime("%B."))
print(x.strftime("%x"), "-", x.strftime("%X"))
