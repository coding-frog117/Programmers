N= int(input())
global maxCount
maxCount = 0

def DFS(length,sum, arr,count):
    if length >= N:
        global maxCount
        maxCount =max(sum,maxCount)
        return maxCount

    count -= 1
    # 작업중인 경우
    if count > 0 :
        DFS(length+1, sum, arr, count)

    else:
        if arr[length][0] == 1:
            DFS(length + 1, sum+ arr[length][1],arr, 0)
        else :
            # 작업 끝마치는 일수가 퇴사일보다 큰 경우
            if arr[length][0] + length > N:
                DFS(length + 1, sum, arr, 0)

            else:
                # 값을 추가한 경우
                DFS(length+1, sum+arr[length][1], arr, arr[length][0])
                # 추가하지 않은 경우
                DFS(length+1,sum, arr, 0)
arr = []

for i in range(N):
    T,P = map(int,input().split())
    arr.append([T,P])

DFS(1,0,arr,0)
if arr[0][0] <= N:
    DFS(1,arr[0][1],arr,arr[0][0])
print(maxCount)