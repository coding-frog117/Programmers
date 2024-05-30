import math 

student = [[0,0] for i in range(6)]
N,K = map(int,input().split())
ans = 0

for i in range(N):
  s,grade = map(int,input().split())

  student[grade-1][s] += 1

for i in student:
  for j in i:
    if j == 0:
      continue
    if j > K:
      room = math.ceil(j / K)
      ans += room
    else:
      ans += 1
print(ans)