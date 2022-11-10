def solution(board, moves):
    stack=[]
    count=0
             
    for move in moves:
        for i in range(len(board)):
            num=board[i][move-1]
            if num==0:
                pass

            elif len(stack)==0:
                stack.append(num)
                board[i][move-1]=0
                break
            else:
                if stack[-1]==num:
                    stack.pop()
                    count+=2
                        
                else:
                    stack.append(num)
                board[i][move-1]=0
                break
             
    return count