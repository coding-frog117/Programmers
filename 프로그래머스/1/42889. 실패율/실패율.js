// 해당 스테이지보다 큰 숫자는 참여자, 같은 숫자는 실행중인자 
// N개의 배열에서 [실패율,-번호] 순서대로 두기
// 내림차순 정렬

function solution(N, stages) {
    const play = new Array(N);
    const fail = new Array(N);
    play.fill(0)
    fail.fill(0)
    
    for (let i=0;i<N;i++){
        for (stage of stages){
            if (stage >= i+1){
                play[i] += 1
            }if (stage == i+1){
                fail[i] += 1
            }
        }
    }
    const arr = play.map((item,idx)=>{
        return [fail[idx]/item,idx+1]
    })
    arr.sort((a,b)=> b[0]-a[0])
    const answer = [];
    
    for (const i of arr){
        answer.push(i[1])
    }
    return answer
}