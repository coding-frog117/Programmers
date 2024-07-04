const readline=require('readline');
const rl = readline.createInterface({input:process.stdin,output:process.stdout});

let N = 0;
const member = new Map();
let cnt = 0;
const dy = [0,0,1,-1];
const dx = [1,-1,0,0];

rl.on('line',(line)=>{
  if (N==0){
    N = parseInt(line);
  }else{
    const [mem,...like]=line.split(' ');
    member.set(mem,[...like])
    cnt++;
    if (cnt > N*N){
      rl.close();
    }
  }
})

rl.on('close',()=>{
  const arr = new Array(N).fill().map(()=>new Array(N).fill(0))
  for (const [num,friends] of member){
    if (num == ''){
      continue
    }
    const res = getCloseInfo(arr,friends);
    arr[res[2]][res[3]] = num
  }
  console.log(calResult(arr))
})

function getCloseInfo(arr,friends){
  const closeInfo = [];

  for (let i=0;i<N;i++){
    for (let j=0;j<N;j++){
      if (arr[i][j] == 0){
        closeInfo.push(checkAround(arr,i,j,friends));
      }
    }
  }
  closeInfo.sort((a,b)=>b[0]-a[0] || b[1]-a[1] || a[2]-b[2] || a[3]-b[3])
  return closeInfo[0]
}

function checkAround(arr,y,x,friends){
  const curr_info =[0,0,y,x];

  for (let i=0;i<4;i++){
    const ny = y + dy[i]
    const nx = x + dx[i]

    if (ny < 0 || ny >= N || nx <0 || nx>=N){
      continue;
    }
    if (friends.includes(arr[ny][nx])){
      curr_info[0] += 1
    }else if (arr[ny][nx] === 0){
      curr_info[1] += 1
    }
  }
  return curr_info
}

function calResult(arr){
  let result = 0;
  for (let i =0;i<N;i++){
    for (let j =0;j<N;j++){
      const friends = member.get(arr[i][j])
      const count = counting(i,j,friends,arr)
      if (count > 0){
        result += 10**(counting(i,j,friends,arr)-1)
      }
    }
  }
  return result
}

function counting(y,x,friends,arr){
  let count = 0;
  for (let i=0;i<4;i++){
    const ny = y + dy[i]
    const nx = x + dx[i]

    if (ny < 0 || ny >= N || nx <0 || nx>=N){
      continue;
    }
    if (friends.includes(arr[ny][nx])){
      count += 1;
    }
  }
  return count
}