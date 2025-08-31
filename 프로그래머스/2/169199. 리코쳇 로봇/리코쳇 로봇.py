from collections import deque

def solution(board):
    ans = 99999
    dy = [0, -1, 0, 1]  # 동, 북, 서, 남
    dx = [1, 0, -1, 0]

    def BFS(i, j, d):
        answer = 99999
        queue = deque()
        # seen을 dict으로: (y,x,d) -> 최소 이동 횟수
        seen = {}
        queue.append([i, j, 1, d])
        seen[(i, j, d)] = 1

        while queue:
            y, x, count, direction = queue.popleft()
            if count >= answer:
                continue

            ny = y + dy[direction]
            nx = x + dx[direction]

            # 현재 방향으로 더 못 가면 멈춤
            if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]) or board[ny][nx] == "D":
                if board[y][x] == "G":
                    answer = min(answer, count)
                    continue

                # 방향 전환
                for i in range(4):
                    if i == direction:
                        continue
                    cur_y = y + dy[i]
                    cur_x = x + dx[i]

                    if cur_y < 0 or cur_x < 0 or cur_y >= len(board) or cur_x >= len(board[0]) or board[cur_y][cur_x] == "D":
                        continue

                    # 더 적은 횟수로 방문했는지 확인
                    if (cur_y, cur_x, i) not in seen or seen[(cur_y, cur_x, i)] > count + 1:
                        seen[(cur_y, cur_x, i)] = count + 1
                        queue.append([cur_y, cur_x, count + 1, i])
            else:
                # 같은 방향으로 계속 이동
                if (ny, nx, direction) not in seen or seen[(ny, nx, direction)] > count:
                    seen[(ny, nx, direction)] = count
                    queue.append([ny, nx, count, direction])

        return answer

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board[0]) or board[ny][nx] == "D":
                        continue
                    ans = min(BFS(i, j, k), ans)
                break

    if ans == 99999:
        return -1
    return ans