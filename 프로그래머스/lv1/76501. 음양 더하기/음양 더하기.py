def solution(absolutes, signs):
    summ=0
    length=len(absolutes)
    for i in range(length):
        if signs[i]==True:
            num=absolutes[i]
        else:
            num=-1*absolutes[i]
            
        summ=summ+num
    return summ