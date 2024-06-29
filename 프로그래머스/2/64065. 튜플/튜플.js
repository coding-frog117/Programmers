// 원소의 갯수가 작은 것부터 정렬 후 배열에 없는 값을 추가해감

function solution(s) {
    const answer = [];
// s를 배열에 담기
    
    s= s.slice(2,-2)
    const sets = s.split('},{')
    const checkArr= [];

    for (let i of sets){
        i = i.split(',').map(Number);
        checkArr.push(i)
    }
    
    checkArr.sort((a,b)=>a.length - b.length)
    for (const i of checkArr){
        for (const j of i){
            if (!answer.includes(j)){
                answer.push(j)
            }
        }
    }return answer
}