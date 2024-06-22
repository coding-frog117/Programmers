function solution(s) {
    const answer = [0,0]
    while (s != '1'){
        answer[0] += 1
        newStr = ''
        for (let i of s){
            if (i == '1'){
                newStr += i
            }else{
                answer[1] += 1
            }
        }
        s = newStr.length.toString(2)
    }
    return answer
}