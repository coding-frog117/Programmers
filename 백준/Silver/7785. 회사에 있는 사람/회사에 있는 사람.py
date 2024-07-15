n= int(input())
maps = {}
for i in range(n):
  name,code = input().split()
  if code == 'enter':
    maps[name] = True 
  else:
    maps[name] = False

answer = []
for key,val in maps.items():
  if val == True:
    answer.append(key)
answer.sort(reverse=True)

for i in answer:
  print(i)