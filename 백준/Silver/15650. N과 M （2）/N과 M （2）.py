import copy

N,M = map(int,input().split())
arr= []
seen = []

for i in range(1,N+1):
  arr.append(str(i))

def BT(length,string):
    if (length == M):
        string.sort();
        if (string not in seen):
          print(' '.join(string));
          seen.append(string)
        return
        
    for i in arr:
      if (i not in string):
        newArr = copy.copy(string)
        BT(len(string)+1,newArr+[i]);
BT(0,[])