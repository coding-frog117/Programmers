function solution(s){
    const stack = [];
    for (let i of s){
        if (i == '('){
            stack.push(i)
        }else{
            if (stack.length >= 1 && stack[stack.length-1] == '('){
                stack.pop()
            }else{
                return false
            }
        }
    }
    if (stack.length == 0){
        return true
    }else{
        return false
    }
}