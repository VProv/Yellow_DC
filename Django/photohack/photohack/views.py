from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from rest_framework.decorators import api_view

from .api_picture import upload, result

from rest_framework.status import HTTP_404_NOT_FOUND


class IndexView(TemplateView):
    template_name = 'index.html'


@api_view(['POST'])
def user_upload(request):
    """
    Upload view for the user.
    """
    r = upload(request)
    if type(r) == int:
        return HttpResponseRedirect('/result?id={}'.format(r))
    else:
        return r


@api_view(['GET'])
def user_result(request):
    """
    Result view for the user.
    Renders a failure page in case an image has not been processed yet
    """
    r = result(request)
    if r is None:
        return HttpResponse(render_to_string('processing.html', {'id': request.GET['id']}))
    if type(r) == dict:
        return HttpResponse(render_to_string('result.html', r))
    else:
        if r.status_code == HTTP_404_NOT_FOUND:
            return HttpResponseNotFound()
        return r
