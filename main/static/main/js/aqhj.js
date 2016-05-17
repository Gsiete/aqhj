$(document).ready(function(){
    var fm = $('#following-matches'), fmToggle = $('#fm-toggle');

    fmToggle.on('click', function(){
        fm.collapse('toggle');
    });
    fm.on('show.bs.collapse', function(){
        fmToggle.addClass('collapsed');
    }).on('hide.bs.collapse', function(){
        fmToggle.removeClass('collapsed');
    });
});

// JS replace replaces only until the first occurrence
String.prototype.boldUntil = function(delimiter) {
    return '<b>' + this.replace(delimiter, delimiter + '</b>');
};
String.prototype.boldBefore = function(delimiter) {
    return '<b>' + this.replace(delimiter, '</b>' + delimiter);
};