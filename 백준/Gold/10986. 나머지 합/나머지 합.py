N,M = map(int,input().split())
array = list(map(int,input().split()))
sumArr = [0]*M
count = 0
answer = 0

# 나머지가 같은 값끼리 뺄셈하면 나머지가 0이 됨 -> 나머지가 같은 값끼리의 조합 찾기
for i in range(len(array)):
  count += array[i]
  sumArr[count%M] += 1

answer += sumArr[0]

for i in range(len(sumArr)):
  if (sumArr[i] > 1):
    answer += sumArr[i] * (sumArr[i]-1) // 2

print(answer)