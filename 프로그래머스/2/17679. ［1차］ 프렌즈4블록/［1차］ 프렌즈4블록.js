function search(board,m,n){
    const dy = [0,1,1]
    const dx = [1,1,0]
    
    let curr = '';
    let isPop = false;
    const change = new Set();
    
    for (let i=0;i<m;i++){
        for (let j=0; j<n;j++){
            curr = board[i][j];
            if (curr == null){
                continue
            }
            let isPossible = true;
            for (let idx=0;idx<3;idx++){
                ny = i + dy[idx]
                nx = j + dx[idx]

                if (ny >= m || nx >= n){
                    isPossible = false
                    break
                }if (board[ny][nx] != curr){
                    isPossible = false
                    break
                }
            }
            if (isPossible){
                isPop = true
                change.add([i,j])
                change.add([i+1,j])
                change.add([i,j+1])
                change.add([i+1,j+1])
            }
        }
    }
    if (isPop){
        return change
    }return false
}

function makeNewBoard(board,m,n){
    const newBoard = new Array(m).fill(null).map(()=>new Array(n).fill(null))
    for (let j=n-1;j>=0;j--){
        let curr_y = m-1
        for (let i=m-1;i>=0;i--){
            if (board[i][j] == null){
                continue
            }
            newBoard[curr_y][j] = board[i][j]
            curr_y -=1
        }
    }
    return newBoard
}

function iter(board,m,n){
    let cnt = 0;
    while (true){
        const ans = search(board,m,n)
        if (ans == false){
            return cnt
        }
        for (const [y,x] of ans){
            if (board[y][x] != null){
                cnt += 1;
            } 
            board[y][x] = null
        }
        const newBoard = makeNewBoard(board,m,n)
        board = newBoard
    }    
}

function solution(m, n, board) {
    for (let i=0;i<m;i++){
        board[i] = [...board[i]]
    }
    return iter(board,m,n)
}