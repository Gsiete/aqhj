/**
 * Created by gab on 08/05/16.
 */

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