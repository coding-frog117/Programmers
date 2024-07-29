import heapq

n,m = map(int,input().split())
card = list(map(int,input().split()))
heapq.heapify(card)

for i in range(m):
  num1= heapq.heappop(card)
  num2 = heapq.heappop(card)
  heapq.heappush(card,num1+num2)
  heapq.heappush(card,num1+num2)
print(sum(card))