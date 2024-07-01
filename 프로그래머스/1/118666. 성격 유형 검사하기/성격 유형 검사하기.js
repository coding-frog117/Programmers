const score = {1:3,2:2,3:1,5:1,6:2,7:3};
const result = [[0,0],[0,0],[0,0],[0,0]]
const type = {'R':[0,0],'T':[0,1],'C':[1,0],'F':[1,1],'J':[2,0],'M':[2,1],'A':[3,0],'N':[3,1]}

function solution(survey, choices) {
    const answer = [];
    for (let i = 0;i<choices.length;i++){
        if (choices[i] < 4){
            const [row,col] = type[survey[i][0]]
            result[row][col] += score[choices[i]]
        }
        else if (choices[i] > 4){
            const [row,col] = type[survey[i][1]]
            result[row][col] += score[choices[i]]
        }
    }
    for (let i =0;i<result.length;i++){
        const [a,b] = result[i]
        if (a>b || a==b){
            result[i][0] = true
        }else{
            result[i][1] = true
        }
    }
    for (const i in type){
        const [row,col] = type[i]
        if (result[row][col] === true){
            answer.push(i)
        }
    }
    return answer.join('')
}
