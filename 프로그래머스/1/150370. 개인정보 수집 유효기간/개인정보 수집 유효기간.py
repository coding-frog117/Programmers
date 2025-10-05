def solution(today, terms, privacies):
    answer = []
    today = "".join(today.split("."))
    
    terms_range = {}
    for t in terms:
        category, month = t.split()
        terms_range[category] = int(month)
    
    for idx, p in enumerate(privacies):
        start, category = p.split()
        year, month, day = map(int, start.split("."))
        
        month += terms_range[category]
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1
        
        day -= 1
        if day == 0:
            day = 28
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        
        end =""
        for i in [str(year),str(month),str(day)]:
            if len(i) == 1:
                end += ("0" + i)
            else:
                end += i
        
        if today > end:
            answer.append(idx + 1)
    
    return answer