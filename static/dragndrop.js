$( function() {
    $(".draggable").draggable({
        classes: {
            "ui-droppable-hover": "trash-hover"
        },
        revert: function(valid) {
            if (!valid) {
                return true;
            }
        }
    });
    $( ".drop-target" ).droppable({
        drop: function( event, ui ) {
            var kids = $(this).children().length;
            if (kids == 0) {
                $(this).text('');
            }

            ui.draggable.appendTo($(this)).css({left: 10, top: 5 });
        }
    });
    $("#next").click(function() {
        var allDroppable1OnTarget1 = $(".draggable1").length == $(".drop-target1 .draggable1").length;
        var allDroppable2OnTarget2 = $(".draggable2").length == $(".drop-target2 .draggable2").length;

        if (allDroppable1OnTarget1 && allDroppable2OnTarget2) {
            $("#dnd_container").text('');
            $(".draggable1").each(function() {
                // Remove decor
                $(this).css("border", "none");
                $(this).text('');

                // Animate
                var centerX = ($(window).width() - $(this).outerWidth()) / 3;
                $(this).animate({
                    left: centerX - 126,
                    top: -30
                }, 1000);
            });

            $(".draggable2").each(function() {
                // Remove decor
                $(this).css("border", "none");
                $(this).text('');

                // Animate
                var centerX = ($(window).width() - $(this).outerWidth()) / 3;
                $(this).animate({
                    left: -centerX + 135,
                    top: -30
                }, 1000);
            });

        } else {
            $(".draggable1").each(function() {
                if (!$(this).parent().hasClass("drop-target1")) {
                    $(this).css("border", "2px solid black");
                    $(this).text(':(');
                } else {
                    $(this).css("border", "none");
                    $(this).text('');
                }
            });

            $(".draggable2").each(function() {
                if (!$(this).parent().hasClass("drop-target2")) {
                    $(this).css("border", "2px solid black");
                    $(this).text(':(');
                } else {
                    $(this).css("border", "none");
                    $(this).text('');
                }
            });
        }
    });
} );
