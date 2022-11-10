def solution(nums):
    array=[]
    for i in nums:
        if i in array:
            pass
        else:
            array.append(i)
            
    if len(array)<=len(nums)//2:
        return len(array)
    else:
        return len(nums)//2