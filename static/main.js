$(document).ready(function() {
  let selectedRecipeId = null;

  // When a recipe card is clicked
  $('.recipe-card').click(function() {
    selectedRecipeId = $(this).data('recipe-id');
    const r = window.recipes[selectedRecipeId];

    // Populate modal content with the selected recipe
    $('#modal-title').text(r.name);
    $('#modal-time').text(r.time);
    $('#modal-difficulty').text(r.difficulty);
    $('#modal-cost').text(r.cost);
    $('#modal-genre').text(r.genre);

    // Show the modal
    $('#recipeModal').fadeIn().css('display', 'flex');
  });

  // Close the modal when the close button is clicked
  $('.close-btn').click(() => $('#recipeModal').fadeOut());

  // Close the modal if the user clicks outside the modal content
  $(window).click(e => {
    if ($(e.target).is('#recipeModal')) $('#recipeModal').fadeOut();
  });

  // Redirect to the recipe page when the "Begin" button is clicked
  $('#begin-button').click(() => {
    if (selectedRecipeId) {
      // Make sure the URL is wrapped in backticks for template literals
      window.location.href = `/recipes/${selectedRecipeId}`;
    }
  });
});
