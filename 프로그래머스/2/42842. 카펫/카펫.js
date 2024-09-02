function solution(brown, yellow) {
    var answer = [];
    
    if (yellow==1){
        answer.push(3);
        answer.push(3);
        
        return answer;
    }
    
    if (yellow==2){
        answer.push(4);
        answer.push(3);
        
        return answer
    }
    
    if (yellow==3){
        answer.push(5);
        answer.push(3);
        
        return answer;
    }
    
    for (let i=1; i<= (yellow/2); i++){
        if (yellow%i === 0){
            const firstNum = i;
            const secondNum = yellow/i+2;
            
            if (isSameToBrown(firstNum, secondNum)){
                answer.push(secondNum);
                answer.push(firstNum+2);
                
                return answer;
            }
        }
        else{
            continue;
        }
        
    }
    
    function isSameToBrown(firstNum, secondNum){
    if ((firstNum*2) + (secondNum*2) === brown){
        return true;
    }
    return false;
}
}

