# 작은거 - 큰거

# 3-10+50-35
# 3-60-35
# +가 나오면 더한다. -가 나오면 다음 숫자부터 괄호 연다

S = input()
total = 0
sub_sum = 0
cur_num = ''
isFirst = True
isMinus = False

test = ''
num = ''
isOpen = False
for i in S:
  if i == '-':
    test += str(int(num))
    num = ''

    if not isOpen:
      test += '-('
      isOpen = True
    else:
      test += ')-('
  
  elif i == '+':
    test += str(int(num))
    test += i
    num = ''
  else:
    num += i

if num != '':
  test += str(int(num))
if isOpen :
  test += ')'
print(eval(test))
# for i in S:
#   if i.isdigit() :
#     cur_num += i
#   elif i == '+':
#     isFirst = False
#     sub_sum += int(cur_num)
#     cur_num = ''
#   else:
#     isMinus = True
#     if isFirst:
#       total += int(cur_num)
#     else:
#       total -= (sub_sum+int(cur_num))
#     sub_sum = 0
#     cur_num = ''

# if isMinus :
#   sub_sum += int(cur_num)
#   total -= sub_sum
# else:
#   sub_sum += int(cur_num)
#   total += sub_sum

# print(total)