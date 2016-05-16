$(document).on('tz-change', function (e, tz, cityName, cityId) {
    document.cookie = "city_code=" + cityId + "; path=/";

    $('.js-local-time').each(function () {
        $(this).data('tz', tz);
        updateTime($(this), tz);
    });

    $('.var-city').each(function () {
        $(this).text(cityName);
    });
});

$(document).on('tformat-change', function (e, tz) {

    $('.time').each(function () {
        // ToDo: evaluate changing only the '.var-tformat' elements
        updateTime($(this), $(this).data('tz'));
    });
});

var updateTime = function($elem, tz) {
        var localTime = moment($elem.data('time')).tz(tz);
        localTime.locale('es');
        $elem.find('.var-time').each(function () {
            var dateTimePart = localTime.format($(this).data('tformat'));
            if ($(this).data('bold-hours')) {
                dateTimePart = dateTimePart.boldUntil(':');
            }
            $(this).html(dateTimePart);
        });
};