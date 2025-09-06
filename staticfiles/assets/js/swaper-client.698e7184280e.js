document.addEventListener("DOMContentLoaded", function () {
    new Swiper(".clients-slider", {
      loop: true,
      speed: 1000,
      autoplay: {
        delay: 2000,
        disableOnInteraction: false,
      },
      slidesPerView: 4,
      spaceBetween: 30,
      breakpoints: {
        320: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
        1024: {
          slidesPerView: 4,
          spaceBetween: 40,
        },
      },
    });
  });

