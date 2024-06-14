from collections import deque

N = int(input())
maps = [[0 for _ in range(N)] for _ in range(N)]
K = int(input())
for i in range(K):
    y,x = map(int,input().split())
    maps[y-1][x-1] = 1

L = int(input())
times = deque()

for i in range(L):
    time,dir = input().split()
    times.append([int(time),dir])

curr = [0,0]
curr_dir = 0
count = 0
body = 1
total_body = [[0,0]]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

curr_time = times.popleft()
while True:
    ny = curr[0] + dy[curr_dir]
    nx = curr[1] + dx[curr_dir]
    curr = [ny, nx]
    count += 1

    if ny < 0 or ny >= N or nx < 0 or nx >= N:
        print(count)
        break

    if [ny,nx] in total_body:
        print(count)
        break

    if curr_time and count == curr_time[0]:
        time,dir = curr_time
        if dir == 'D':
            curr_dir += 1
            if curr_dir > 3:
                curr_dir = 0
        else:
            curr_dir -= 1
            if curr_dir < 0:
                curr_dir = 3
        if times :
            curr_time = times.popleft()
        else:
            curr_time = False
    total_body.append([ny, nx])
    if maps[ny][nx] == 1:
        body += 1
        maps[ny][nx] = 0
        if body >= N:
            print(count)
            break
    else:
        total_body = total_body[1:]