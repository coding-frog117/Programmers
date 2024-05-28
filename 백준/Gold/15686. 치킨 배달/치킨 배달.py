from copy import deepcopy
import itertools
import sys

N,M =map(int,input().split())
maps = []
chickens =[]
houses = []
minLen = sys.maxsize

# 해결 전략 : M개를 뽑는 모든 경우의 수를 구해서 거리가 최소로 하기
#

for i in range(N):
    inp = list(map(int,input().split()))
    maps.append(inp)

    for j in range(N):
        if inp[j] == 2:
            chickens.append([i,j])
        elif inp[j] == 1:
            houses.append([i,j])

def checkLength(y,x,chickens):
    length = []
    for i in range(len(chickens)):
        chicken_y = chickens[i][0]
        chicken_x = chickens[i][1]
        length.append(abs(chicken_y-y)+abs(chicken_x-x))

    minLen = min(length)
    for i in range(len(length)):
        if length[i] == minLen:
            return minLen

# M개를 뽑는 모든 경우
newArr = list(itertools.combinations(chickens,M))

for combi in newArr:
    length = 0
    for house in houses:
        y,x = house
        length += checkLength(y,x,combi)
        if length > minLen:
            break
    minLen = min(length,minLen)

print(minLen)