from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the Hugging Face recipe generator
recipe_generator = pipeline("text-generation", model="gpt2")

# Function to generate a recipe using AI
def generate_ai_recipe(ingredients):
    # Create a prompt for the AI
    prompt = f"Generate a detailed recipe using only the following ingredients: {ingredients}.\n\nRecipe:"
    
    # Generate the recipe using the AI model
    recipe = recipe_generator(prompt, max_length=300, num_return_sequences=1)[0]['generated_text']
    
    # Extract the recipe text (remove the prompt)
    recipe = recipe.replace(prompt, "").strip()
    
    return recipe

@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    try:
        data = request.json
        if not data or 'ingredients' not in data:
            return jsonify({"error": "Missing ingredients"}), 400

        ingredients = data.get('ingredients', '')

        # Generate a recipe using AI
        recipe_text = generate_ai_recipe(ingredients)

        return jsonify({
            "recipe": recipe_text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Handle 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
