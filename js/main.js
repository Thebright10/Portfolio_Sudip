AOS.init({
  duration: 800,
  easing: 'slide'
});

(function($) {

  "use strict";

  $(window).stellar({
    responsive: true,
    parallaxBackgrounds: true,
    parallaxElements: true,
    horizontalScrolling: false,
    hideDistantElements: false,
    scrollProperty: 'scroll'
  });

  var fullHeight = function() {
    $('.js-fullheight').css('height', $(window).height());
    $(window).resize(function(){
      $('.js-fullheight').css('height', $(window).height());
    });
  };
  fullHeight();

  var loader = function() {
    setTimeout(function() { 
      if($('#ftco-loader').length > 0) {
        $('#ftco-loader').removeClass('show');
      }
    }, 1);
  };
  loader();

  $.Scrollax();

  var burgerMenu = function() {
    $('body').on('click', '.js-fh5co-nav-toggle', function(event){
      event.preventDefault();
      if ($('#ftco-nav').is(':visible')) {
        $(this).removeClass('active');
      } else {
        $(this).addClass('active');  
      }
    });
  };
  burgerMenu();

  var onePageClick = function() {
    $(document).on('click', '#ftco-nav a[href^="#"]', function (event) {
      event.preventDefault();
      var href = $.attr(this, 'href');
      $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top - 70
      }, 500);
    });
  };
  onePageClick();

  var carousel = function() {
    $('.home-slider').owlCarousel({
      loop:true,
      autoplay: true,
      margin:0,
      animateOut: 'fadeOut',
      animateIn: 'fadeIn',
      nav:false,
      autoplayHoverPause: false,
      items: 1
    });
  };
  carousel();

  $('nav .dropdown').hover(function(){
    var $this = $(this);
    $this.addClass('show');
    $this.find('> a').attr('aria-expanded', true);
    $this.find('.dropdown-menu').addClass('show');
  }, function(){
    var $this = $(this);
    $this.removeClass('show');
    $this.find('> a').attr('aria-expanded', false);
    $this.find('.dropdown-menu').removeClass('show');
  });

  $('#dropdown04').on('show.bs.dropdown', function () { console.log('show'); });

  var scrollWindow = function() {
    $(window).scroll(function(){
      var $w = $(this),
          st = $w.scrollTop(),
          navbar = $('.ftco_navbar'),
          sd = $('.js-scroll-wrap');

      if (st > 150) {
        if (!navbar.hasClass('scrolled')) navbar.addClass('scrolled');  
      } else {
        if (navbar.hasClass('scrolled')) navbar.removeClass('scrolled sleep');
      }

      if (st > 350) {
        if (!navbar.hasClass('awake')) navbar.addClass('awake');  
        if(sd.length > 0) sd.addClass('sleep');
      } else {
        if (navbar.hasClass('awake')) {
          navbar.removeClass('awake');
          navbar.addClass('sleep');
        }
        if(sd.length > 0) sd.removeClass('sleep');
      }
    });
  };
  scrollWindow();

  var counter = function() {
    $('#section-counter, .hero-wrap, .ftco-counter, .ftco-about').waypoint(function(direction){
      if(direction === 'down' && !$(this.element).hasClass('ftco-animated')) {
        var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',');
        $('.number').each(function(){
          var $this = $(this),
              num = $this.data('number');
          $this.animateNumber({number: num, numberStep: comma_separator_number_step}, 7000);
        });
      }
    }, { offset: '95%' });
  };
  counter();

  var contentWayPoint = function() {
    var i = 0;
    $('.ftco-animate').waypoint(function(direction){
      if(direction === 'down' && !$(this.element).hasClass('ftco-animated')) {
        i++;
        $(this.element).addClass('item-animate');
        setTimeout(function(){
          $('body .ftco-animate.item-animate').each(function(k){
            var el = $(this);
            setTimeout(function() {
              var effect = el.data('animate-effect');
              if (effect === 'fadeIn') el.addClass('fadeIn ftco-animated');
              else if (effect === 'fadeInLeft') el.addClass('fadeInLeft ftco-animated');
              else if (effect === 'fadeInRight') el.addClass('fadeInRight ftco-animated');
              else el.addClass('fadeInUp ftco-animated');
              el.removeClass('item-animate');
            }, k * 50);
          });
        }, 100);
      }
    }, { offset: '95%' });
  };
  contentWayPoint();

  $('.image-popup').magnificPopup({
    type: 'image',
    closeOnContentClick: true,
    closeBtnInside: false,
    fixedContentPos: true,
    mainClass: 'mfp-no-margins mfp-with-zoom',
    gallery: { enabled: true, navigateByImgClick: true, preload: [0,1] },
    image: { verticalFit: true },
    zoom: { enabled: true, duration: 300 }
  });

  $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
    disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,
    fixedContentPos: false
  });

})(jQuery);

document.addEventListener("DOMContentLoaded", () => {
  const tabButtons = document.querySelectorAll(".tab-btn");
  const tabContents = document.querySelectorAll(".tab-content");
  const cards = document.querySelectorAll(".profile-card");

  // Tab switching
  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      tabButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      let target = btn.getAttribute("data-target");
      tabContents.forEach(tc => {
        tc.classList.remove("active");
        if (tc.id === target) tc.classList.add("active");
      });
    });
  });

  // Card glow on click
  cards.forEach(card => {
    card.addEventListener("click", () => {
      cards.forEach(c => c.classList.remove("active"));
      card.classList.add("active");
    });
  });

  // Cursor glow effect
  const glowCursor = document.createElement("div");
  glowCursor.style.position = "fixed";
  glowCursor.style.width = "25px";
  glowCursor.style.height = "25px";
  glowCursor.style.borderRadius = "50%";
  glowCursor.style.pointerEvents = "none";
  glowCursor.style.background = "rgba(255, 255, 0, 0.6)";
  glowCursor.style.boxShadow = "0 0 20px rgba(255, 255, 0, 0.8)";
  glowCursor.style.zIndex = "9999";
  document.body.appendChild(glowCursor);

  document.addEventListener("mousemove", e => {
    glowCursor.style.left = e.pageX - 12 + "px";
    glowCursor.style.top = e.pageY - 12 + "px";
  });

  // Visitor logging
  function logVisitor() {
  fetch("https://portfolio-backend.onrender.com/log-visitor", {
    method: "POST"
  })
  .then(res => res.json())
  .then(data => console.log("Visitor logged:", data))
  .catch(err => console.error("Error logging visitor:", err));
}


  function unlockTab(tabName) {
  // Hide all tabs
  document.querySelectorAll(".tab-content").forEach(tab => tab.style.display = "none");

  // Show selected tab
  document.getElementById(tabName).style.display = "block";

  // Log visitor only for Family or Friends tabs
  if(tabName === "family" || tabName === "friends") {
    logVisitor();
  }
}


  // Example: Automatically unlock a tab (optional)
  // unlockTab("family");
});
