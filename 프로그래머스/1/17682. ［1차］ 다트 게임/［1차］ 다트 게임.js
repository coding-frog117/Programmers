// 세개의 결과로 분리 -> 숫자가 나오면 분리
// 10을 'C'로 바꾼다음 숫자기준,C기준 분리 후 C를 다시 10으로 변경

const score = {'S':1,'D':2,'T':3}

function solution(dartResult) {
    const result = dartResult.replaceAll('10','C');
    let cur_num = -1;
    let cur_score = '';
    let cur_idx = -1;
    
    const ans = [0,0,0];
    
    for (i of result){
        if (!isNaN(i) || i==='C'){
            cur_num = i
            if (cur_num === 'C'){
                cur_num = 10;
            }
        }else if (i in score){
            cur_score = score[i]
            cur_idx += 1
            ans[cur_idx] = cur_num ** cur_score
            
        }else {
            if (i == '*'){
                ans[cur_idx] = ans[cur_idx] * 2
                if (cur_idx > 0){
                    ans[cur_idx-1] = ans[cur_idx-1] * 2
                }
            }
            else{
                ans[cur_idx] = ans[cur_idx] * -1
            }
        }
    }
    const sum = ans.reduce((acc,curr)=>acc+curr,0)
    return sum
}