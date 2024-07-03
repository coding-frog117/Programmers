const possibleString = ['-','_','.'];
const eng = /[a-zA-Z]/;
const num = /[0-9]/;

function solution(new_id) {
    new_id = new_id.toLowerCase()
    let i = 0;
    while (true){
        if (!eng.test(new_id[i]) && !num.test(new_id[i]) && !possibleString.includes(new_id[i])){
            new_id = new_id.slice(0,i)+new_id.slice(i+1);
        }
        else{
            i++
            if (i>new_id.length-1){
                break
            }
        }
    }
    while (new_id.includes('..')){
        new_id = new_id.replaceAll('..','.')
    }
    
    if (new_id[0] === '.'){
        new_id = new_id.slice(1)
    }
    if (new_id.length > 0){
        if (new_id[new_id.length-1] === '.'){
            new_id = new_id.slice(0,new_id.length-1)
        }
    }
    if (new_id.length === 0){
        new_id = 'a'
    }
    if (new_id.length >= 16){
        new_id = new_id.slice(0,15)
    }
    if (new_id[new_id.length-1] === '.'){
        new_id = new_id.slice(0,new_id.length-1)
    }
    while (new_id.length < 3){
        new_id += new_id[new_id.length-1]
    }
    return new_id
}