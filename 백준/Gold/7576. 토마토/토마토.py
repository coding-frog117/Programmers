from collections import deque

M,N = map(int,input().split())
box = []
emptyCount = 0
queue = deque()
answer = 0

for i in range(N):
  tomato = list(map(int,input().split()))

  box.append(tomato)

isZero = False
isOne = False

for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      isOne = True
      queue.append([i,j])
    elif box[i][j] == 0:
      isZero = True
    elif box[i][j] == -1:
      emptyCount += 1

if isZero == False :
  print(0)
  exit()
if isOne == False:
  print(-1)
  exit()

dx = [1,-1,0,0]
dy = [0,0,1,-1]
reachCount = len(queue)

while queue:
  [y,x] = queue.popleft()
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue

    if box[ny][nx] == -1 :
        box[ny][nx] = 1
        emptyCount += 1
        continue

    if box[ny][nx] == 0 :
        reachCount+=1
        box[ny][nx] = box[y][x] + 1
        queue.append([ny,nx])

if len(queue) ==0 :
  for i in range(N):
      for j in range(M):
          if box[i][j] == 0:
              print(-1)
              exit()
          answer = max(answer,box[i][j])

print(answer-1)