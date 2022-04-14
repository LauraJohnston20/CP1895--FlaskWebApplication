from flask import Flask, render_template, url_for, request
import csv
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'

@app.route("/")
@app.route("/home")
def home():
    recipe_images = os.listdir(os.path.join(app.static_folder, "images"))
    print(recipe_images)
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

        if recipe_name != "" or ingredients != "" or prep_instructions != "" \
                or uploaded_file.filename != "":
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
            columns = ['Name', 'Ingredients', 'Prep', 'File']
            all_recipes = read_from_csv()
            recipe = {'Name': recipe_name, 'Ingredients': ingredients, 'Prep': prep_instructions,
                      'File': uploaded_file.filename}
            all_recipes.append(recipe)
            write_to_csv(all_recipes, columns)
            print(all_recipes)

            return render_template('add_recipes.html', title='Add Recipes')
        else:
            return render_template('add_recipes.html', title='Add Recipes')

    else:
        return render_template('add_recipes.html', title='Add Recipes')


@app.route("/delete_recipe", methods=["POST", "GET"])
def delete_recipe():
    recipe_list = read_from_csv()
    columns = ['Name', 'Ingredients', 'Prep', 'File']
    print(recipe_list)
    if request.method == "POST":
        recipe_name = request.form['delete_select']
        for i in range(len(recipe_list)):
            if recipe_list[i]['Name'] == recipe_name:
                image = recipe_list[i]['File']
                path = 'static/images'
                file = os.path.join(path, image)
                os.remove(file)
                del recipe_list[i]
                break
        write_to_csv(recipe_list, columns)
        print(recipe_list)
    else:
        return render_template('delete_recipe.html', recipe_list=recipe_list)
    return render_template('delete_recipe.html', recipe_list=recipe_list)


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template('login.html')


def write_to_csv(all_recipes, columns):
    with open("recipes.csv", 'w', newline='') as csvfile:
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
