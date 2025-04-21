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


current_id = 4

# ROUTES

@app.route('/')
def hello_world():
   return render_template('hello_world.html')   

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




