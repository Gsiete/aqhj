$(document).ready(function() {
    $('#cuartos').on('click', function() {
        $('#inner-view').animate({'left': 0});
        $('.phase-choice').removeClass('active');
        $(this).addClass('active')
    });
    $('#semi').on('click', function() {
        $('#inner-view').animate({'left': '-100%'});
        $('.phase-choice').removeClass('active');
        $(this).addClass('active')

    });
    $('#final').on('click', function() {
        $('#inner-view').animate({'left': '-200%'});
        $('.phase-choice').removeClass('active');
        $(this).addClass('active')
    });
});