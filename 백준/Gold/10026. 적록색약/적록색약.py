N = int(input())
maps = []
checkmaps = [[0 for _ in range(N)] for _ in range(N)]
handicheckmaps = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
  inp = list(input())
  maps.append(inp)

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def originDFS(i,j):
  stack = [[i,j,maps[i][j]]]
  while stack:
    [y,x,color] = stack.pop()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny < 0 or ny >= N or nx < 0 or nx >= N:
        continue
      if maps[ny][nx] == color and checkmaps[ny][nx] != True:
        checkmaps[ny][nx] = True
        stack.append([ny,nx,color])

def handicapDFS(i,j):
  stack = [[i,j,maps[i][j]]]
  while stack:
    [y,x,color] = stack.pop()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny < 0 or ny >= N or nx < 0 or nx >= N:
        continue
      if handicheckmaps[ny][nx] == True:
        continue
      isSame = False
      if color == 'R':
        if maps[ny][nx] == color or maps[ny][nx] == 'G':
          isSame = True
      elif color == 'G':
        if maps[ny][nx] == color or maps[ny][nx] == 'R':
          isSame = True
      else:
        if maps[ny][nx] == color:
          isSame = True

      if isSame:
        handicheckmaps[ny][nx] = True
        stack.append([ny,nx,color])

cnt = 0
while True:
  isPossible= False
  for i in range(N):
    for j in range(N):
      if checkmaps[i][j] != True:
        cnt += 1
        isPossible = True
        checkmaps[i][j] = True
        originDFS(i,j)
        break
  if not isPossible:
    break

print(cnt)

handicapCnt = 0
while True:
  isPossible= False
  for i in range(N):
    for j in range(N):
      if handicheckmaps[i][j] != True:
        handicapCnt += 1
        isPossible = True
        handicheckmaps[i][j] = True
        handicapDFS(i,j)
        break
  if not isPossible:
    break

print(handicapCnt)