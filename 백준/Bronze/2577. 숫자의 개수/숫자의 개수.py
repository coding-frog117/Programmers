number = []
for i in range(3):
  number.append(int(input()))

mul = 1
for i in number:
  mul *= i

mul = str(mul)
for i in range(10):
  print(mul.count(str(i)))