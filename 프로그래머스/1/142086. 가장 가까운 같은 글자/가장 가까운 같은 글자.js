function solution(s) {
    const pos = {};
    const result = [];
    for (const i in s){
        if (pos[s[i]] == undefined){
            result.push(-1)
        }else{
            result.push(i-pos[s[i]])
        }
        pos[s[i]] = i
    }
    return result
}