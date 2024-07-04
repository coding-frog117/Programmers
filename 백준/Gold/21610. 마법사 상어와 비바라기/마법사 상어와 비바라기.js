const readline = require('readline');
const rl= readline.createInterface({input:process.stdin,output:process.stdout});

let N = 0;
let M = 0;
let arr = [];
let cnt = 0;
const magic = [];
const dy = [0,-1,-1,-1,0,1,1,1];
const dx = [-1,-1,0,1,1,1,0,-1];

rl.on('line',(line)=>{
  if (N===0){
    const inp = line.split(' ')
    N = parseInt(inp[0])
    M = parseInt(inp[1])
  }
  else if (arr.length < N){
    arr.push(line.split(' ').map(Number))
  } 
  else{
    magic.push(line.split(' ').map(Number));
    cnt++;
    if (cnt >= M){
      rl.close();
    }
  }
})

rl.on('close',()=>{
  const cloud = new Array(N).fill().map(()=>new Array(N).fill(0));
  cloud[N-1][0] = 1
  cloud[N-1][1] = 1
  cloud[N-2][0] = 1
  cloud[N-2][1] = 1

  for (const [dir,pos] of magic){
    move(dir-1,pos,cloud)
    newCloud(cloud)
  }
  let answer =0;
  for (let i=0;i<N;i++){
    for (let j=0;j<N;j++){
      answer += arr[i][j]
    }
  }
  console.log(answer)
})

function move(dir,pos,cloud){
  const move_cloud =[];
  for (let i=0;i<N;i++){
    for (let j=0;j<N;j++){
      if (cloud[i][j] === 1){
        cloud[i][j] = 0
        move_cloud.push(getMoveIdx(dir,pos,i,j))
      }
    }
  }
  for (move_pos of move_cloud){
    const [y,x] = move_pos
    cloud[y][x] = 1
    arr[y][x] += 1
  }
  for (move_pos of move_cloud){
    const [y,x] = move_pos
    const count = diagnal(y,x)
    arr[y][x] += count;
  }
}

function getMoveIdx(dir,pos,y,x){
  let ny = y;
  let nx = x;
  for (let i=0;i<pos;i++){
    ny = ny + dy[dir]
    nx = nx + dx[dir]

    if (ny < 0){
      ny = N-1
    }
    if (nx < 0){
      nx = N-1
    }
    if (ny >= N){
      ny = 0
    }
    if (nx >= N){
      nx = 0
    }
  }
  return [ny,nx]
}

const diagnal_y = [-1,-1,1,1];
const diagnal_x = [-1,1,-1,1];

function diagnal(y,x){
  let cnt = 0;
  for (let i=0;i<4;i++){
    ny = y+diagnal_y[i]
    nx = x+diagnal_x[i]

    if (ny < 0 || ny >= N || nx <0 || nx >= N){
      continue;
    }
    if (arr[ny][nx] > 0){
      cnt++;
    }
  }
  return cnt;
}

function newCloud(cloud){
  for (let i=0;i<N;i++){
    for (let j=0;j<N;j++){
      if (cloud[i][j] === 1){
        cloud[i][j] = 0
      }
      else{
        if (arr[i][j] >= 2){
          cloud[i][j] = 1
          arr[i][j] -= 2
        }
      }
    }
  }
}