$(document).on('tz-change', function (e, tz, cityName, cityId) {
    var momentUTC = moment($('.local-time').data('time')),
        stadiumTimeOffset = parseInt(momentUTC.tz($('.stadium-time').data('tz')).format('Z')),
        localTimeOffset = parseInt(momentUTC.tz(tz).format('Z')),
        diff = stadiumTimeOffset - localTimeOffset;
    if(diff > 0) {
        diff = '+' + diff;
    }
    $('.var-time-diff').text(diff);
    document.cookie = "city_code=" + cityId + "; path=/";

    $('.js-local-time').each(function () {
        $(this).data('tz', tz);
        updateTime($(this), tz);
    });

    $('#mce-TIMEZONE').val(tz);
    var startOfCountryName = cityName.lastIndexOf(',');
    $('#mce-CITY').val(cityName.substr(0, startOfCountryName).trim());
    $('#mce-COUNTRY').val(cityName.substr(startOfCountryName+1).trim());

    $('.var-city').text(cityName);
});

$(document).on('tformat-change', function (e, tz) {

    $('.time').each(function () {
        // ToDo: evaluate changing only the '.var-tformat' elements
        updateTime($(this), $(this).data('tz'));
    });
});

var updateTime = function ($elem, tz) {
    var localTime = moment($elem.data('time')).tz(tz);
    localTime.locale('es');
    $elem.find('.var-time').each(function () {
        var time_format = $(this).data('tformat'), dateTimePart = '';
        if (time_format) {
            dateTimePart = localTime.format(time_format);
            if ($(this).data('bold-hours')) {
                dateTimePart = dateTimePart.boldBefore(':');
            }
        }

        $(this).html(dateTimePart);
    });
};