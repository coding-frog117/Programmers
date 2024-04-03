import heapq

def solution(operations):
    minheap=[]
    
    for operation in operations:
        op1, op2 = operation.split(' ')
        op2= int(op2)
        if (op1 == 'I'):
            heapq.heappush(minheap,op2)
            
        elif (op1 == 'D' and op2 == 1 and len(minheap)>0):
#             heapq.nlargest 메소드로 최댓값부터 추출해냄, 최댓값인 인덱스 0을 제외하고 새로운 배열 생성
            newheap = heapq.nlargest(len(minheap),minheap)[1:]
#     최솟값 우선순위큐로 만들어줌
            heapq.heapify(newheap)
            minheap = newheap
        
        elif (op1 == 'D' and op2 == -1 and len(minheap)>0):
            heapq.heappop(minheap)
    
    maxAnswer = heapq.nlargest(1,minheap)[0] if len(minheap) > 0 else 0
    minAnswer = minheap[0] if len(minheap) > 0 else 0
    answer = [maxAnswer,minAnswer]
    
    return answer