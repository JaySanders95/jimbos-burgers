setTimeout (function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

$(document).ready(function() {
    $("#toggleDarkMode").click(function() {
        $(".navbar, .footer, .background-standard ").toggleClass("dark-mode");
    });
});