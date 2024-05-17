for tc in range(10):
    num, numList = input().split()
    numList = list(''.join(numList))

    start,end = 0,1
    while True :
        if end >= len(numList):
            break
        if numList[start] == numList[end] :
            if start == 0:
                numList = numList[end+1:]
                start = 0
                end = 1
            elif end == len(numList) -1 :
                numList = numList[:start]
                end = start -1
                start = end-1
            else :
                start -= 1
                end += 1
        else :
            if end - start == 1:
                start += 1
                end += 1
            else :
                numList = numList[:start+1] + numList[end:]
                start += 1
                end= start+1
    answer = ''.join(numList)
    print(f'#{tc+1} {answer}')