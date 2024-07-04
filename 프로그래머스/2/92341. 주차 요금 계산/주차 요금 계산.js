const parking = {};
const times = {};
const answer = [];

function solution(fees, records) {
    for (const record of records){
        const [time,car,type] = record.split(' ');
        if (type == 'IN'){
            parking[car] = [time.split(':').map(Number)]
        }else{
            const start = parking[car].pop()
            const end = time.split(':').map(Number)
            changeTime(start,end,car)
        }
    }
    for (const [car,val] of Object.entries(parking)){
        if (val.length > 0){
            const start = val.pop()
            const end = [23,59];
            changeTime(start,end,car)
        }
    }
    for (const [car,time] of Object.entries(times)){
        answer.push([car,changeFee(car,time,fees)])
    }
    answer.sort((a,b)=>a[0]-b[0])
    
    const answer_fee = [];
    for (const [car,fee] of answer){
        answer_fee.push(fee)
    }
    return answer_fee
}

function changeTime(start,end,car){
    const [s_hour,s_min] = start
    const [e_hour,e_min] = end
    const time = (e_hour*60+e_min)-(s_hour * 60+s_min)
    if (times[car] == undefined){
        times[car] = time
    }
    else{
        times[car] += time
    }
}

function changeFee(car,times,fee){
    const [init,init_fee,per,per_fee]=fee
    if (times > init){
        const remained_time = times-init
        return init_fee+(Math.ceil(remained_time/per)*per_fee);
    }else{
        return init_fee;
    }
}