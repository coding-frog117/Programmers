def solution(n, computers):
    stack = [0]
    seen = [0]
    answer = n  # answer 변수 초기화

    def dfs():
        nonlocal answer  # answer 변수를 갱신하기 위해 nonlocal 선언
        while len(stack) > 0 :
            presIndex = stack.pop()
            for i in range(n):
                if (computers[presIndex][i] == 1) and (presIndex != i) and (i not in seen):
                    answer -= 1
                    stack.append(i)
                    seen.append(i)
                    if answer == 1:
                        return 1

        for i in range(n):
            if i not in seen:
                stack.append(i)
                seen.append(i)
                dfs()
                
        return answer  # answer 값을 반환하도록 수정

    return dfs() 