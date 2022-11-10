def solution(s):
    array=[]
    s=s[2:-2]
    new=s.split('},{')
    new.sort(key=len)
    
    for i in new:
        ii=i.split(',')
        for j in ii:
            if int(j) not in array:
                array.append(int(j))


    
    return array