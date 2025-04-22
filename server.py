from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import redirect, url_for
app = Flask(__name__)

Recipe = {
    "1": {
    },
    "2": {
    },
    "3": {
    },
    "4": {
    }

}

quiz_data = [
    {
        "id": 1,
        "question": "After adding milk or water to the mix, what's the next step?",
        "options": ["Preheat the pan", "Add salt", "Put in the eggs", "Whisk again"],
        "correct": 3,  # Index of correct answer (0-based)
        "explanation": "The eggs should already be in and mixed by the time you're adding milk or water."
    },
    {
        "id": 2,
        "question": "For a nice creamy scramble, you should...",
        "options": ["Stop when the eggs are mostly set, but a little liquid egg remains", 
                   "Whisk harder", 
                   "Add pepper", 
                   "Cook the eggs for longer than recommended"],
        "correct": 0,
        "explanation": "Stopping when eggs are mostly set but still slightly liquid ensures a creamy texture."
    }
]

current_id = 4

# ROUTES

@app.route('/')
def home():
   return render_template('index.html')   

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


if __name__ == '__main__':
   app.run(debug = True, port=5001)




