# 1이 붙어있는 갯수, 0이 붙어있는 갯수 확인 후 더 작은 쪽 리턴
S = input()
oneCount = 0
zeroCount = 0
cur = -1

for i in S:
  if i != cur:
    cur = i
    if cur == '1':
      oneCount += 1
    else:
      zeroCount +=1
 
print(min(oneCount,zeroCount))