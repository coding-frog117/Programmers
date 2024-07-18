N= int(input())
plans = []
count = 0

for i in range(N):
  inp = list(map(int,input().split()))
  plans.append(inp)

plans.sort()
start = -1
end = -1

for plan in plans:
  if plan[0] >= end :
    count += 1
    start = plan[0]
    end = plan[1]
  elif plan[1] < end:
    start = plan[0]
    end = plan[1]
print(count)