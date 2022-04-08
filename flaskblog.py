from flask import Flask, render_template, url_for
import csv

app = Flask(__name__)


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
    return render_template('view_recipes.html', title='View Recipes')


@app.route("/add_recipes")
def add_recipes():
    return render_template('add_recipes.html', title='Add Recipes')


@app.route("/delete_recipe")
def delete_recipe():
    return render_template('delete_recipe.html', title='Delete Recipe')


if __name__ == '__main__':
    app.run(debug=True)
