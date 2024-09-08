# DFS 최소비용
import copy
import sys
from collections import deque

dy= [0,0,1,-1]
dx= [1,-1,0,0]
directions = ['R','L','D','U']
global ans

def solution(board):
    N = len(board)
    costs = [[sys.maxsize for i in range(N)] for i in range(N)]
    def DFS(y,x,direction,ans):
        board[y][x] = 0
        queue = deque([[y,x,0,direction]])
        
        while queue:
            [y,x,cost,direction] = queue.popleft()
            if y == N-1 and x == N-1:
                continue
                
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board):
                    continue
                if board[ny][nx] == 1:
                    continue
                    
                if direction == directions[i]:
                    nc = cost+100
                else:
                    nc = cost+600
                
                if nc <= costs[ny][nx] :
                    costs[ny][nx] = nc
                    queue.append([ny,nx,nc,directions[i]])
    
    DFS(0,0,'R',0)
    DFS(0,0,'D',0)
    return costs[-1][-1]