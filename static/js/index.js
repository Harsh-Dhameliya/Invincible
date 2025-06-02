function change_image(src) {
  let stat = document.querySelector(".states");
  if (src == "saputara") {
    stat.style.backgroundImage = "url('../static/images/gj-vav.jpg')";
  } else if (src == "goa") {
    stat.style.backgroundImage = "url('../static/images/goa-2.jpg')";
  } else if (src == "manali") {
    stat.style.backgroundImage = "url('../static/images/uttrakhand-1.jpg')";
  } else if (src == "rajasthan") {
    stat.style.backgroundImage =
      "url('../static/images/rajasthan-thar-desert.jpg')";
  } else {
    stat.style.backgroundImage = "url('../static/images/jammu-1.jpg')";
  }
}


function handleToast() {
  // console.log("haaaaa");
  
    const toast = document.getElementById("toast")
    toast.classList.remove("d-block")
    toast.classList.add("d-none")
}

// $(document).ready(function () {
//   $(".owl-carousel").owlCarousel({
//     center: true,
//     loop: true,
//     items: 3,
//     // margin:10,
//     nav: false,
//     dots: false,
//     autoplay: true,
//     autoplayHoverPause: false,
//     smartSpeed: 1500,
//     startPosition: "0",
//   });
// });

// const sliderTrack = document.querySelector(".slider-track");
// const slides = document.querySelectorAll(".slide");
// const slideCount = slides.length - 1; // Exclude the cloned slide
// const slideWidth = slides[0].clientWidth;

// let currentIndex = 0;

// const moveToNextSlide = () => {
//   currentIndex++;
//   sliderTrack.style.transform = `translateX(-${currentIndex * slideWidth}px)`;

//   if (currentIndex === slideCount + (slideCount - 4)) {
//     // Reset to the first slide without transition
//     setTimeout(() => {
//       sliderTrack.style.transition = "none";
//       currentIndex = 0;
//       sliderTrack.style.transform = `translateX(0)`;
//     }, 500); // Match the transition duration
//   } else {
//     // Ensure smooth transition
//     sliderTrack.style.transition = "transform 0.5s ease-in-out";
//   }
// };

// setInterval(moveToNextSlide, 3000);

// function reviewslide()
// {
//   const sliderTrack = document.querySelector(".slider-track");
//   const slides = document.querySelectorAll(".slide");
//   const slideCount = slides.length - 1; // Exclude the cloned slide
//   const slideWidth = slides[0].clientWidth;
//   // console.log(slideWidth);

//   for(i=1;i<=slideCount;i++)
//     {
//       sliderTrack.style.transform = `translateX(-${i * slideWidth}px)`;

//     }
//     setTimeout("reviewslide",3000)

// }/*

// setInterval(reviewslide, 3000);

// var menu = document.querySelector(".menu-add i")
// var full = document.querySelector(".inner-menu")
// var close = document.querySelector(".inner-menu i")
// // var a = document.querySelector("#full ")
// var tl = gsap.timeline()

// tl.to(full, {
//     right:0,
//     duration:0.3

// });

// tl.from("#full a",{
//     x:500,
//     stagger:0.06
// })

// tl.pause()

// menu.addEventListener('click',function (){
//     // console.log("click");

//     tl.play()

// })
// close.addEventListener('click',function (){
//     // console.log("click");

//     tl.reverse()

// })
