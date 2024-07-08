N = int(input())
cnt = [0]*(N+1)
if N == 1 :
  print(1)
  exit()
elif N == 2:
  print(2)
  exit()
cnt[1] = 1
cnt[2] = 2

for i in range(3,N+1):
  cnt[i] = cnt[i-1] + cnt[i-2]

print(cnt[N]%10007)