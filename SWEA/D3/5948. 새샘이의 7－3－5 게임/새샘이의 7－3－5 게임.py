T = int(input())


def DFS(length, summ, seen, numArr, sumArr):
    if length == 3:
        sumArr.append(summ)
        return

    for i in numArr:
        if i not in seen:
            DFS(length + 1, summ + i, seen + [i], numArr, sumArr)


for tc in range(T):
    numArr = list(map(int, input().split()))
    sumArr = []
    for i in numArr:
        DFS(1, i, [i], numArr, sumArr)

    print(f'#{tc+1} {sorted(list(set(sumArr)))[-5]}')