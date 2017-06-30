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
}

)
