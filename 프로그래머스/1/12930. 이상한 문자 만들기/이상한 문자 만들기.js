function solution(s) {
    s = s.split(' ')
    let answer = [];
    for (const word of s){
        let cur_word = '';
        
        for (const i in word){
            if (i % 2 == 0){
                cur_word += word[i].toUpperCase()
            }else{
                cur_word += word[i].toLowerCase()
            }
        }
        answer.push(cur_word);
    }
    return answer.join(' ')
}