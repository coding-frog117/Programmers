N,K = map(int,input().split())
coins = []
curr_k = K
ans = 0

for i in range(N):
  inp = int(input())
  coins.append(inp)

while curr_k > 0:
  for i in range(len(coins)-1,-1,-1):
    if coins[i] <= curr_k:
      ans += (curr_k//coins[i])
      curr_k -= (curr_k//coins[i] * coins[i])
      break

print(ans)