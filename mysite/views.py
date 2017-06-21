#mysite/mysite/views.py
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return render(request, 'hello.html')

def index(request):
    return render(request, 'index.html')

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)

    params = {
            'offset' : offset,
            'dt' : dt,
            }

    return render(request, 'hours_ahead.html', params)


def display_meta(request):
    values = request.META.items()
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k[0], k[1]))

    return HttpResponse('<table>%s</table>' % '\n'.join(html))

# \books\views.py

def search_form(request):
    return render(request,'books/search_from.html')
