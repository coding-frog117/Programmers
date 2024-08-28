# 1~9까지 길이 1 -> 총 길이 9*1
# 10~99까지 길이 2 -> 총 길이 90*2
# 100~999까지 길이 3 -> 총 길이 900*3
# n이 해당하는 범위를 구한 후 그 안에서 몇번째 숫자인지 판단하면 됨

N,K = map(int,input().split())

nine = 9
numLen = 1
start = 0

while K > nine*numLen:
  K -= (numLen*nine)
  start += nine
  numLen += 1
  nine *= 10

l,r = divmod(K-1,numLen)
result = start+1+l

if result > N :
  print(-1)
else:
  print(str(result)[r])