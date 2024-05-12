T = int(input())
for tc in range(T):
    num = int(input())
    score = list(map(int,input().split()))
    countArr = {}

    for i in score:
        if countArr.get(i) :
            countArr[i][0] += 1
        else:
            countArr[i] = [1,i]

    result = list(countArr.values())
    print(f'#{num} {sorted(result)[-1][1]}')