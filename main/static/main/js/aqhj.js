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