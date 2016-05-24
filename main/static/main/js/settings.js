/**
 * Created by gab on 08/05/16.
 */

$(document).ready(function(){
    var $changeCityButton = $('#change-city'), $cityElement = $('#city'), $confirmCityButton = $('#confirm-city'),
        $settingsModal = $('#settings-modal');


    if($settingsModal.data('show') == 'yes'){
        $settingsModal.modal('show');
    }

    $('#format-12').on('click', function() {
        $("#format-24").removeClass('activated');
        $("#format-12").addClass('activated');
        $(".am-pm").removeClass('hidden');
        document.cookie = "tformat=12; path=/";
        $('.var-tformat').data('tformat', 'h:mm');
        $(document).trigger('tformat-change');
    });
    $('#format-24').on('click', function() {
        $("#format-12").removeClass('activated');
        $("#format-24").addClass('activated');
        $(".am-pm").addClass('hidden');
        document.cookie = "tformat=24; path=/";
        $('.var-tformat').data('tformat', 'H:mm');
        $(document).trigger('tformat-change');
    });

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
                $changeCityButton.removeClass('activated');
                $confirmCityButton.addClass('activated');
                $(document).trigger('tz-change', [$selectedCity.data('tz'), cityName, cityId]);
                $cityElement.html(cityName.boldUntil(','));
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