class Question {
  constructor(text, options, answer) {
    // this
    this.text = text;
    this.options = options;
    this.answer = answer;
  }

  print() {
    console.log(this.text);
    this.options.forEach((value, i) => {
      console.log(`${i + 1}. ${value}`);
    });
  }

  ask() {
    let userAnswer = null;
    while (!userAnswer) {
      userAnswer = prompt("What is your answer? Please enter the number: \n");
    }
    if (!isNaN(Number(userAnswer))) {
      return Number(userAnswer);
    }
  }

  evaluate(userAnswer) {
    return userAnswer === this.answer;
  }
}

const question1 = new Question(
  "Who is the odd one out of Sigma Staff?",
  ["Harry", "Sonali", "Chris"],
  1
);

const question2 = new Question(
  "What is Chris' surname?",
  ["John", "Owen", "Gaston"],
  2
);

const question3 = new Question(
  "What is the capital of China?",
  ["Beijing", "Shanghai", "Taipei"],
  1
);

const question4 = new Question(
  "What is the tallest mountain above sea level?",
  ["K2", "Mauna Kea", "Everest"],
  3
);

function print(question) {
  console.log(question.text);
  question.values.forEach((value, i) => {
    console.log(`${i + 1}. ${value}`);
  });
}

function finish(finalScore, totalScore) {
  console.log("Your score is: " + finalScore + " out of " + totalScore);
}

const round1 = { name: "Sigma Labs", questions: [question1, question2] };

const round2 = { name: "Geography", questions: [question3, question4] };

const rounds = [round1, round2];

function play() {
  let score = 0;
  const noQuestions = rounds.reduce(
    (prev, round) => prev + round.questions.length,
    0
  );
  rounds.forEach((round) => {
    round.questions.forEach((question) => {
      print(question);
      const answer = ask(question);
      const isCorrect = answer === question.answer;
      if (isCorrect) {
        score += 1;
        console.log("Correct!");
      } else {
        console.log("Incorrect!");
      }
    });
  });
  finish(score, noQuestions);
}

// play();
