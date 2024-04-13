N,M = map(int,input().split())
arr= []

for i in range(1,N+1):
  arr.append(str(i))

def BT(length,string):
    if (length == M):
      print(' '.join(string))
      return

    for i in arr:
      if (i not in string):
        c = string + i
        BT(len(c),c)

BT(0,'')