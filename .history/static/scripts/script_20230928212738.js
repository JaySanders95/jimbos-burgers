setTimeout (function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

$(document).ready(function() {
    $('#toggleDarkMode').click(function() {
        $('.footer').toggleClass('dark-mode');
        $('.bg-light').toggleClass('dark-mode');

    });
});