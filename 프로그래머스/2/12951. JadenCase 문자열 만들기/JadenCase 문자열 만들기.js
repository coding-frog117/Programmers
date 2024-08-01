function solution(s) {
    answer = []
    s = s.toLowerCase()
    stringArr = s.split(' ')
    console.log(stringArr)
    stringArr.forEach((str,index)=>{
        console.log(str)
        if (str == '' || str == ' '){
            answer.push('')
        }
        else if (isNaN(str[0])) {
            upper = str[0].toUpperCase()
            if (str.length > 1){
                answer.push(upper + str.slice(1,))
            }
            else{
                answer.push(upper)
            }
        }
        else{
            if (str.length > 1){
                answer.push(str[0] + str.slice(1,))
            }else{
                answer.push(str[0])
            }
        }
    })
    return answer.join(' ')
//     최종 문자열 출력
}