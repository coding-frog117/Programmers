from itertools import permutations

def solution(expression):
    maxNum = 0
    operations = []
    splited = []
    currNum = ''
    for i in expression:
        if i.isdigit():
            currNum += i
        elif i in ['+','-','*'] :
            splited.append(currNum)
            splited.append(i)
            currNum = ''
            if i not in operations:
                operations.append(i)
    splited.append(currNum)
    per = list(permutations(operations,len(operations)))

    for opers in per:
        newSplited = splited[:]
        # 각 연산자 순서대로 연산 시도
        for oper in opers:
            i =0
            while oper in newSplited:
                if newSplited[i] == oper :
                    num1 = newSplited[i-1]
                    num2 = newSplited[i+1]
                    
                    if oper == '-':
                        result = int(num1)-int(num2)
                    elif oper == '+':
                        result = int(num1)+int(num2)
                    elif oper == '*':
                        result = int(num1)*int(num2)
                    newSplited = newSplited[:i-1] + newSplited[i+2:]
                    newSplited.insert(i-1,result)
                else:
                    i+= 1
                    if i >= len(newSplited):
                        i = 0
        
        maxNum = max(abs(newSplited[0]),maxNum)
    
    return maxNum