def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    count = {}
    answer = 0
    index =0
    
    # 각 A 원소보다 큰 B원소 저장
    for i in range(len(A)):
        if A[i] < B[index] :
            answer += 1
            index += 1
            
    return answer