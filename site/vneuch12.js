let currentIndex = 0;
const visibleItems = 3;
const items = document.querySelectorAll('.carousel-item');
const totalItems = items.length;

document.querySelector('.next-btn').addEventListener('click', () => {
    if ((currentIndex + visibleItems) > totalItems || currentIndex == totalItems - visibleItems){
        currentIndex = 0
    }
    else if ((currentIndex + visibleItems) + visibleItems > totalItems){
        currentIndex = totalItems - visibleItems 
    }
    else{
        currentIndex = (currentIndex + visibleItems) % totalItems;
    }
    updateCarousel();
});

document.querySelector('.prev-btn').addEventListener('click', () => {
    currentIndex = (currentIndex - visibleItems + totalItems) % totalItems;
    updateCarousel();
});

function updateCarousel() {
    const carouselInner = document.querySelector('.carousel-inner');
    const offset = -currentIndex * (100 / visibleItems);
    carouselInner.style.transform = `translateX(${offset}%)`;
}
