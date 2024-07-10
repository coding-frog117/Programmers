import sys
n,k = map(int,sys.stdin.readline().split())
coin = []
arr = [0]*(k+1)
ans = 0

for i in range(n):
  inp = int(input())
  coin.append(inp)

arr[0] = 1
# coin을 돌면서 해당 동전까지 사용했을때 각 금액의 코인 사용 갯수 구하기
for c in coin:
  for i in range(c,k+1):
    arr[i] = arr[i] + arr[i-c]

print(arr[-1])