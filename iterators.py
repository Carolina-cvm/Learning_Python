class numeros:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

classNum = numeros()
myiter = iter(classNum)

print(next(myiter)) # 1
print(next(myiter)) # 2
print(next(myiter)) # 3
print(next(myiter)) # 4
print(next(myiter)) # 5
print(next(myiter)) # 6
print(next(myiter)) # 7
print(next(myiter)) # 8
print(next(myiter)) # 9
print(next(myiter)) # 10
