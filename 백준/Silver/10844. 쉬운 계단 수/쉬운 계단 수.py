N = int(input())
arr = [[0]*10 for i in range(N+1)]
arr[1][0] = 0

for i in range(1,N+1):
  for j in range(10):
    if i == 1 and j!=0:
      arr[i][j] = 1
      continue
    if j ==0 :
      arr[i][j] = arr[i-1][1]
      continue
    if j == 9:
      arr[i][j] = arr[i-1][8]
      continue
    arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]   
print(sum(arr[-1]) % 1000000000)