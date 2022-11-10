def solution(N, stages):
    hashmap={}
    arr=[]
    array=[]
    for i in range(1,N+1):  
        total=0
        fail=0
        for stage in stages:
            if i<=stage:
                total+=1
                if i==stage:
                    fail+=1
        if total==0 or fail==0:
            hashmap[i]=0
        else:
            hashmap[i]=fail/total
    
    '''for idx,value in hashmap.items():
        arr.append([idx,value])
    arr.sort(key=lambda x:x[1],reverse=True)
    for i in arr:
        array.append(i[0])
    return array'''
    sortdic=sorted(hashmap.items(),key=lambda x: x[1],reverse=True)
    
    for i in sortdic:
        arr.append(i[0])
                 
    return arr