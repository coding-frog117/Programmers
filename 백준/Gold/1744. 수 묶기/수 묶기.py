# 음수가 한개면 0과 묶거나 없으면 안묶기, 두개 이상이면 큰 순서대로 묶기
# 양수는 큰 순서대로 묶기

N = int(input())
numbers = []
sum = 0

for i in range(N):
  inp = int(input())
  numbers.append(inp)

numbers.sort()
curr_minusNum = 0
is_zero = False

for num in numbers:
  if num < 0:
    if curr_minusNum == 0:
      curr_minusNum = num
    else :
      sum += (curr_minusNum*num)
      curr_minusNum = 0
  elif num == 0:
    is_zero = True
  else:
    break

curr_plusNum=0

for num in reversed(numbers):
  if num == 1:
    sum += num
  elif num > 0:
    if curr_plusNum == 0:
      curr_plusNum = num
    else:
      sum += (curr_plusNum*num)
      curr_plusNum = 0
  else:
    break
    
if curr_minusNum != 0:
  if not is_zero:
    sum += curr_minusNum

if curr_plusNum != 0:
  sum += curr_plusNum

print(sum)