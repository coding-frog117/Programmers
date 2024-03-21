def solution(phone_book):
    hashmap={}
    for i in phone_book:
        hashmap[i]=1
    
    for i in phone_book:
        tmp=''
        for number in i:
            tmp+=number
            if tmp in hashmap and tmp!=i:
                return False
    return True