$(document).ready(function() {
    $("#next").click(function() {
        var currentUrl = window.location.href;
        
        // Split the URL by '/'
        var urlParts = currentUrl.split('/');
        
        // Get the last part of the URL which is the number
        var pageNumber = parseInt(urlParts[urlParts.length - 1]);
        
        // Increment the page number
        var nextPageNumber = pageNumber + 1;
        
        // Modify the URL by replacing the last part with the new page number
        urlParts[urlParts.length - 1] = nextPageNumber.toString();
        
        // Join the URL parts back together
        var newUrl = urlParts.join('/');
        
        // Redirect to the new URL
        window.location.href = newUrl;
    });
});