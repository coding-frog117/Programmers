import sys
S,E,Q = sys.stdin.readline().split()
ans = 0

def getMinuets(time):
  start,end = map(int,time.split(':'))
  return start*60 + end

S = getMinuets(S)
E = getMinuets(E)
Q = getMinuets(Q)

check = {}
lines = sys.stdin.readlines()

for line in lines:
  time, name = line.split()
  m = getMinuets(time)
  if m <= S :
    check[name] = False
  elif check.get(name) == False and E <= m <= Q:
    check[name] = True

for key,val in check.items():
  if val == True:
    ans += 1

print(ans)