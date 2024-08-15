# n이 s보다 크면 return -1
# 같으면 1을 n개
# 작으면 s를 n으로 나눠서 나머지를 균등 분배

def solution(n, s):
    if n > s:
        return [-1]
    elif n == s:
        return [1]*n
    else:
        num,r = divmod(s,n)
        answer = [num] * n
        
        if r == 0:
            return answer
        else:
            for i in range(r):
                answer[n-1-i] += 1
        return answer