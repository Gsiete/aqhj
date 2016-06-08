from dal import autocomplete
from django.shortcuts import redirect, get_object_or_404

from cities.models import City
from main.functions import set_cookie


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = City.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

    def get_results(self, context):
        """Return data for the 'results' key of the response.
        :type context: dict[str, list[City]]
        """
        return [
            {
                'id': self.get_result_value(result),
                'text': result.get_display_name(),
                'tz': str(result.timezone),
            } for result in context['object_list']
        ]


def set_city(request, **kwargs):
    resp = redirect('index', permanent=True)
    city = get_object_or_404(City, **kwargs)
    set_cookie(resp, 'city_code', city.id)

    return resp
