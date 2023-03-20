function solution(answers) {
    let answer = [];

  let one = [1, 2, 3, 4, 5];
  let two = [2, 1, 2, 3, 2, 4, 2, 5];
  let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let countOne = 0;
  let countTwo = 0;
  let countThree = 0;

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === one[i % one.length]) {
      countOne++;
    }
    if (answers[i] === two[i % two.length]) {
      countTwo++;
    }
    if (answers[i] === three[i % three.length]) {
      countThree++;
    }
  }

  let max = Math.max(countOne, countTwo, countThree);
  console.log(countOne, countTwo, countThree);

  if (max === countOne) {
    answer.push(1);
  }
  if (max === countTwo) {
    answer.push(2);
  }
  if (max === countThree) {
    answer.push(3);
  }

  return answer;
}