String.prototype.ucfirst = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
};

$(document).on('tz-change', function (e, tz, cityName, cityId) {
    document.cookie = "city_code=" + cityId + "; path=/";

    $('.js-local-time').each(function () {
        var localTime = moment($(this).data('time')).tz(tz);
        localTime.locale('es');
        $(this).find('.var-time').each(function () {
            var dateTimePart = localTime.format($(this).data('tformat'));
            //ToDo: deal with ucfirst().replace('.','') in the moment.js itself. and remove unnecessary locales
            $(this).text(dateTimePart.ucfirst().replace('.',''));
        });
    });

    $('.var-city').each(function () {
        $(this).text(cityName);
    });
});
