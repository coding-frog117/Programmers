// gems돌면서 보석 종류 세기
// 종류 갯수를 초기 window로 잡아서 시작
// 모든 종류가 있다면 start+1
// 모든 종류가 없다면 end+1
// end가 gems를 넘어간다면 break

const allGems = new Map();
const answer = [];

function solution(gems) {
    for (const gem of gems){
        if (allGems.get(gem) == undefined){
            allGems.set(gem,1)
        }else{
            allGems.set(gem,allGems.get(gem)+1)
        }
    }
    const size= allGems.size
    
    let start = 0;
    let end = size-1
    const window = new Map();
    
    for (let i=0;i<end+1;i++){
        if (window.get(gems[i]) == undefined){
            window.set(gems[i],1)
        }else{
            window.set(gems[i],window.get(gems[i])+1)
        }
    }
    while (end < gems.length){
        if (window.size == size){
            answer.push([end-start,[start+1,end+1]])
            if (window.get(gems[start]) === 1){
                window.delete(gems[start])
            }else{
                window.set(gems[start],window.get(gems[start])-1)
            }
            start++
            
        }else {
            end++
            if (end >= gems.length){
                break;
            }
            if (window.get(gems[end]) === undefined){
                window.set(gems[end],1)
            }else{
                window.set(gems[end],window.get(gems[end])+1)
            }
        }
    }
    if (answer.length == 1){
        return answer[0][1]
    }
    answer.sort((a,b)=>a[0]-b[0] || a[1][1] - b[1][1])
    return answer[0][1]
}