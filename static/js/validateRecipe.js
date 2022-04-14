"use strict";

$(document).ready( () => {

     $("#recipeName").focus();

     // validate image file
    function fileValidation() {
            var fileInput =
                document.getElementById('imageFile');

            var filePath = fileInput.value;

            // Allowing file type
            var allowedExtensions = /(\.jpeg|\.jpg|\.png)$/i;

            if (!allowedExtensions.exec(filePath)) {
                alert('Invalid file type');
                fileInput.value = '';
                return isValid = false;
            }
        }

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

        if (isValid === false) {
            evt.preventDefault();
        } else if (isValid === true) {
            alert("Recipe successfully added!")
        }
    });
});