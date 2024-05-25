N = int(input())
global ans
answer = []

def move(n,fromIdx,toIdx,supportIdx):
    if n == 1:
        print(fromIdx,toIdx)
        return

    move(n-1,fromIdx,supportIdx,toIdx)
    print(fromIdx,toIdx)
    move(n-1,supportIdx,toIdx,fromIdx)

if N <= 20:
    print((2**N) -1)
    move(N, 1, 3, 2)

else:
    print((2**N) -1)