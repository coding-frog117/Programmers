N = int(input())

if N == 1:
  print(0)
  print('1')
  exit()
elif N == 2:
  print(1)
  print('2 1')
  exit()
arr= [0]*(N+1)
arr[1] = [1,1]
arr[2] = [1,2]
arr[3] = [1,3]

for i in range(4,N+1):
  arr[i]=[arr[i-1][0]+1,1]

  if i%2==0:
    if arr[i][0] > arr[i//2][0]+1:
      arr[i] = [arr[i//2][0]+1,2]
  
  if i%3 == 0:
    if arr[i][0] > arr[i//3][0]+1:
      arr[i] = [arr[i//3][0]+1,3]

ans = arr[N]
curr = N
answer = [N]

while True:
  if ans[1] == 1:
    curr-=1
    ans = arr[curr]
  elif ans[1] == 2:
    curr =curr // 2
    ans = arr[curr]
  elif ans[1] == 3:
    curr= curr // 3
    ans = arr[curr]
  
  answer.append(curr)
  if ans == [1,1]:
    break
print(arr[N][0])
print(*answer)