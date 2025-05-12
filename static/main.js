$(document).ready(function () {
    let quizData = {}; // Store quiz data for the selected recipe
    let currentQuestionIndex = 0;
    let score = 0;

    // Start the quiz for the selected recipe
    $(".start-quiz-btn").click(function () {
        const recipeId = $(this).data("recipe-id");
        quizData = window.recipes[recipeId].quiz; // Load the quiz data for the recipe
        $("#quiz-overlay").show();
        initializeQuiz();
    });

    // Quit the quiz
    $("#quit-quiz-btn, #close-quiz-btn").click(function () {
        $("#quiz-overlay").hide();
    });

    // Restart the quiz
    $("#restart-btn").click(function () {
        initializeQuiz();
    });

    // Initialize the quiz
    function initializeQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        $("#score").text(score);
        $("#quiz-content").show();
        $("#completion-screen").hide();
        loadQuestion();
    }

    // Load the current question
    function loadQuestion() {
        const question = quizData[currentQuestionIndex];
        $("#question-number").text(`Question ${currentQuestionIndex + 1} of ${quizData.length}`);
        $("#question-text").text(question.question);
        $("#options-container").empty();
        $("#feedback-container").hide();
        $("#next-btn").prop("disabled", true);

        question.options.forEach((option, index) => {
            const button = $("<button>")
                .addClass("btn btn-outline-primary option-btn")
                .text(option)
                .click(() => handleOptionClick(index, question.correct));
            $("#options-container").append(button);
        });
    }

    // Handle option click
    function handleOptionClick(selectedIndex, correctIndex) {
        $(".option-btn").prop("disabled", true);
        if (selectedIndex === correctIndex) {
            score++;
            $("#score").text(score);
            $("#feedback-text").text("Correct!").addClass("text-success").removeClass("text-danger");
        } else {
            $("#feedback-text").text("Incorrect!").addClass("text-danger").removeClass("text-success");
        }
        $("#feedback-container").show();
        $("#next-btn").prop("disabled", false);
    }

    // Load the next question or show the completion screen
    $("#next-btn").click(function () {
        currentQuestionIndex++;
        if (currentQuestionIndex < quizData.length) {
            loadQuestion();
        } else {
            $("#quiz-content").hide();
            $("#completion-screen").show();
            $("#final-score").text(score);
        }
    });
});