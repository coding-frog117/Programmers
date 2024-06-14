from sys import stdin

M = int(stdin.readline())
S = 0
def isHave(S,idx):
    num = (1 << idx)
    if num&S == 0:
        return False
    else:
        return True

for i in range(M):
    inp=list(stdin.readline().split())
    if inp[0] == 'all':
        S= (1<<20)-1
    elif inp[0] == 'empty':
        S = 0
    else:
        oper,x=inp
        check = isHave(S, 20-int(x))
        if oper =='add':
            if not check :
                num = (1 << 20-int(x))
                S = S | num
        elif oper == 'remove':
            if check:
                num = ~(1 << 20 - int(x))
                S = S & num
        elif oper == 'check':
            if check:
                print(1)
            else:
                print(0)
        elif oper =='toggle':
            if check:
                num = ~(1 << 20 - int(x))
                S = S & num
            else:
                num = (1 << 20 - int(x))
                S = S | num