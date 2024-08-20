from itertools import permutations

hashset = set()

def isPrimitiveNum(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    for i in range(1,len(numbers)+1): 
        curr_permute = list(permutations(numbers,i))
        for curr in curr_permute:
            nums = ''
            for i in curr:
                nums+=i
            hashset.add(int(nums))
    for number in hashset:
        if isPrimitiveNum(number):
            answer += 1
    return answer