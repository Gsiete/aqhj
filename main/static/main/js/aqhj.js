$(document).ready(function(){
    $('#fm-toggle').on('click', function(){
        $(this).toggleClass('collapsed');
        $('#following-matches').collapse('toggle');
        $('#time-clarification').collapse('toggle');
    });
});

// JS replace replaces only until the first occurrence
String.prototype.boldUntil = function(delimiter) {
    return '<b>' + this.replace(delimiter, delimiter + '</b>');
};
String.prototype.boldBefore = function(delimiter) {
    return '<b>' + this.replace(delimiter, '</b>' + delimiter);
};