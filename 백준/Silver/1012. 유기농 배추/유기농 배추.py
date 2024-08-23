from collections import deque

dy = [0,0,1,-1]
dx = [1,-1,0,0]

T =int(input())

def BFS(pos):
  [y,x] = pos
  queue = deque([[y,x]])
  while queue:
    y,x = queue.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if ny < 0 or ny >= N or nx < 0 or nx >= M:
        continue

      if ground[ny][nx] == 1:
        ground[ny][nx] = 'Check'
        queue.append([ny,nx])


for i in range(T):
  M,N,K = map(int,input().split())
  ground = [[0 for i in range(M)] for i in range(N)]

  for i in range(K):
    x,y = map(int,input().split())
    ground[y][x] = 1
    
  cnt = 0

  while True:
    isPossible = False
    for row_idx,i in enumerate(ground):
      for col_idx,j in enumerate(i):
        if j == 1:
          isPossible = True
          ground[row_idx][col_idx] = 'Check'
          BFS([row_idx,col_idx])
          cnt +=1
    if not isPossible:
      break
  print(cnt)