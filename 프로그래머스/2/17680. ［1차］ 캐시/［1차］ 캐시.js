// 캐시에 있는 자료와 접근 횟수를 기록
// 캐시 히트일 때 time +1하고 해당 이름의 카운트를 1로 갱신, 다른 이들의 카운트 +1
// 캐시 미스일 때 time +5하고 카운트가 가장 높은 것 제거

function solution(cacheSize, cities) {
    const cache = new Map();
    let time = 0;
    
    if (cacheSize == 0){
        return cities.length * 5
    }
    
    for (const c of cities){
        const city = c.toLowerCase()
        if (cache.get(city)){
            time += 1
            cache.set(city, 1)
            for (let [key,value] of cache.entries()){
                if (key != city){
                    cache.set(key, cache.get(key)+1)
                }
            }
        }else{
            time += 5
            if (cache.size < cacheSize){
                cache.set(city, 1)
                for (const [k,v] of cache.entries()){
                    if (k != city){
                        cache.set(k, cache.get(k)+1)
                    }
                }
            }
            else{
                let maxKey = null;
                let maxValue = -Infinity;
                
                for (const [key,value] of cache.entries()){
                    if (value > maxValue){
                        maxKey = key
                        maxValue = value
                    }
                }
                cache.delete(maxKey)
                cache.set(city,1)
                for (const [k,v] of cache.entries()){
                    if (k != city){
                        cache.set(k, cache.get(k)+1)
                    }
                }
            }
        }
    }
    return time
}