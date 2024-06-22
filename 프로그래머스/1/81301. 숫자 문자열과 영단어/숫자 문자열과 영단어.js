const str = {'one':'1','two':'2','three':'3','four':'4',"five":'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}

let newS = ''

function solution(s) {
    [...s].forEach((i,idx)=>{
        if (isNaN(i)){
            if (s.slice(idx,idx+3) in str){
                newS += str[s.slice(idx,idx+3)]
            }
            else if (s.slice(idx,idx+4) in str){
                newS += str[s.slice(idx,idx+4)]
            }else if (s.slice(idx,idx+5) in str){
                newS += str[s.slice(idx,idx+5)]
            }
        }else{
            newS += i
        }
    })
    return Number(newS)
}