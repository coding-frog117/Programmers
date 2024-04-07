n = int(input())
arr = list(map(int,input().split()))
arr.sort()
target = int(input())
count =0
idx1 = 0
idx2 = len(arr)-1

while (idx1 < idx2):
  if arr[idx1] + arr[idx2] == target :
    count += 1
    idx1 += 1
    idx2 -= 1

  elif arr[idx1] + arr[idx2] < target :
    idx1 += 1
  
  elif arr[idx1] + arr[idx2] > target :
    idx2 -= 1

print(count)