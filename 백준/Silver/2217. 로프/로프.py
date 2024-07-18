N= int(input())
lopes = []
weight = 0

for i in range(N):
  w = int(input())
  lopes.append(w)

lopes.sort()
for idx,lope in enumerate(lopes):
  if (len(lopes) - idx)*lope > weight:
    weight = (len(lopes) - idx)*lope
print(weight)