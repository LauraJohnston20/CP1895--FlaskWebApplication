# CP1895-FlaskWebApplication
Advanced Python Programming Course Project - Flask Web Application
## Description
This flask application was created as a requisite for CP1895 Advanced Python Programming. This application will allow users to view, add and, delete recipes based on the user preference. To add a recipe the user must enter the recipe name, ingredients list, preparation instructions, and a corresponding image. The image is validated by checking the file extension. To delete a recipe, the user must select their choice from the dropdown and confirm their choice by clicking the 'Confirm Recipe' button. The View Recipes page shows each recipe name and image. To view the ingredients and prep instructions, the user can click on the corresponding button. The home page lists all recipe images as thumbnails which can be clicked to open the image in a new tab. The user is also able to register and login, each located on separated pages, and logout of an account. To navigate between pages, the user can click the desired link in the navigation bar located on each page. 
# Download & Installation
## Step 1:
* Download the files located in the git repo https://github.com/LauraJohnston20/CP1895-FlaskWebApplication or [click here](https://github.com/LauraJohnston20/CP1895-FlaskWebApplication/archive/refs/heads/main.zip).
* Unzip the downloaded folder and add all files to your Python project.
## Step 2:
Navigate to the terminal in your Python project, or to the Command Prompt, and run the following command in your virtual environment to install Flask web framework:
```python
pip install flask
```
Note: If you have not created a virtual environment within your project, follow the steps for creating and activating an environment, found here:
https://flask.palletsprojects.com/en/2.1.x/installation/.
## Step 3:
To start the Flask application, run the following commands in the terminal, or Command Prompt:
```python
Flask_APP="application"
Flask_ENV="development"
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

![image](https://user-images.githubusercontent.com/95102375/163734744-e88e6a0d-3b6f-4825-83a0-ca81bbcbb2f8.png)
### Step 3: 
After registration is completed, you will be automatically redirected to the login page. Fill out the login form and click Login

![image](https://user-images.githubusercontent.com/95102375/163734729-49e3d34b-8b98-4d85-bf07-0f3493d254b7.png)
## Add a Recipe
### Step 1:
Click the Add Recipes link in the navigation bar
![image](https://user-images.githubusercontent.com/95102375/163734684-5c586c5c-da75-4e41-ba67-ee8a4017e88d.png)
### Step 2:
Fill out the recipe form by entering the recipe name, ingredients list, preparation instructions, and recipe image. The recipe must have file extension .jpeg, .jpg, or .png.
![image](https://user-images.githubusercontent.com/95102375/163734913-93f6b923-ae06-43a8-a22b-7b3c9e86b41a.png)
### Step 3:
Click the 'Submit Recipe' button to add the recipe.
![image](https://user-images.githubusercontent.com/95102375/163734895-3ade9c79-5da1-4475-822b-e853afd25721.png)


