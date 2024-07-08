N,M= map(int,input().split())
num = list(map(int,input().split()))
arr = [0]*(N+1)

for i in range(1,N+1):
  arr[i] = arr[i-1] + num[i-1]

for i in range(M):
  s,e = map(int,input().split())
  print(arr[e]-arr[s-1])