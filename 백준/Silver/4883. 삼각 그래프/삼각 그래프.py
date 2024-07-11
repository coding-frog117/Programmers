import sys

tc = 1
while True:
  N= int(sys.stdin.readline())
  if N == 0:
    break

  graph = []
  dp = [[sys.maxsize]*3 for i in range(2)]
  for i in range(N):
    col = list(map(int,sys.stdin.readline().split()))
    graph.append(col)

  dp[0][0] = graph[0][0]
  dp[0][1] = graph[0][1]
  dp[0][2] = graph[0][1] + graph[0][2]

  dp[1][0] = graph[0][1] + graph[1][0]
  dp[1][1] = min(min(dp[0][1],dp[0][2]),dp[1][0]) + graph[1][1]
  dp[1][2] = min(min(dp[0][1],dp[0][2]),dp[1][1]) + graph[1][2]

  dp[0][0] = dp[1][0]
  dp[0][1] = dp[1][1]
  dp[0][2] = dp[1][2]

  for i in range(2,N):
    dp[1][0] = min(dp[0][0],dp[0][1]) + graph[i][0]
    dp[1][1] = min(min(dp[0][0],dp[0][1],dp[0][2]),dp[1][0]) + graph[i][1]
    dp[1][2] = min(min(dp[0][1],dp[0][2]),dp[1][1]) + graph[i][2]

    dp[0][0] = dp[1][0]
    dp[0][1] = dp[1][1]
    dp[0][2] = dp[1][2]

  print(f'{tc}. {dp[1][1]}')
  tc+= 1