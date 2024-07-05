// 맵 두개에 장르별 총 재생횟수, 각 곡마다 재생횟수 저장(인덱스와 같이)
// 장르별 총 재생횟수 정렬, 각 곡마다 재생횟수 정렬(2개 이상이면 제거)
// 인덱스로 새로운 배열 생성

function solution(genres, plays) {
    let total_play = new Map();
    let each_play = new Map();
    const answer = [];
    
    for (let i=0;i<genres.length;i++){
        const data = total_play.get(genres[i])
        if (data == undefined){
            total_play.set(genres[i],plays[i])
            each_play.set(genres[i],[[plays[i],i]])
        }else{
            const each_data = each_play.get(genres[i])
            total_play.set(genres[i],data + plays[i])
            each_play.set(genres[i],[...each_data, [plays[i],i]])
        }
    }
    
    total_play = [...total_play]
    
    total_play.sort((a,b)=> b[1]-a[1])
    each_play.forEach((item)=>{
        item.sort((a,b)=> b[0]-a[0] || a[1]-b[1])
    })
    
    for (const [genre,play] of total_play){
        let cnt = 0;
        for (const [count,idx] of each_play.get(genre)){
            answer.push(idx)
            cnt++;
            if (cnt >= 2){
                break;
            }
        }
    }
    return answer
}