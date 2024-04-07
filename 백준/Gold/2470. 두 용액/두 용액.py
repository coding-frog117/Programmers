N = int(input())
arr = list(map(int,input().split()))
arr.sort()

if (arr[0] > 0):
  print(arr[0],arr[1])

elif (arr[-1] < 0):
  print(arr[-2],arr[-1])

else :
  idx1 = 0
  idx2 = len(arr) -1
  minVal1 = arr[idx1]
  minVal2 = arr[idx2]
  minDel = abs(arr[idx2] + arr[idx1])

  while (idx1 < idx2):
    if (arr[idx1] + arr[idx2] == 0):
      print(arr[idx1], arr[idx2])
      break

    elif (arr[idx1] + arr[idx2] < 0):
      if (abs(arr[idx2] + arr[idx1]) < minDel):
        minDel = abs(arr[idx2] + arr[idx1])
        minVal1 =  arr[idx1]
        minVal2 = arr[idx2]
      idx1 += 1

    elif (arr[idx1] + arr[idx2] > 0):
      if (abs(arr[idx2] + arr[idx1]) < minDel):
        minDel = abs(arr[idx2] + arr[idx1])
        minVal1 =  arr[idx1]
        minVal2 = arr[idx2]
      idx2 -= 1

  print(minVal1, minVal2)