N = int(input())
line = list(map(int,input().split()))
sum = 0
ans = 0

line.sort()
for i in line:
  sum += i
  ans += (sum)

print(ans)