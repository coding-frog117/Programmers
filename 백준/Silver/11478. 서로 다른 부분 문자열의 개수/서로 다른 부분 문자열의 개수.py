S = input()
maps = set()

for i in range(1,len(S)+1):
  start = 0
  end = i 
  while end < len(S)+1:
    maps.add(S[start:end])
    start += 1
    end += 1
print(len(maps))