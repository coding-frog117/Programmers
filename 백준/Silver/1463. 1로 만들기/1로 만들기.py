n = int(input())
# 각 수량 체크
arr = [0] * 1000001

for i in range(2,n+1):
    # 일단 -1의 경우를 갱신
    arr[i] = arr[i-1] + 1
    # %3이 0이면 그 값과 현재값중 작은 값 채택
    if i % 2 == 0:
        arr[i] = min(arr[i//2]+1,arr[i])
    # %2이 0이면 그 값과 현재값중 작은 값 채택
    if i % 3 == 0:
        arr[i] = min(arr[i//3]+1,arr[i])
print(arr[n])