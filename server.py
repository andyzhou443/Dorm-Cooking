import random
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import redirect, url_for
app = Flask(__name__)
import json, os

recipe_file = 'recipes.json'

def load_recipes():
    if os.path.exists(recipe_file):
        with open(recipe_file, 'r') as f:
            return json.load(f)
    return {}

recipes = load_recipes()


def get_random_recipes(n=3):
    # returns a list of (recipe_id, recipe_dict) tuples
    return random.sample(list(recipes.items()), n)


current_id = 4

# ROUTES

@app.route('/')
def home():
    random_recipes = get_random_recipes(3)
    return render_template('index.html', random_recipes=random_recipes)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/all_recipes')
def all_recipes():
    return render_template('all_recipes.html', recipes=recipes)

@app.route("/recipes/<recipe_id>")
def show_recipe(recipe_id):
    print(f"recipes: {recipes}")  # Debugging line
    recipe = recipes.get(recipe_id)
    if not recipe:
        return f"Recipe with ID {recipe_id} not found", 404
    return render_template("recipe.html", recipe=recipe)

@app.route("/ingredients")
def ingredients():
    return render_template('ingredients.html')

@app.route("/equipment")
def equipment():
    return render_template('equipment.html')



if __name__ == '__main__':
   app.run(debug = True, port=5001)