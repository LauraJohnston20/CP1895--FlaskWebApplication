from flask import Flask, render_template, url_for, request
import csv
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'

@app.route("/")
@app.route("/home")
def home():
    recipe_images = []
    with open("photos.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            recipe_images.append(row)
    return render_template("home.html", recipe_images=recipe_images)


@app.route("/view_recipes")
def view_recipes():
    recipe_list = read_from_csv()
    return render_template('view_recipes.html', recipe_list=recipe_list)


@app.route("/add_recipes", methods=["POST", "GET"])
def add_recipes():
    if request.method == "POST":
        recipe_name = request.form["recipeName"]
        ingredients = request.form["ingredientsList"]
        prep_instructions = request.form["prepInstructions"]
        uploaded_file = request.files["imageFile"]

        if recipe_name != " " or ingredients != " " or prep_instructions != " " \
                or uploaded_file.filname != " ":
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))

            columns = ['Name', 'Ingredients', 'Prep', 'File']
            all_recipes = []
            recipe = {'Name': recipe_name, 'Ingredients': ingredients, 'Prep': prep_instructions, 'File': uploaded_file}
            all_recipes.append(recipe)
            write_to_csv(all_recipes, columns)
            print(all_recipes)

            return render_template('add_recipes.html', title='Add Recipes')
        else:
            return render_template('add_recipes.html', title='Add Recipes')

    else:
        return render_template('add_recipes.html', title='Add Recipes')


@app.route("/delete_recipe")
def delete_recipe():
    return render_template('delete_recipe.html', title='Delete Recipe')


def write_to_csv(all_recipes, columns):
    with open("recipes.csv", 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for key in all_recipes:
            writer.writerow(key)
    print("Writing to csv complete.")


def read_from_csv():
    recipes = []
    with open('recipes.csv') as datafile:
        data_reader = csv.DictReader(datafile)
        for row in data_reader:
            recipes.append(row)
    return recipes


if __name__ == '__main__':
    app.run(debug=True)
