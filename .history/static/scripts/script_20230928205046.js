const images = ["{% static 'burger-hero-image.jpg'%}",'burger-hero.jpg','burger-hero1'];
let currentIndex = 0;
const heroImage = document.getElementById('hero');

function changeImage() {
    heroImage.src = images[currentIndex];
    currentIndex = (currentIndex + 1) % images.length;
}

setInterval(changeImage, 3000);