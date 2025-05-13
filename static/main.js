$(document).ready(function () {
   
    const quizData = {{ recipe.quiz | tojson }};
    
    let userSelections = [];  // store chosen index per question
    let currentQuestionIndex = 0;
    let score = 0;
    let questionAnswered = false; // Track if current question has been answered

    const startQuizButton      = document.getElementById('start-quiz-btn');
    const quizOverlay          = document.getElementById('quiz-overlay');
    const questionNumberElement = document.getElementById('question-number');
    const questionTextElement   = document.getElementById('question-text');
    const optionsContainer      = document.getElementById('options-container');
    const nextButton            = document.getElementById('next-btn');
    const scoreElement          = document.getElementById('score');
    const feedbackContainer     = document.getElementById('feedback-container');
    const feedbackTextElement   = document.getElementById('feedback-text');
    const quizContent           = document.getElementById('quiz-content');
    const completionScreen      = document.getElementById('completion-screen');
    const finalScoreElement     = document.getElementById('final-score');
    const restartButton         = document.getElementById('restart-btn');
    const closeQuizButton       = document.getElementById('close-quiz-btn');
    const quitQuizButton        = document.getElementById('quit-quiz-btn');

    document.addEventListener('DOMContentLoaded', function () {
    const toggleCheck = (selector) => {
      document.querySelectorAll(selector).forEach(item => {
        item.addEventListener('click', () => {
          item.classList.toggle('checked');
        });
      });
    };

    toggleCheck('.equipment-item');
    toggleCheck('.ingredient-item');
  });

    startQuizButton.addEventListener('click', () => {
        quizOverlay.style.display = 'flex';
        console.log(quizData)
        initializeQuiz();
    });

    closeQuizButton.addEventListener('click', () => {
        quizOverlay.style.display = 'none';
    });
    
    quitQuizButton.addEventListener('click', () => {
        quizOverlay.style.display = 'none';
    });

    function initializeQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        questionAnswered = false;
        userSelections = [];
        scoreElement.textContent = score;
        quizContent.style.display      = 'block';
        completionScreen.style.display = 'none';
        loadQuestion();
    }

    function loadQuestion() {
        const currentQuestion = quizData[currentQuestionIndex];
        questionNumberElement.textContent = 
            `Question ${currentQuestionIndex + 1} of ${quizData.length}`;
        questionTextElement.textContent = currentQuestion.question;
        feedbackContainer.style.display = 'none';
        nextButton.disabled = true;
        questionAnswered = false; // Reset for new question

        optionsContainer.innerHTML = '';

        currentQuestion.options.forEach((option, index) => {
            const btn = document.createElement('div');
            btn.classList.add('option');
            btn.textContent = option;

            btn.addEventListener('click', () => {
                if (questionAnswered) {
                    return;
                }
                questionAnswered = true;

                // record selection:
                userSelections[currentQuestionIndex] = index;
                
                // clear previous highlights
                document.querySelectorAll('.option')
                        .forEach(opt => opt.classList.remove('selected','correct','incorrect'));

                btn.classList.add('selected');

                if (index === currentQuestion.correct) {
                    btn.classList.add('correct');
                    score++;
                    scoreElement.textContent = score;
                    feedbackTextElement.textContent = "Correct!";
                } else {
                    btn.classList.add('incorrect');
                    // highlight the right answer
                    document.querySelectorAll('.option')[currentQuestion.correct]
                            .classList.add('correct');
                    feedbackTextElement.textContent = currentQuestion.explanation;
                }

                // Remove previous status classes
                feedbackContainer.classList.remove('correct', 'incorrect');

                if (index === currentQuestion.correct) {
                    feedbackContainer.classList.add('correct');
                } else {
                    feedbackContainer.classList.add('incorrect');
                }

                feedbackContainer.style.display = 'block';
                nextButton.disabled = false;
            });

            optionsContainer.appendChild(btn);
        });
    }

    nextButton.addEventListener('click', () => {
        currentQuestionIndex++;
        if (currentQuestionIndex < quizData.length) {
            loadQuestion();
        } else {
            // hide quiz UI
            quizContent.style.display      = 'none';
            completionScreen.style.display = 'block';
            finalScoreElement.textContent  = score;

            // build review
            const review = document.getElementById('review-container');
            review.innerHTML = '';  // clear old

            quizData.forEach((q, i) => {
            // question wrapper
            const qDiv = document.createElement('div');
            qDiv.classList.add('review-question');

            // question text
            const qText = document.createElement('p');
            qText.classList.add('question');
            qText.innerHTML = `Question ${i+1}: ${q.question}`;
            qDiv.appendChild(qText);

            // options list
            q.options.forEach((opt, idx) => {
                const optDiv = document.createElement('div');
                optDiv.classList.add('option');

                // mark user’s pick
                if (userSelections[i] === idx) {
                optDiv.classList.add('selected');
                }
                // mark correctness
                if (idx === q.correct) {
                optDiv.classList.add('correct');
                } else if (userSelections[i] === idx && idx !== q.correct) {
                optDiv.classList.add('incorrect');
                }

                optDiv.textContent = opt;
                qDiv.appendChild(optDiv);
            });

            // explanation
            const expl = document.createElement('p');
            expl.classList.add('explanation');
            expl.innerHTML = `<em>Explanation:</em> ${q.explanation}`;
            qDiv.appendChild(expl);

            review.appendChild(qDiv);
            });
        }
    });


    restartButton.addEventListener('click', initializeQuiz);
    document.querySelectorAll(".dropdown-btn").forEach(button => {
        button.addEventListener("click", () => {
            const content = button.nextElementSibling;
            content.style.display = content.style.display === "block" ? "none" : "block";
        });
    });
});