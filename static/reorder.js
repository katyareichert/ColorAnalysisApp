$(document).ready(function() {
    $(".order-container").sortable({
      axis: "x",
      containment: "parent",
      tolerance: "pointer"
    });
  });