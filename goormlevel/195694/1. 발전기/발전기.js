const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let N = 0;
let arr = [];
let answer = 0;

rl.on('line', (line) => {
	if (N === 0){
		N = parseInt(line);
	}else if (arr.length < N){
		arr.push(line.split(' ').map(Number))
	}else{
		rl.close();
	}
});

rl.on('close', () => {
	let vis = new Array(N).fill().map(()=>new Array(N).fill(0))
	for (let i=0;i<N;i++){
		for (let j=0;j<N;j++){
			if (arr[i][j] === 1 && vis[i][j] === 0){
				answer++;
			 	DFS(i,j,vis);
			}
		}
	}
	console.log(answer)
	process.exit()
})

const dy = [0,0,1,-1]
const dx = [1,-1,0,0]

function DFS(i,j,vis){
	let stack =[];
	stack.push([i,j])
	
	while (stack.length > 0){
		const inp = stack.pop();
		const [y,x] = inp;
		for (let t=0;t<4;t++){
			const ny = y + dy[t]
			const nx = x + dx[t]
			
			if (ny<0 || ny >=N || nx <0|| nx>= N){
				continue
			}
			if (vis[ny][nx] === 1){
				continue
			}
			if (arr[ny][nx] === 1){
				stack.push([ny,nx])
				vis[ny][nx] = 1
			}
		}
	}
}
