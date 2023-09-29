const images = ["{% static 'burger-hero-image.jpg'%}","{% static 'burger-hero.jpg' %}","{% static 'burger-hero1'%}"];
let currentIndex = 0;
const heroImage = document.getElementById('hero-container');

function changeImage() {
    heroImage.src = images[currentIndex];
    currentIndex = (currentIndex + 1) % images.length;
}

setInterval(changeImage, 3000);