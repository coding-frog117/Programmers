// 각 칸마다 가능한 19가지 경우를 모두 체크
const readline = require('readline');
const rl = readline.createInterface({input:process.stdin,output:process.stdout})

let N = 0;
let M = 0;
const arr = new Array();
let cnt =0;
const allCases_y = [[0,0,0,0],[0,1,2,3],[0,0,1,1],[0,1,2,2],[0,0,0,1],[0,0,0,1],[-2,-1,0,0],[0,1,1,1],[0,0,1,2],[0,0,1,2],[-1,0,0,0],[0,1,1,2],[0,0,1,1],[-1,0,0,1],[-1,-1,0,0],[0,0,0,1],[-1,0,0,1],[-1,0,0,0],[0,1,1,2]]
const allCases_x = [[0,1,2,3],[0,0,0,0],[0,1,0,1],[0,0,0,1],[0,1,2,0],[0,1,2,2],[1,1,0,1],[0,0,1,2],[0,1,0,0],[0,1,1,1],[2,0,1,2],[0,0,1,1],[0,1,1,2],[1,0,1,0],[1,2,0,1],[0,1,2,1],[1,0,1,1],[1,0,1,2],[0,0,1,0]]

rl.on('line',(line)=>{
  if (N == 0){
    const [i,j] = line.split(' ');
    N = i;
    M = j;
  }else {
    arr.push(line.split(' '))
    cnt++
    if (cnt == N){
      rl.close();
    }
}})

rl.on('close',()=>{
  let answer = 0;
  for (let i=0;i<N;i++){
    for (let j=0;j<M;j++){
      const res = checkIdx(i,j)
      answer = answer >= res ? answer : res
    }
  }
  console.log(answer)
})

function checkIdx(y,x){
  let maxSum =0;
  allCases_y.forEach((item,idx)=>{
    let isPossible = true;
    let sum = 0;

    for (let i=0;i<4;i++){
      const ny = y+item[i]
      const nx = x+allCases_x[idx][i]

      if (ny < 0 || nx < 0 || ny >= N || nx >= M){
        isPossible = false;
        break
      }else{
        sum += parseInt(arr[ny][nx]);
      }
    }
    if (isPossible){
      maxSum = maxSum >= sum ? maxSum : sum
  }
  })
  return maxSum
}