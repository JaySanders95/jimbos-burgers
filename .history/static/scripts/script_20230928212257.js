setTimeout (function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

$(document).ready(function() {
    $('#darkModeToggle').click(function() {
        $('body').toggleClass('dark-mode');
        $('.navbar').toggleClass('dark-mode');
        $('.footer').toggleClass('dark-mode');
    });
});