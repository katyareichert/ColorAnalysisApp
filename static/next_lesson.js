$(document).ready(function() {
    $("#next").click(function() {
        window.location.href = next_lesson;
    });
    
    $("#back").click(function() {
        window.location.href = prev_lesson;
    });
});