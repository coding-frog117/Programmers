// 두글자씩 끊어서저장 , 영문이 아니면 패스
// 합집합 -> B + B에 없는 A의 값
// 교집합 -> A와 B에 있는 값(B에서 제거해가면서 확인)
const pattern = /[a-zA-Z]/;
function checkValidation(str){
    if (pattern.test(str[0]) && pattern.test(str[1])){
        return true
    }return false
}

function iterArr(str){
    const set = [];
    for (let i=0;i<str.length-1;i++){
        curr = str[i]+str[i+1]
        if (checkValidation(curr)){
            set.push(curr.toUpperCase())
        }
    }
    return set
}

function solution(str1, str2) {
    const set1 = iterArr(str1)
    const set2 = iterArr(str2)
    const copyset2 = [...set2]
    const union = [];
    const intersect = [];
    
    for (const str of set1){
        if (copyset2.includes(str)){
            intersect.push(str)
            copyset2.splice(copyset2.indexOf(str),1)
        }else{
            union.push(str)
        }
    }
    const newUnion = union.concat(set2)
    
    if (newUnion.length == 0 && intersect.length == 0){
        return 65536
    }
    if (intersect.length == 0 || newUnion.length == 0){
        return 0
    }
    
    return parseInt(intersect.length/newUnion.length*65536)
}