def solution(answers):
    cnt1,cnt2,cnt3=0,0,0
    
    person1=[1,2,3,4,5]
    person2=[2,1,2,3,2,4,2,5]
    person3=[3,3,1,1,2,2,4,4,5,5]
    answer = []
    b=[]
    length=len(answers)
    
    for i in range(length):
        if answers[i]==person1[i%5]:
            cnt1=cnt1+1
        if answers[i]==person2[i%8]:
            cnt2=cnt2+1
        if answers[i]==person3[i%10]:
            cnt3=cnt3+1
                
    b.append(cnt1)
    b.append(cnt2)
    b.append(cnt3)

    maxnum=(max(b))
    if maxnum==cnt1:
        answer.append(1)
    if maxnum==cnt2:
        answer.append(2)
    if maxnum==cnt3:
        answer.append(3)
    answer.sort()
    return answer