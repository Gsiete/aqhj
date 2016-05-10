/**
 * Created by gab on 08/05/16.
 */

$(document).ready(function(){
    var $changeCityButton = $('#change-city'), $cityElement = $('#city'), $confirmCityButton = $('#confirm-city'),
        $settingsModal = $('#settings-modal');


    if($settingsModal.data('show') == 'yes'){
        $settingsModal.modal('show');
    }

    $changeCityButton.on('click', function() {
        if($cityElement.find('select').length == 0){
            $changeCityButton.addClass('activated');
            $confirmCityButton.removeClass('activated');
            $cityElement.html("<select style='width:175px'></select>");

            var $select2 = $cityElement.find('select');
            $select2.select2({
                ajax: {
                    url: '/cities/ajax/city-autocomplete/',
                    dataType: 'json',
                    delay: 250,
                    data: function (params) {
                        return {
                            q: params.term, // search term
                            page: params.page,
                            csrfmiddlewaretoken: $('#change-city').data('token')
                        };
                    }
                },
                placeholder: "Elige tu ciudad",
                templateResult: addTZ,
                templateSelection: addTZ
            });

            $select2.on("change", function (e) {
                var $selectedCity = $cityElement.find('.city-elem'), cityName = $(this).text(), cityId = $(this).val();

                $(document).trigger('tz-change', [$selectedCity.data('tz'), cityName, cityId]);
                var formattedCityName = '<b>' + cityName.replace(',', ',</b>');
                $cityElement.html(formattedCityName);
            });
        }
    });
});

var addTZ = function(city) {
    if (!city.id) {
        return city.text;
    }

    return $('<span class="city-elem" data-tz="' + city.tz + '">' + city.text + '</span>');
};