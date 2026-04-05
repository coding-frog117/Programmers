def solution(s):
    numbers = s.split(" ")
    answer_arr = list(map(int,numbers))
    answer = ""
    answer += str(min(answer_arr))
    answer += " "
    answer += str(max(answer_arr))
    print(answer)
    return answer