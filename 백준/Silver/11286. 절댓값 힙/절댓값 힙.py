import heapq
import sys

N = int(sys.stdin.readline())
plusHeap = []
minusHeap =[]

for i in range(N):
  num = int(sys.stdin.readline())

  if (num < 0):
    heapq.heappush(minusHeap,-num)
  elif num > 0:
    heapq.heappush(plusHeap,num)
  else:
    if len(plusHeap) == 0:
      if len(minusHeap) == 0:
        print(0)
      else:
        print(heapq.heappop(minusHeap) * -1)
    elif len(minusHeap) == 0:
      print(heapq.heappop(plusHeap))
    else:
      if minusHeap[0] == plusHeap[0] or minusHeap[0] < plusHeap[0]:
        print(heapq.heappop(minusHeap) * -1)
      elif minusHeap[0] > plusHeap[0]:
        print(heapq.heappop(plusHeap))