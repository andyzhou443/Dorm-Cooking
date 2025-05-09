$(document).ready(function() {
  // When a recipe card is clicked, go directly to the recipe page
  $('.recipe-card').click(function() {
    const recipeId = $(this).data('recipe-id');
    if (recipeId) {
      window.location.href = `/recipes/${recipeId}`;
    }
  });
});
