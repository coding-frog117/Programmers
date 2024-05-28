N= input()
nums= {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
global answer
answer = 0

def appendSet(nums,i):
    global answer
    for num in range(10):
        nums[str(num)] += 1
    answer += 1
    nums[i] -= 1

for i in N:
    if i == '6':
        if nums['6'] > 0 :
            nums['6'] -= 1
        elif nums['9'] > 0:
            nums['9'] -= 1
        else:
            appendSet(nums,i)
    elif i == '9':
        if nums['9'] > 0 :
            nums['9'] -= 1
        elif nums['6'] > 0:
            nums['6'] -= 1
        else:
            appendSet(nums,i)
    else:
        if nums[i] > 0:
            nums[i] -=1
        else:
            appendSet(nums,i)
print(answer)