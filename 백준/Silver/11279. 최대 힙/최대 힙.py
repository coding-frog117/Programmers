import heapq
import sys

arr = []
N = int(sys.stdin.readline())
for i in range(N):
  num = int(sys.stdin.readline())
  if num > 0 :
    heapq.heappush(arr,-num)
  else:
    if len(arr) == 0:
      print(0)
    else:
      print(-1 * heapq.heappop(arr))