N,M = map(int,input().split())
number = []

for i in range(N):
  inp = int(input())
  number.append(inp)

number.sort()

start = 0
end = 0
sub = 0
ans = number[-1]-number[0]
isAns = False

while start < len(number) and end < len(number):
  sub = number[end]-number[start]
  if sub < M:
    end += 1
  elif sub > M:
    ans = min(ans,sub)
    start += 1
  else:
    print(M)
    isAns = True
    break

if not isAns:
  print(ans)