// record 돌면서 Enter거나 change면 map에 저장, Leave면 건너뛰기, 
// 다시 돌면서 id에 해당하는 닉네임 출력

function solution(record) {
    const maps = {}
    const result = [];
    
    for (i of record){
        const [type,id,name] = i.split(' ')
        if (type == 'Enter' || type == 'Change'){
            maps[id] = name
        }
    }
    for (i of record){
        const [type,id,name] = i.split(' ')
        if (type == 'Enter'){
            result.push(`${maps[id]}님이 들어왔습니다.`)
        } else if (type == 'Leave'){
            result.push(`${maps[id]}님이 나갔습니다.`)
        }
    }
    return result
}