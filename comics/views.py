from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from models import Comic

def view_comic(request, number=None):
    if number == None:
        number = Comic.objects.order_by('-id')[0].id
    variables = RequestContext(request, {'comic': get_object_or_404(Comic, id=number)})
    response = render_to_response('comic.html', variables)
    return response

