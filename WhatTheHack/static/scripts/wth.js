$(function(){
  var wthTimeline = anime.timeline();
  wthTimeline
    .add({
    targets: '.logo-row .lines .wth-stroke',
    strokeDashoffset: [anime.setDashoffset, 0],
    easing: 'easeInOutSine',
    duration: 1500,
    delay: function(el, i) { return i * 200 },
    direction: 'alternate',
    loop: true
  })
  .add({
     targets: '.logo-row .lines .wth-fill',
    easing: 'easeInOutSine',
    duration: 500,
    opacity: [0, 1]
  })
  .add({
    targets: '.logo-row .SomeTxt' ,
    duration:500,
    easing: 'easeInOutQuad'
  });

  // Taken from CSS-Tricks
  // Select all links with hashes
  $('a[href*="#"]')
    // Remove links that don't actually link to anything
    .not('[href="#"]')
    .not('[href="#0"]')
    .click(function(event) {
      // On-page links
      if (
        location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
        && 
        location.hostname == this.hostname
      ) {
        // Figure out element to scroll to
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        // Does a scroll target exist?
        if (target.length) {
          // Only prevent default if animation is actually gonna happen
          event.preventDefault();
          $('html, body').animate({
            scrollTop: target.offset().top
          }, 500, function() {
            // Callback after animation
            // Must change focus!
            if($('.navbar-toggle').is(':visible')){
              $('.navbar-toggle').click(); // close the menu when selection has been made
            }
            var $target = $(target);
            $target.focus();
            if ($target.is(":focus")) { // Checking if the target was focused
              return false;
            } else {
              $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
              $target.focus(); // Set focus again
            };
          });
        }
      }
    });



}

)
