function getScore() {
    $.ajax({
        url: '/get_score',
        type: 'GET',
        success: function(response) {
            $('#score').text(response.score);
            $('#total').text(response.total);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching score:', error);
        }
    });
}

function updateScore(correct) {

    data = {
        "question_id": question_id,
        "correct": correct
    }

    $.ajax({
        url: '/update_score',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function(response) {
            $('#score').text(response.score);
            console.log(response.next_question_url);
            setTimeout(function() {
                window.location.href = response.next_question_url;
            }, 1200);
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
        let correct = 1 === ans;
        if (correct) {
            $(this).animate({
                borderWidth: "10px",
                borderColor: "green"
            }, 500);
            $(this).css("border", "10px solid green");
            
        } else {
            $(this).animate({
                borderWidth: "10px",
                borderColor: "red"
            }, 500);
            $(this).css("border", "10px solid red");
        }

        updateScore(correct);

    });

    // Option 2
    $("#option2").click(function() {
        let correct = 2 === ans;
        if (correct) {
            $(this).animate({
                borderWidth: "10px",
                borderColor: "green"
            }, 500);
            $(this).css("border", "10px solid green");
            
        } else {
            $(this).animate({
                borderWidth: "10px",
                borderColor: "red"
            }, 500);
            $(this).css("border", "10px solid red");
        }

        updateScore(correct);
    });
});
