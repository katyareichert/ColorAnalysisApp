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
        $( this )
            .addClass( "ui-state-highlight" )
            .find( "p" )
            .html( "Dropped!" );
        }
    });
} );