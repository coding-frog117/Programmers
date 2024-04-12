import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
count = {}
answer = []
  
M = int(input())
findArr = list(map(int,input().split()))

left = 0
right = N-1

for i in arr:
  if (count.get(i)):
    count[i] += 1
  else :
    count[i] = 1

for target in findArr:
  if (count.get(target)):
    answer.append(str(count[target]))
  else:
    answer.append('0')

print(' '.join(answer))