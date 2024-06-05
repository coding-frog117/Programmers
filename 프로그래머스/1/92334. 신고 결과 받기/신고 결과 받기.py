def solution(id_list, report, k):
    banCount = {}
    reportBoard = {}
    banList = []
    answer = [0 for i in range(len(id_list))]
    
    for i in id_list:
        banCount[i] = 0
        reportBoard[i] = []
    
    for i in report:
        reporter,reported = i.split()
        if reported not in reportBoard[reporter]:
            banCount[reported] += 1
            reportBoard[reporter].append(reported)
    
    for key,values in banCount.items():
        if values >= k:
            banList.append(key)
    
    for idx,val in enumerate(id_list):
        curr_report = reportBoard[val]
        for i in curr_report:
            if i in banList:
                answer[idx] += 1
    return answer