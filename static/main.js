$(document).ready(function() {
    $('.recipe-card').click(function() {
      const title = $(this).find('.recipe-title').text();
      const time = $(this).find('.recipe-time').text();
      // Placeholder values — replace later with data-* attributes or AJAX
      const difficulty = "Easy";
      const cost = "$";
      const genre = "Breakfast";
  
      $('#modal-title').text(title);
      $('#modal-time').text(time);
      $('#modal-difficulty').text(difficulty);
      $('#modal-cost').text(cost);
      $('#modal-genre').text(genre);
  
      $('#recipeModal').fadeIn().css('display', 'flex');    });
  
    $('.close-btn').click(function() {
      $('#recipeModal').fadeOut();
    });
  
    $(window).click(function(e) {
      if ($(e.target).is('#recipeModal')) {
        $('#recipeModal').fadeOut();
      }
    });
  });
  