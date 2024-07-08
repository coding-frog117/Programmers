n= int(input())
triangle = []
ans = [[0]*i for i in range(1,n+1)]
answer = []

for i in range(n):
  triangle.append(list(map(int,input().split())))

ans[0][0] = triangle[0][0]

for i in range(1,n):
  for j in range(i+1):
    if j == 0:
      ans[i][j] = ans[i-1][j] + triangle[i][j]
    elif j == i:
      ans[i][j] = ans[i-1][j-1] + triangle[i][j]
    else:
      ans[i][j] = max(ans[i-1][j-1],ans[i-1][j]) + triangle[i][j]
    
print(max(ans[-1]))