"use strict";

$(document).ready( () => {

     $("#recipeName").focus();

    $("#submitRecipe").click( evt => {
        let isValid = true;

        // validate recipe name
        const recipeNamePattern = /^[A-Za-z ]+$/;
        const recipeName = $("#recipeName").val().trim();
        if (recipeName == "") {
            alert("Recipe name is required.")
            isValid = false;
        } else if ( !recipeNamePattern.test(recipeName) ) {
            alert("Recipe name can only contain alphabetic characters.")
            isValid = false;
        }
        $("#recipeName").val(recipeName);
        console.log(recipeName);

        // validate ingredients list
        const ingredientsList = $("#ingredientsList").val().trim();
        if (ingredientsList == "") {
            alert("Ingredients list is required.")
            isValid = false;
        }
        $("#ingredientsList").val(ingredientsList);
        console.log(ingredientsList);

        // validate prep instructions
        const prepInstructions = $("#prepInstructions").val().trim();
        if (prepInstructions == "") {
            alert("Prep instructions are required.")
            isValid = false;
        }
        $("#prepInstructions").val(prepInstructions);

        // validate file extension
        let file_extension = $("#imageFile").val().split('.').pop().toLowerCase();
        if ($.inArray(file_extension, ["png","jpg","jpeg"]) == -1) {
            alert("Invalid file extension. Must be .png, .jpg, .jpeg.");
            isValid = false;
        }

        if (isValid === false) {
            evt.preventDefault();
        } else if (isValid === true) {
            alert("Recipe successfully added!")
        }
    });
});