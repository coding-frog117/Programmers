K,L = map(int,input().split())
wait = {}
cur = 1

for i in range(L):
  student = input()
  wait[student] = cur
  cur += 1

newArr = sorted(list(wait.items()),key = lambda x : x[1])[:K]
for i in newArr:
  print(i[0])