$(document).ready(function() {
    // Attach click event handler to the images
    $("#option1").click(function() {
        if (1 === ans) {
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

    $("#option2").click(function() {
        if (2 === ans) {
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
