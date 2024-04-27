import heapq
import sys

heap =[]
N = int(sys.stdin.readline())
for i in range(N):
  num = int(sys.stdin.readline())
  if num > 0:
    heapq.heappush(heap,num)
  else :
    if len(heap) == 0 :
      print(0)
    else:
      print(heapq.heappop(heap))
