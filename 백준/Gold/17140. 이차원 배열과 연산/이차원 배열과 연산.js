const readline = require('readline');
const rl = readline.createInterface({input:process.stdin,output:process.stdout});

let arr = new Array();
let cnt = 0;
let r = 0;
let c = 0;
let k = 0;
let time = 0;

rl.on('line',(line)=>{
  if (r == 0){
    const inp = line.split(' ');
    r = inp[0]
    c = inp[1]
    k = inp[2]
  }else{
    arr.push(line.split(' '));
    cnt++;
    if (cnt >= 3){
      rl.close();
    }
  }
})

rl.on('close',()=>{
  while (true){
    if (arr.length >= r && arr[0].length >= c){
      if (arr[r-1][c-1] == k){
        console.log(time);
        break;
      }
    }
    if (countLength(arr) == 'R'){
      arr = R(arr);
    }
    else{
      arr = C(arr);
    }
    time++
    if (time > 100){
      console.log(-1)
      break
    }
  }
})

function countLength(arr){
  if (arr.length >= arr[0].length){
    return 'R'
  }else {
    return 'C'
  }
}

function R(arr){
  let newRow = []
  let maxLen = 0;
  for (let i=0; i<arr.length;i++){
    newRow.push([])
    let count = {};
    // 각 숫자 등장 횟수 세기
    for (j of arr[i]){
      if (j == 0){
        continue
      }
      if (count[j] == undefined){
        count[j] = 1
      }else{
        count[j] += 1
      }
    }
    let len = counting(count,i,newRow)
    maxLen = maxLen >= len ? maxLen : len
  }
  return fillZero(newRow,maxLen)
}

function C(arr){
  let newCol = new Array(arr[0].length);
  let countingCol = new Array(arr[0].length);
  let maxLen =0;

  for (let i=0;i<newCol.length;i++){
    newCol[i]= [];
    for (let j =0;j<arr.length;j++){
      newCol[i].push(0)
    }
    countingCol[i] = [];
  }
  
  // 열을 뽑아내기
  newCol = getRowArr(arr,newCol)
  // 열을 돌면서 수와 등장횟수 기록
  for (let i=0;i<newCol.length;i++){
    let count = {};
    for (j of newCol[i]){
      if (j == 0){
        continue;
      }
      if (count[j] == undefined){
        count[j] = 1
      }else{
        count[j] += 1
      }
    }
    let len = counting(count,i,countingCol);
    maxLen = maxLen >= len ? maxLen : len;
  }
  let changedCol= fillZero(countingCol,maxLen)
  let changedNewCol = new Array(changedCol[0].length);
  for (let i=0;i<changedNewCol.length;i++){
    changedNewCol[i] = [];
  }
  changedNewCol = getRowArr(changedCol,changedNewCol)
  return changedNewCol
}

function getRowArr(arr,newCol){
  for (let i =0;i<arr[0].length;i++){
    for (let j=0;j<arr.length;j++){
      newCol[i][j] = arr[j][i]
    }
  }
  return newCol
}

function counting(arr,i,newArr){
  let countArr = Object.entries(arr).sort((a,b)=>a[1]-b[1])

  for (const [key,val] of countArr){
    newArr[i].push(key);
    newArr[i].push(val.toString());
  }
  if (newArr[i].length > 100){
    newArr[i] = newArr[i].slice(0,100)
  }
  return newArr[i].length
}

function fillZero(arr,n){
  for (let i=0;i<arr.length;i++){
    while (arr[i].length < n){
      arr[i].push('0')
    }
  }
  return arr;
}