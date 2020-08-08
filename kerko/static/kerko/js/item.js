jQuery(function($) {
  var hash = document.location.hash;
  if (hash) {
    $('.nav-tabs .nav-item a[href="' + hash + '"]').tab('show');
  }

  $('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
    window.location.hash = e.target.hash;
  });
});
