AOS.init({
	duration: 800,
	easing: 'slide'
});

(function($) {
	"use strict";

	// Stellar for parallax
	$(window).stellar({
	    responsive: true,
	    parallaxBackgrounds: true,
	    parallaxElements: true,
	    horizontalScrolling: false,
	    hideDistantElements: false,
	    scrollProperty: 'scroll'
	});

	// Full height sections
	var fullHeight = function() {
		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});
	};
	fullHeight();

	// Loader
	var loader = function() {
		setTimeout(function() { 
			if($('#ftco-loader').length > 0) {
				$('#ftco-loader').removeClass('show');
			}
		}, 1);
	};
	loader();

	// Scrollax
	$.Scrollax();

	// Burger menu toggle
	var burgerMenu = function() {
		$('body').on('click', '.js-fh5co-nav-toggle', function(event){
			event.preventDefault();
			$(this).toggleClass('active');
		});
	};
	burgerMenu();

	// One-page navigation
	var onePageClick = function() {
		$(document).on('click', '#ftco-nav a[href^="#"]', function(event) {
			event.preventDefault();
			var href = $.attr(this, 'href');
			$('html, body').animate({
				scrollTop: $($.attr(this, 'href')).offset().top - 70
			}, 500);
		});
	};
	onePageClick();

	// Carousel
	var carousel = function() {
		$('.home-slider').owlCarousel({
			loop: true,
			autoplay: true,
			margin: 0,
			animateOut: 'fadeOut',
			animateIn: 'fadeIn',
			nav: false,
			items: 1,
			responsive:{
				0:{ items:1 },
				600:{ items:1 },
				1000:{ items:1 }
			}
		});
	};
	carousel();

	// Dropdown hover effect
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

	// Scroll window effects
	var scrollWindow = function() {
		$(window).scroll(function(){
			var st = $(this).scrollTop(),
				navbar = $('.ftco_navbar'),
				sd = $('.js-scroll-wrap');

			if(st > 150) navbar.addClass('scrolled'); else navbar.removeClass('scrolled sleep');
			if(st > 350) {
				navbar.addClass('awake');
				if(sd.length > 0) sd.addClass('sleep');
			} else {
				navbar.removeClass('awake').addClass('sleep');
				if(sd.length > 0) sd.removeClass('sleep');
			}
		});
	};
	scrollWindow();

	// Counter animation
	var counter = function() {
		$('#section-counter, .hero-wrap, .ftco-counter, .ftco-about').waypoint(function(direction){
			if(direction === 'down' && !$(this.element).hasClass('ftco-animated')) {
				var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',');
				$('.number').each(function(){
					var $this = $(this);
					var num = $this.data('number');
					$this.animateNumber({ number: num, numberStep: comma_separator_number_step }, 7000);
				});
			}
		}, { offset: '95%' });
	};
	counter();

	// Content animation on scroll
	var contentWayPoint = function() {
		var i = 0;
		$('.ftco-animate').waypoint(function(direction){
			if(direction === 'down' && !$(this.element).hasClass('ftco-animated')) {
				i++;
				$(this.element).addClass('item-animate');
				setTimeout(function(){
					$('body .ftco-animate.item-animate').each(function(k){
						var el = $(this);
						setTimeout(function(){
							var effect = el.data('animate-effect');
							if(effect === 'fadeIn') el.addClass('fadeIn ftco-animated');
							else if(effect === 'fadeInLeft') el.addClass('fadeInLeft ftco-animated');
							else if(effect === 'fadeInRight') el.addClass('fadeInRight ftco-animated');
							else el.addClass('fadeInUp ftco-animated');
							el.removeClass('item-animate');
						}, k * 50, 'easeInOutExpo');
					});
				}, 100);
			}
		}, { offset: '95%' });
	};
	contentWayPoint();

	// Magnific popup
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


// DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
	const tabButtons = document.querySelectorAll(".tab-btn");
	const tabContents = document.querySelectorAll(".tab-content");
	const cards = document.querySelectorAll(".profile-card");

	// Tab switching
	tabButtons.forEach(btn => {
		btn.addEventListener("click", () => {
			tabButtons.forEach(b => b.classList.remove("active"));
			btn.classList.add("active");
			const target = btn.dataset.target;
			tabContents.forEach(tc => tc.classList.remove("active"));
			document.getElementById(target).classList.add("active");

			// Log visitor for family/friends tabs
			if(target === "family" || target === "friends") {
				logVisitor(target);
			}
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

	// Log homepage visit
	logVisitor("homepage", "visit");
});


// Log visitor to Render backend
function logVisitor(section = "", action = "tab_open") {
	fetch("https://portfolio-backend-da4l.onrender.com/log-visitor", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ section: section, action: action, success: true })
	})
	.then(res => res.json())
	.then(data => console.log("Visitor logged:", data))
	.catch(err => console.error("Error logging visitor:", err));
}
