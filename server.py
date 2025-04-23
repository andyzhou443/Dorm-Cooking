from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import redirect, url_for
app = Flask(__name__)

recipes = {
    1: {
        "name": "Scrambled Eggs",
        "image": "scrambled_eggs.jpg",
        "time": "5 Minutes",
        "cost": "$",
        "genre": "Breakfast",
        "difficulty": "Easy",
        "ingredients": ["2 eggs", "1 tbsp butter", "Salt", "Pepper"],
        "steps": [
            "Crack eggs into a bowl.",
            "Whisk until yolks and whites are blended.",
            "Heat butter in pan over medium heat.",
            "Pour in eggs and stir until cooked through."
        ],
        "quiz": [
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
    },
    2: {
        "name": "Mediterranean Chickpea Salad",
        "image": "chickpea_salad.jpg",
        "time": "20 Minutes",
        "cost": "$$",
        "genre": "Lunch/Dinner",
        "difficulty": "Easy",
        "ingredients": ["1 can chickpeas (15 oz), drained and rinsed", "1 cucumber, diced", "1 small red onion, finely chopped", "½ cup crumbled feta cheese", "2–3 tablespoons olive oil", "2 tablespoons lemon juice (freshly squeezed)"],
        "steps": [
            "Rinse chickpeas and drain.",
            "Chop cucumber, onion, and feta.",
            "Mix everything in a bowl and dress with olive oil and lemon juice."
        ],
        "quiz": [
            {
                "id": 1,
                "question": "What is the main protein source in this salad?",
                "options": ["Chickpeas", "Feta cheese", "Olive oil", "Lemon juice"],
                "correct": 0,
                "explanation": "Chickpeas provide the main source of protein."
            }
        ]
    },
    3: {
        "name": "Sausage Egg n' Cheese",
        "image": "sausage_egg_cheese.jpg",
        "time": "15 Minutes",
        "cost": "$",
        "genre": "Breakfast/Lunch",
        "difficulty": "Easy",
        "ingredients": ["1 sausage patty", "1 egg", "1 slice cheese", "1 sandwich bun", "Butter"],
        "steps": [
            "Cook sausage patty in a pan over medium heat.",
            "Crack egg into the same pan and cook until desired doneness.",
            "Toast the sandwich bun with a little butter.",
            "Assemble the sandwich by placing the sausage, egg, and cheese on the bun."
        ],
        "quiz": [
            {
                "id": 1,
                "question": "What is the best way to cook the sausage patty?",
                "options": ["Grill it", "Pan-fry it", "Microwave it", "Bake it"],
                "correct": 1,
                "explanation": "Pan-frying the sausage patty gives it a crispy texture and enhances the flavor."
            },
            {
                "id": 2,
                "question": "What type of cheese is commonly used for a Sausage Egg n' Cheese sandwich?",
                "options": ["Cheddar", "Swiss", "American", "Mozzarella"],
                "correct": 2,
                "explanation": "American cheese is typically used for its meltability and mild flavor."
            }
        ]
    },
    4: {
        "name": "Avocado Toast",
        "image": "avocado_toast.jpg",
        "time": "10 Minutes",
        "cost": "$",
        "genre": "Breakfast",
        "difficulty": "Easy",
        "ingredients": ["2 slices of bread", "1 ripe avocado", "Lemon juice", "Salt", "Pepper", "Olive oil"],
        "steps": [
            "Toast the slices of bread.",
            "Mash the avocado with lemon juice, salt, and pepper.",
            "Spread the mashed avocado onto the toasted bread.",
            "Drizzle with olive oil and serve."
        ],
        "quiz": [
            {
                "id": 1,
                "question": "What is the main ingredient of avocado toast?",
                "options": ["Tomato", "Avocado", "Cucumber", "Lettuce"],
                "correct": 1,
                "explanation": "The main ingredient in avocado toast is mashed avocado."
            },
            {
                "id": 2,
                "question": "Which of the following is a typical topping for avocado toast?",
                "options": ["Cheese", "Tomatoes", "Peanut butter", "Butter"],
                "correct": 1,
                "explanation": "Tomatoes are commonly used as a topping for avocado toast."
            }
        ]
    },
    5: {
        "name": "Chicken Stir Fry",
        "image": "chicken_stir_fry.jpg",
        "time": "25 Minutes",
        "cost": "$$",
        "genre": "Lunch/Dinner",
        "difficulty": "Medium",
        "ingredients": ["1 chicken breast", "1 bell pepper", "1 onion", "Soy sauce", "Garlic", "Ginger", "Olive oil"],
        "steps": [
            "Cut the chicken breast into strips.",
            "Chop the bell pepper and onion.",
            "Heat olive oil in a pan and cook the chicken until browned.",
            "Add the garlic, ginger, onion, and bell pepper, and stir-fry for 5-7 minutes.",
            "Add soy sauce and stir for another minute. Serve."
        ],
        "quiz": [
            {
                "id": 1,
                "question": "What is the key seasoning in a stir-fry?",
                "options": ["Soy sauce", "Salt", "Pepper", "Lemon juice"],
                "correct": 0,
                "explanation": "Soy sauce is typically used as the key seasoning in stir-fry dishes."
            },
            {
                "id": 2,
                "question": "What is an important ingredient for adding flavor to stir-fry?",
                "options": ["Garlic", "Tomatoes", "Cinnamon", "Chocolate"],
                "correct": 0,
                "explanation": "Garlic is an important flavoring agent in stir-fry recipes."
            }
        ]
    },
    6: {
        "name": "Quesadillas",
        "image": "quesadillas.jpg",
        "time": "15 Minutes",
        "cost": "$$",
        "genre": "Lunch/Dinner",
        "difficulty": "Medium",
        "ingredients": ["2 tortillas", "Cheese", "Sour cream", "Salsa", "Chicken or beef (optional)"],
        "steps": [
            "Heat a tortilla in a pan over medium heat.",
            "Add cheese and optional meat on one half of the tortilla.",
            "Fold the tortilla and cook until both sides are golden and the cheese is melted.",
            "Serve with sour cream and salsa."
        ],
        "quiz": [
            {
                "id": 1,
                "question": "What is the main filling in a quesadilla?",
                "options": ["Cheese", "Meat", "Vegetables", "Rice"],
                "correct": 0,
                "explanation": "The main filling in a quesadilla is typically cheese."
            },
            {
                "id": 2,
                "question": "What is commonly served alongside quesadillas?",
                "options": ["Sour cream and salsa", "Chips", "Rice", "Salad"],
                "correct": 0,
                "explanation": "Quesadillas are often served with sour cream and salsa on the side."
            }
        ]
    }
}


current_id = 4

# ROUTES

@app.route('/')
def home():
   return render_template('index.html', recipes=recipes)  

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/all_recipes')
def all_recipes():
    return render_template('all_recipes.html', recipes=recipes)

@app.route("/recipes/<int:recipe_id>")
def show_recipe(recipe_id):
    print(f"recipes: {recipes}")  # Debugging line
    recipe = recipes.get(recipe_id)
    if not recipe:
        return f"Recipe with ID {recipe_id} not found", 404
    return render_template("recipe.html", recipe=recipe)


if __name__ == '__main__':
   app.run(debug = True, port=5001)