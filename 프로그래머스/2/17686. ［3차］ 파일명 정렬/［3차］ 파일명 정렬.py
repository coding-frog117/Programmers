# 각 file마다 [head,number,idx] 부분을 나눠서 만든후 정렬

def solution(files):
    answer = []
    strings = ['','.','-']
    for file in files:
        head = ''
        number = ''
        isAfterString = False
        
        for char in file:
            # 처음에 나오는 알파벳 부분 -> head
            if (not char.isdigit()) and number == '':
                head += char.lower()
            # 두번째 나오는 숫자 부분 -> number
            elif char.isdigit() and len(number) < 5 and isAfterString == False:
                number += char
            # number 이후에 영문자나 기호 오는 경우 예외처리
            elif (char.isalpha() or char in strings) and number != '':
                isAfterString = True
            
        number = int(number)
        answer.append([head,number,files.index(file)])
    answer.sort()
    correctArr = []
    
    for file in answer:
        correctArr.append(files[file[2]])
    
    return correctArr