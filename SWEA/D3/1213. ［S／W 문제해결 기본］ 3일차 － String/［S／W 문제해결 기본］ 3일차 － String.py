for i in range(10):
  tc = int(input())
  target = input()
  string = input()
  answer = 0

  for i in range(len(string)-len(target)+1):
    if string[i] != target[0]:
      continue
    
    if string[i:i+len(target)] == target:
      answer += 1

  print(f'#{tc} {answer}')