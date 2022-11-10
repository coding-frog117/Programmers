def solution(record):
    result = []
    id_name={}
    
    for i in record:
        if "Leave" not in i:          
            string=i.split()            
            id_name[string[1]]=string[2]
             
    for i in record:
        name=i.split()
        if "Enter" in i:
            result.append("%s님이 들어왔습니다."%id_name[name[1]])
        elif "Leave" in i:
            result.append("%s님이 나갔습니다."%id_name[name[1]])
        else:
            pass
         
    return result