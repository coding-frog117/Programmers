# m과 일치하는 문자열 있으면 배열에 담아주기 [재생시간,인덱스]

stringifyMap = {'C#':'k','D#':'L','F#':'M','G#':'N','A#':'O','B#':'P'}
    
def timeCul(start,end):
    start_m,start_s = start.split(':')
    end_m,end_s = end.split(':')
    hour = (int(end_m) - int(start_m))*60
    minuets = int(end_s) - int(start_s)
    return hour + minuets
    
def invertNewInfo(singInfo):
    for key,value in stringifyMap.items():
        singInfo = singInfo.replace(key,value)
        
    return singInfo

def solution(m, musicinfos):
    answer = []
    musics = [[] for i in range(len(musicinfos) // 4)]
    m = invertNewInfo(m)
    
    for idx in range(len(musicinfos)):
        start,end,name,singInfo = musicinfos[idx].split(',')
        playTime = timeCul(start,end)
        newSingInfo = invertNewInfo(singInfo)

        # 재생 시간이 악보 문자열 길이보다 길면 (재생시간 - 악보 길이)한 것 만큼 악보를 더해주기
        if playTime > len(newSingInfo) :
            appendLen,mod = divmod(playTime,len(newSingInfo))
            newSingInfo = (newSingInfo * appendLen) + newSingInfo[:mod]
            
            if m in newSingInfo:
                answer.append([-playTime,idx,name])
                
        # 재생 시간이 악보 문자열 길이보다 짧으면 재생시간만큼 자르기
        elif playTime < len(newSingInfo) :
            newSingInfo = newSingInfo[:playTime]
            
            if m in newSingInfo:
                answer.append([-playTime,idx,name])
                
        # 재생 시간이 악보 문자열 길이와 같다면 바로 비교
        elif playTime == len(newSingInfo):
            if m in newSingInfo:
                answer.append([-playTime,idx,name])
    
    if not answer :
        return '(None)'
    
    answer = sorted(answer)
    return answer[0][2]