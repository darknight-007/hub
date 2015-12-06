from django.http import HttpResponse
import urllib2
import simplejson

def index(request):

    html_str = 'Winter sucks.'
    return HttpResponse(html_str)
