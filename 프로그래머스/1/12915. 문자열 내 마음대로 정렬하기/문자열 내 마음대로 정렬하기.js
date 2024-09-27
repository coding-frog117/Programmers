function solution(strings, n) {
    newSort = []
    for (s in strings){
        newSort.push([strings[s][n],strings[s],s])
    }
    newSort.sort()
    ans = []
    
    for (i of newSort){
        ans.push(strings[i[2]]);
    }
    return ans
}