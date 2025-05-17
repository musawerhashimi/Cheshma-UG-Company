document.addEventListener("DOMContentLoaded", function () {
  new Swiper(".news-slider", {
    loop: true, // Enables infinite looping
    speed: 800, // Transition speed
    autoplay: {
      delay: 3000, // Delay between slides
      disableOnInteraction: false, // Continue autoplay after interaction
    },
    slidesPerView: 1, // Default: Show 1 slide at a time
    spaceBetween: 20, // Space between slides
    pagination: {
      el: ".swiper-pagination",
      clickable: true, // Enable pagination bullets
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      768: {
        slidesPerView: 2, // Show 2 slides on medium screens (≥768px)
        spaceBetween: 30,
      },
      1024: {
        slidesPerView: 3, // Show 3 slides on large screens (≥1024px)
        spaceBetween: 40,
      },
    },
  });
});