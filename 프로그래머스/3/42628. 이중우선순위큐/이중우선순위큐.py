import heapq

def solution(operations):
    minheap=[]
    maxheap=[]
    
    for operation in operations:
        op1, op2 = operation.split(' ')
        op2= int(op2)
        if (op1 == 'I'):
            heapq.heappush(minheap,op2)
            heapq.heappush(maxheap,int(op2)*-1)
            
        elif (op1 == 'D' and op2 == 1 and len(minheap)>0):
            maxData = heapq.heappop(maxheap)
            minheap.remove(-maxData)
        
        elif (op1 == 'D' and op2 == -1 and len(minheap)>0):
            minData = heapq.heappop(minheap)
            maxheap.remove(-minData)
    
    maxAnswer = -maxheap[0] if len(maxheap) > 0 else 0
    minAnswer = minheap[0] if len(maxheap) > 0 else 0
    answer = [maxAnswer,minAnswer]
    
    return answer