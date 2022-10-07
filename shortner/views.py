from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from . models import Shortner
from . forms import URLShortnerForm
import pyqrcode
import png

def home(request):

    template = 'shortner/home.html'

    context = {}

    context['form'] = URLShortnerForm()

    if request.method == "GET":
        return render(request, template, context)
    
    elif request.method == "POST":
        used_form = URLShortnerForm(request.POST)

        if used_form.is_valid():
            shortned_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortned_object.short_url
            long_url = shortned_object.long_url

            qrcode = pyqrcode.create(long_url)
            qrcode.png('static/images/{}.png'.format(new_url[22:]), scale = 3)

            context['new_url'] = new_url
            context['long_url'] = long_url
            context['qrcode'] = 'static\images\{}.png'.format(new_url[22:])
            
            return render(request, template, context)

        context['error'] = used_form.errors

        return render(request, template, context)

def redirect_url_view(request, shortend_part):

    try:
        shortner = Shortner.objects.get(short_url=shortend_part)
        shortner.total_clicks += 1
        shortner.save()

        return HttpResponseRedirect(shortner.long_url)
    except:
        raise Http404('Sorry this link is broken :(')

