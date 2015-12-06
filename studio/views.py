from django.http import HttpResponse


def index(request):

    html_str = 'Winter sucks.'
    return HttpResponse(html_str)
