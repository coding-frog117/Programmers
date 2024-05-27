# 문자열 돌면서 target과 같고, 기존 endidx보다 크다면(중복되지 않는다면) +1

inp = input()
target = input()
answer = []

start = 0
end = len(target)-1

def isDuplicate(answer,start):
  if not answer :
    return False
  if answer[-1][1] < start:
    return False
  return True

while end <len(inp):
  if inp[start:end+1] == target:
    if not isDuplicate(answer,start):
      answer.append([start,end])
  start += 1
  end += 1
print(len(answer))