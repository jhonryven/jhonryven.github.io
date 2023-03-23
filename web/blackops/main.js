const menuglow = $("#menu-bar");
const navbar = $(".nav_menu");
const section = document.querySelector('.our-coffee_section');
const productimage = $("#product-image");
const ourcoffee = $('.coffee-contents li');

$(menuglow).click(() => {
    menuglow.toggleClass('fa-times');
    navbar.toggleClass('nav-toggle');
});

$(window).scroll(() => {
    menuglow.toggleClass("glow", $(window).scrollTop() !== 0);
    menuglow.removeClass("fa-times");
    navbar.removeClass('nav-toggle');
});

const contents = document.querySelectorAll('.coffee-contents li, #product-image, .about-contents h3, .about-contents p, .about-image, .menu, .specials,.contacts,.barista,.footer-contents');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        } else {
            entry.target.classList.remove("show");

        }
    });
},
    {
        rootMargin: "80px",
    }
);
contents.forEach(li => {
    observer.observe(li);
});


/* menus filter */
$(document).ready(() => {
    $(".menu_filter").click(function() {
      const filter = $(this).attr("data-filter");
      if (filter === "all") {
        $(".menu").show();
      } else {
        $(".menu").hide();
        $(`.menu[data-filter='${filter}']`).show();
      }
      $(".menu_filter").removeClass("active");
      $(this).addClass("active");
    });
  });