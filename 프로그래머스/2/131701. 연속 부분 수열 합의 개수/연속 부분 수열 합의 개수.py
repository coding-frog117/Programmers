ans = set()

def solution(elements):
    newArr = elements*2
    for i in range(len(elements)):
        pos = i
        for j in range(len(elements)):
            if i == len(elements)-1:
                ans.add(sum(elements))
                break
            ans.add(sum(newArr[j:j+pos+1]))
    return len(ans)