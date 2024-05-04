$(document).ready(function() {
    $(".order-container").sortable({
      axis: "x",
      containment: "parent",
      tolerance: "pointer"
    });

    $(".reorder_block").mousedown(function() {
      $("#tip").text('drag to reorder');
      $("#tip").removeClass("purple");
    });

    $("#back").click(function() {
      window.location.href = prev_lesson;
    });

    $('#next').on('click', function() {
      var sortedIds = $('.color_block').map(function() {
          return this.id;
      }).get();
  
      var correctOrder = true;
      for (var i = 0; i < sortedIds.length; i++) {
          if (sortedIds[i] !== 'a' + i) {
              correctOrder = false;
              break;
          }
      }
  
      if (correctOrder) {
          window.location.href = next_lesson;
      } else {
          $("#tip").text('try again!');
          $("#tip").addClass("purple");
      }
  });
  
  }); 