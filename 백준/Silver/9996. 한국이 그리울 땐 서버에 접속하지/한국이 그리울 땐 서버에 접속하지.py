N = int(input())
# '*'을 기준으로 나누기, 각 값을 앞과 뒤에서 비교하며 같은지 확인
pattern = input().split('*')
front,back = pattern

for i in range(N):
    name = input()
    isPossible = True
    if len(name) < len(front) + len(back) :
        isPossible = False
        isPossible = 'DA' if isPossible else 'NE'
        print(isPossible)
        continue

    for i in range(len(front)):
        if front[i] != name[i]:
            isPossible = False
            break
    currIdx = -1
    for i in range(len(back)-1,-1,-1):
        if back[i] != name[currIdx]:
            isPossible = False
            break
        currIdx -= 1

    isPossible = 'DA' if isPossible else 'NE'
    print(isPossible)