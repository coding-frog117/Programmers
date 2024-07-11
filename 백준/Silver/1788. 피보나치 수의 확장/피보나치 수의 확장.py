n= int(input())

arr = [0]*(abs(n)+1)
if n == 0:
  print(0)
  print(0)
  exit()

arr[1] = 1
for i in range(2,abs(n)+1):
  arr[i] = (arr[i-1]+arr[i-2])% 1000000000

if n > 0:
  print(1)
  print(arr[-1] % 1000000000)

else:
  if n % 2 == 0:
    print(-1)
  else:
    print(1)
  print(arr[-1] % 1000000000)