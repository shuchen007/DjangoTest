from django.http import HttpResponse
# def hello(request):
#     return HttpResponse("Hello world dogo! ")

from django.shortcuts import render
def hello(request):
    context = {}
    context['x'] = 'Hello12 Worldfd,fjdk,fd!'
    context['y'] = 'Hello12 World!'
    context['z'] = ''
    return render(request, 'hello.html', context)

def index(request):
    context = {}
    context['hello'] = 'index!'
    context['user'] = 'Hello12 World!'
    context['currentuser'] = 'Hello12 World!'
    return render(request, 'index.html', context)