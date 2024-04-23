function getScore() {
    $.ajax({
        url: '/get_score',
        type: 'GET',
        success: function(response) {
            $('#score').text(response.score);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching score:', error);
        }
    });
}

function updateScore() {
    $.ajax({
        url: '/update_score',
        type: 'POST',
        data: { correct_answer: true },
        success: function(response) {
            $('#score').text(response.score);
        },
        error: function(xhr, status, error) {
            console.error('Error updating score:', error);
        }
    });
}

$(document).ready(function() {

    getScore();

    // Option 1
    $("#option1").click(function() {
        if (1 === ans) {
            updateScore();
            $("#option1").animate({
                borderWidth: "10px",
                borderColor: "green"
            }, 500);
            $("#option1").css("border", "10px solid green");
            
        } else {
            $("#option1").animate({
                borderWidth: "10px",
                borderColor: "red"
            }, 500);
            $("#option1").css("border", "10px solid red");
        }
    });

    // Option 2
    $("#option2").click(function() {
        if (2 === ans) {
            updateScore();
            $(this).animate({
                borderWidth: "10px",
                borderColor: "green"
            }, 500);
            $("#option2").css("border", "10px solid green");
        } else {
            $(this).animate({
                borderWidth: "10px",
                borderColor: "red"
            }, 500);
            $("#option2").css("border", "10px solid red");
        }
    });
});
