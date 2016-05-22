$(document).ready(function(){
    $('#fm-toggle').on('click', function(){
        $(this).toggleClass('collapsed');
        $(this).find('.glyphicon').toggleClass('glyphicon-menu-up');
        setTimeout(function() {
            $('#following-matches').collapse('toggle');
            $('#time-clarification').collapse('toggle');
        }, 100);
    });
});

// JS replace replaces only until the first occurrence
String.prototype.boldUntil = function(delimiter) {
    return '<b>' + this.replace(delimiter, delimiter + '</b>');
};
String.prototype.boldBefore = function(delimiter) {
    return '<b>' + this.replace(delimiter, '</b>' + delimiter);
};