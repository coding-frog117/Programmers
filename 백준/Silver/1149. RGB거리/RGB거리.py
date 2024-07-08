N = int(input())
color = [[0,0,0]]
for i in range(N):
  inp = list(map(int,input().split()))
  color.append(inp)

minColor = [[0,color[1][0]],[0,color[1][1]],[0,color[1][2]]]

for i in range(2,N+1):
  minColor[0].append(min(minColor[1][i-1]+color[i][0],minColor[2][i-1]+color[i][0]))
  minColor[1].append(min(minColor[0][i-1]+color[i][1],minColor[2][i-1]+color[i][1]))
  minColor[2].append(min(minColor[0][i-1]+color[i][2],minColor[1][i-1]+color[i][2]))
answer= []

for i in minColor:
  answer.append(i[-1])
print(min(answer))