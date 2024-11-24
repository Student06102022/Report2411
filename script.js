let currentSlide = 0;
const slides = document.querySelectorAll('.slides img');
const caption = document.getElementById('caption');

function showSlide(index) {
    if (index >= slides.length) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = slides.length - 1;
    } else {
        currentSlide = index;
    }
    updateSlider();
}

function updateSlider() {
    const offset = -currentSlide * 100;
    document.querySelector('.slides').style.transform = `translateX(${offset}%)`;
    caption.innerText = `Изображение ${currentSlide + 1} из ${slides.length}`;
}

function changeSlide(direction) {
    showSlide(currentSlide + direction);
}

// Инициализация
updateSlider();