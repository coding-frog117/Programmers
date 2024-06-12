from collections import deque

N = int(input())
maps = []
queue = []
queue.append([[0,1],0])
count = 0

def calculate(arr_y,arr_x,end_ny,end_nx,i):
  end_y = end_ny + arr_y[i][1]
  end_x = end_nx + arr_x[i][1]

  return [end_y,end_x]

for i in range(N):
  inp = list(map(int,input().split()))
  maps.append(inp)

if maps[N-1][N-1] == 1:
    print(0)
    exit()

# 가로일 때 이동(start,end)
colMove_y =[[0,0],[0,1]]
colMove_x =[[1,1],[1,1]]

rowMove_y= [[1,1],[1,1]]
rowMove_x= [[0,0],[0,1]]

interMove_y=[[1,0],[1,1],[1,1]]
interMove_x=[[1,1],[1,0],[1,1]]

while queue:
  end,dir = queue.pop()
  if end == [N-1,N-1]:
    count += 1
    continue

  end_ny = end[0]
  end_nx = end[1]

  if dir == 0 :
    for i in range(2):
      result = calculate(colMove_y,colMove_x,end_ny,end_nx,i)
      end_y, end_x = result
      if end_y >= N or end_x >= N:
        continue
      # 대각선 영역 빈칸인지 확인
      if i == 1:
        isPossible = True
        for j in range(3):
          ny = end_ny+interMove_y[j][1]
          nx = end_nx+interMove_x[j][1]

          if maps[ny][nx] == 1:
            isPossible = False
            break

        if isPossible:
          queue.append([[end_y,end_x],2])
      # 가로 영역 빈칸인지 확인
      else:
          if maps[end_y][end_x] == 0:
            queue.append([[end_y, end_x], i])

  elif dir == 1:
    for i in range(2):
      result = calculate(rowMove_y,rowMove_x,end_ny,end_nx,i)
      end_y, end_x = result
      if end_y >= N or end_x >= N:
        continue
      # 대각선 영역 확인
      if i == 1:
        isPossible = True
        for j in range(3):
          ny = end_ny+interMove_y[j][1]
          nx = end_nx+interMove_x[j][1]
          if maps[ny][nx] == 1:
            isPossible = False
            break
        if isPossible:
          queue.append([[end_y,end_x],2])
      # 세로 영역 빈칸인지 확인
      else:
          if maps[end_y][end_x] == 0:
            queue.append([[end_y, end_x], 1])
  elif dir == 2:
    for i in range(3):
      result = calculate(interMove_y,interMove_x,end_ny,end_nx,i)
      end_y, end_x = result
      if end_y >= N or end_x >= N:
        continue

      # 대각선 영역 확인
      isPossible = True
      if i == 2:
        for j in range(3):
          ny = end_ny+interMove_y[j][1]
          nx = end_nx+interMove_x[j][1]
          if maps[ny][nx] == 1:
            isPossible = False
            break
        if isPossible :
          queue.append([[end_y, end_x], 2])
      # 가로,세로 영역 빈칸인지 확인
      else:
        if maps[end_y][end_x] == 0:
          queue.append([[end_y, end_x], i])

print(count)