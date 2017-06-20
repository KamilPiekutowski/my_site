from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def index(request):
    return HttpResponse("<h1>This is a homepgae</h1>")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)
