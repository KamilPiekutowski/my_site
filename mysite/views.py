#mysite/mysite/views.py
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail, get_connection

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

# \my_site\my_site\views.py

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email','noreply@example.com'),
                    ['siteowner@example.com'],
                    connection=con
                    )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm()
        return render(request,'contact_form.html', {'form' : form})

# \my_site\my_site\views.py

def contact_thanks(request):
    return HttpResponse('Thank you for your message!')
