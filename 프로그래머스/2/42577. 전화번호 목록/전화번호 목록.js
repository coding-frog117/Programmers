// 번호를 1부터 번호 길이까지 쪼개서 모두 저장
// 이미 존재하는 접두어면 return false

const phone_front = {};
const origin_number = {};

function solution(phone_book) {
    for (const number of phone_book){
        origin_number[number] = 1
    }
    
    for (const number of phone_book){
        if (!splitNumber(number,phone_book)){
            return false
        }
    }
    return true
}

function splitNumber(number,phone_book){
    let curr_str = '';
    for (const i of number){
        curr_str += i
        if (phone_front[curr_str] === undefined){
            phone_front[curr_str] = 1
        }
        else {
            if (origin_number[curr_str]){
                return false
            }
        }
    }return true
}