def solution(N, number):
#   매 횟수 계산 결과를 저장할 배열
    dp_array=[[]]
    for i in range(1,9):
#       현재 해당하는 횟수 계산값 저장할 배열
        count=[]
#       i에서 차례대로 짝을 맞춰 순회(예를 들어 5면 1과4, 2와 3.... 순서)
        for j in range(1,i):
            for k in dp_array[i-j]:
                for l in dp_array[j]:
#                     덧셈 연산 결과값 저장
                    count.append(k+l)
#                     뺄셈 연산 결과값 저장
                    if k-l>0:
                        count.append(k-l)
#                     곱셈 연산 결과값 저장
                    count.append(k*l)
#                     나눗셈 연산 결과값 저장
                    if (k != 0 and l != 0) :
                        count.append(k//l)
        count.append(int(str(N) * i))
#       만약 결과값이 해당 횟수 연산 결과에 들어있다면 해당 횟수를 리턴
        if number in count:
            return i
#       count를 중복 제거하여 해당 횟수 결과 저장
        dp_array.append(list(set(count)))
#   모두 순회했는데 없다면 -1 를 리턴
    return -1