$('.programs-list').slick({
  dots:true,
  speed: 300,
  slidesToShow: 3,
  slidesToScroll:1,
  prevArrow: '.prev-arrow',
  nextArrow: '.next-arrow',
});

$('.slider_container').slick({
  autoplay:true,
  dots:true,
  speed: 300,
  slidesToShow: 1,
  slidesToScroll:1,
  prevArrow: '.prev-arrow_stories',
  nextArrow: '.next-arrow_stories',
});


const btnFilter = document.querySelector('.btnfilter');
const filterContainer = document.querySelector('.filter-selection');
const coursesSection = document.querySelector('.courses_container');
const course = document.querySelector('.course');

course.onclick= function (){
  filterContainer.classList.remove('active');
}

coursesSection.onmouseover = function(){
  btnFilter.classList.remove('filterbtn-active');
  filterContainer.classList.remove('active');
}

btnFilter.onclick = function(){
  btnFilter.classList.toggle('filterbtn-active');
  filterContainer.classList.toggle('active');
}

filterContainer.onmouseleave = function() {
  btnFilter.classList.remove('filterbtn-active');
  filterContainer.classList.remove('active');
}

$(document).ready(() => {
  
  $(".course").click(function() {
    const filter = $(this).attr("data-filter");
    if (filter === "All Courses") {
      $(".course-name ").html(`${filter}`).show();
      $(".courses").show();
    } else {
      $(".course-name").html(`${filter}`).show();
      $(".courses").hide();
      $(`.courses[data-filter='${filter}']`).show();
    }
    $(".courses").removeClass("active");
    $(this).addClass("active");
  });
});
