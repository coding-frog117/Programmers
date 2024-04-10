N=int(input())
arr = list(map(int,input().split()))
arr.sort()

M = int(input())
findArr = list(map(int,input().split()))

def search(start,end,target):
  
  while (start <= end):
    pivot = (end+start) // 2

    if (arr[pivot] == target):
      return 1
    elif (arr[pivot] > target):
      end = pivot-1
    elif (arr[pivot] < target):
      start = pivot+1

  return 0

for target in findArr:
  start=0
  end = N-1
  print(search(start,end,target))