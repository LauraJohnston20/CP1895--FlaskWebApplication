# CP1895-FlaskWebApplication
Advanced Python Programming Course Project - Flask Web Application
## Description
This flask application was created as a requisite for CP1895 Advanced Python Programming. This application will allow users to view, add and, delete recipes based on the user preference. To add a recipe the user must enter the recipe name, ingredients list, preparation instructions, and a corresponding image. The image is validated by checking the file extension. To delete a recipe, the user must select their choice from the dropdown and confirm their choice by clicking the 'Confirm Recipe' button. The View Recipes page shows each recipe name and image. To view the ingredients and prep instructions, the user can click on the corresponding button. The home page lists all recipe images as thumbnails which can be clicked to open the image in a new tab. The user is also able to register and login, each located on separated pages, and logout of an account. To navigate between pages, the user can click the desired link in the navigation bar located on each page. 
## Summary of Files
* **static folder**: contains all asset files to be used by the templates, including main.css (main styling sheet), images folder (recipe images), and js folder (jquery file, jquery-3.6.0-min.js and recipe validation file, validateRecipe.js).
* **templates folder**: contains .html files that are to be rendered in the browser. These files have both static data and placeholders for dynamic data.
* **app.py**: main python file that imports the Flask module to create the web application.
* **recipes.csv** csv file in which the recipe information is stored.
* **recipes.db** database file in which usernames and password are stored for login/registration.
# Download & Installation
## Step 1:
* Download the files located in the git repo https://github.com/LauraJohnston20/CP1895-FlaskWebApplication or [click here](https://github.com/LauraJohnston20/CP1895-FlaskWebApplication/archive/refs/heads/main.zip).
* Unzip the downloaded folder and add all files to your Python project.
## Step 2:
Navigate to the terminal in your Python project, or to the Command Prompt, and run the following command in your virtual environment to install Flask web framework:
```python
pip install flask
```
## Step 3:
To start the Flask application, run the following commands in the terminal, or Command Prompt:
```python
set FLASK_APP=app.py
flask run
```
Now the application is ready to be used.
# Using the Application
## Register
An account is not required to use the application, but if the user wishes to create an account they can navigate to the register page in the upper right hand corner of the webpage. 
### Step 1:
Click register
![image](https://user-images.githubusercontent.com/95102375/163734480-00907713-80fb-4746-b212-57f30d455c58.png)
### Step 2:
Fill out the register form and click Register

![image](https://user-images.githubusercontent.com/95102375/163735214-6a9d5115-7a50-472e-a7d5-7aff8e730add.png)
### Step 3: 
After registration is completed, you will be automatically redirected to the login page. Fill out the login form and click Login

![image](https://user-images.githubusercontent.com/95102375/163735178-d4263170-920f-40b2-8af2-d66e2f2e94a9.png)
## Add a Recipe
### Step 1:
Click the Add Recipes link in the navigation bar
![image](https://user-images.githubusercontent.com/95102375/163734684-5c586c5c-da75-4e41-ba67-ee8a4017e88d.png)
### Step 2:
Fill out the recipe form by entering the recipe name, ingredients list, preparation instructions, and recipe image. The recipe must have file extension .jpeg, .jpg, or .png.
![image](https://user-images.githubusercontent.com/95102375/163735225-f2b590f8-d92f-414e-9dc0-bbbb7f20e628.png)
### Step 3:
Click the 'Submit Recipe' button to add the recipe.
![image](https://user-images.githubusercontent.com/95102375/163734895-3ade9c79-5da1-4475-822b-e853afd25721.png)
## View Recipes
### Step 1:
Click the View Recipes link in the navigation bar
![image](https://user-images.githubusercontent.com/95102375/163734971-b688310f-e3fb-4642-a70e-4fb27ad64fce.png)
### Step 2:
All added recipes will be available on the View Recipes page. To view a specific recipes ingredients or prep instructions, click on the corresponding button for that recipe.

![image](https://user-images.githubusercontent.com/95102375/163735243-61b81a5f-63d2-4491-b6f3-c9ce133bf0c8.png)
## View Recipes
### Step 1:
Click the View Recipes link in the navigation bar
![image](https://user-images.githubusercontent.com/95102375/163735055-a2c2964e-60c4-49dc-913b-3befe6ebb888.png)
### Step 2:
Select the recipe to delete from the dropdown list

![image](https://user-images.githubusercontent.com/95102375/163735134-d25ef7d1-da18-431b-970c-0fb0392dd479.png)
### Step 3:
Confirm the recipe to be deleted by clicking 'Confirm Recipe'

![image](https://user-images.githubusercontent.com/95102375/163735116-1de05cf8-b513-4ae6-9a1a-fabd2f3fcf51.png)



