from dal import autocomplete
from cities.models import City


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return City.objects.none()

        qs = City.objects.all()

        if self.q:
            qs = qs.filter(name__startswith=self.q)

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
