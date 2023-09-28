setTimeout (function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);


function checkDate() {
    var selectedDate = new Date(document.getElementById('id_time').value);
    var now = new Date();

    if (selectedDate < now) {
    alert("Date must be in the future");
    window.location.reload();
    }
