$(document).ready(function(){
    var $fmToggle = $('#fm-toggle');
    $fmToggle.on('click', function(){
        $(this).toggleClass('collapsed');
        $(this).find('.glyphicon').toggleClass('glyphicon-menu-up');
        setTimeout(function() {
            $('#following-matches').collapse('toggle');
            $('#time-clarification').collapse('toggle');
        }, 100);
    });
    if ($fmToggle.data('is-toggled') == '1') {
        $fmToggle.trigger('click');
    }
});

// JS replace replaces only until the first occurrence
String.prototype.boldUntil = function(delimiter) {
    return '<b>' + this.replace(delimiter, delimiter + '</b>');
};
String.prototype.boldBefore = function(delimiter) {
    return '<b>' + this.replace(delimiter, '</b>' + delimiter);
};
$(document).ready(function() {
    $('a.dbl-link').on('click', function (e) {
        e.preventDefault();
        var hitCallbackFn, href = $(this).attr('href');
        if (window.isBlocked) {
            hitCallbackFn = function () {window.location = href;};
            window.open(window.location.href);
        } else {
            hitCallbackFn = function () {window.open(href);};
        }

        if($(this).data('track') == '1') {
            ga('send', 'event', {
                eventCategory: 'Outbound Link', eventAction: 'click', eventLabel: href,
                hitCallback: createFunctionWithTimeout(hitCallbackFn)
            });
        } else {
            hitCallbackFn();
        }
        return false;
    });
});

function createFunctionWithTimeout(callback, opt_timeout) {
  var called = false;
  function fn() {
    if (!called) {
      called = true;
      callback();
    }
  }
  setTimeout(fn, opt_timeout || 1000);
  return fn;
}