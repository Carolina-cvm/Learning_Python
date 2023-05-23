x = lambda a: a + 10
print(x(5)) # 15

y = lambda c, d : c * d
print(y(5, 6)) # 30

z = lambda d, e, f: d + e - f
print(z(5, 6, 2)) # 9

def myfunc(n):
  return lambda i : i * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) # 22
print(mytripler(11)) # 33


