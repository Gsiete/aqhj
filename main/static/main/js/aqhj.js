$(document).ready(function(){
    var fm = $('#following-matches'), fmToggle = $('#fm-toggle');

    fmToggle.on('click', function(){
        fmToggle.toggleClass('collapsed');
        fm.collapse('toggle');
    });
});

// JS replace replaces only until the first occurrence
String.prototype.boldUntil = function(delimiter) {
    return '<b>' + this.replace(delimiter, delimiter + '</b>');
};
String.prototype.boldBefore = function(delimiter) {
    return '<b>' + this.replace(delimiter, '</b>' + delimiter);
};