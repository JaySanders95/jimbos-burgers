const images = ["{% static 'logo_image/burger-hero-image.jpg'%}","{% static 'burger-hero.jpg' %}","{% static 'burger-hero1'%}"];
let currentIndex = 0;
const heroImage = document.getElementById('hero');

function changeImage() {
    heroImage.src = images[currentIndex];
    currentIndex = (currentIndex + 1) % images.length;
}

setInterval(changeImage, 3000);


setTimeout (function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);