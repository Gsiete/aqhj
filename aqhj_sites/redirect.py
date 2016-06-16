from django.http.response import Http404
from django.shortcuts import redirect

from aqhj_sites.models import RedirectOn404


class RedirectMiddleware(object):
    def process_exception(self, request, exception):
        if exception is Http404:
            redirect_object = RedirectOn404.objects.filter(source=request.get_full_path()).first()

            if redirect_object is not None:
                return redirect(redirect_object.target, permanent=True)

        return None