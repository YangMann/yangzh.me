from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from djangoweb.projects import Cookie

__author__ = 'Yang ZHANG'


def home(request):
    return render_to_response('home.html')


def project_cookie(request, arg):
    if len(arg) == 0:
        return render_to_response('projects/Cookie/index.html')
    elif arg == "about":
        return render_to_response('projects/Cookie/about.html')
    elif arg == "paragraph":
        if request.META.get('REQUEST_METHOD', 'UNKNOWN') == 'GET' or request.META.get('REQUEST_METHOD',
                                                                                      'UNKNOWN') == 'UNKNOWN':
            c = RequestContext(request)
            t = get_template('projects/Cookie/main3.html')
            return HttpResponse(t.render(c))
        elif request.META.get('REQUEST_METHOD', 'UNKNOWN') == 'POST':
            cookie = Cookie.Cookie()
            return render_to_response('projects/Cookie/main4.html',
                                      {"out_words": cookie.slice(request.POST.get('user-input-1'))})
    else:
        return render_to_response('projects/Cookie/index.html')