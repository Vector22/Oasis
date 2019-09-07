from django.http import HttpResponseBadRequest


def ajax_required(f):
    """
        Check if a request is ajax
        Return an HttpResponseBadRequest otherwise
    """
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
