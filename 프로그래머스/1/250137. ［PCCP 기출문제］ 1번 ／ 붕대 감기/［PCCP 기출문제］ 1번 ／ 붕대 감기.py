def solution(bandage, health, attacks):
    originHeal = health
    attackList = [False for i in range(attacks[-1][0]+1)]
    
    for time,num in attacks:
        attackList[time] = num
    
    bandageTime = 0
    for i in range(attacks[-1][0]+1):
        if (attackList[i] != False):
            health -= attackList[i]
            bandageTime = 0
            
            if (health <= 0):
                return -1
        else :
            bandageTime+=1
            health += bandage[1]
            if (health > originHeal):
                health = originHeal
            
            if (bandageTime == bandage[0]):
                health += bandage[2]
                if (health > originHeal):
                    health = originHeal
                    
                bandageTime = 0
        
    return health