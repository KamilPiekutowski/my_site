#mysite/mysite/views.py
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
