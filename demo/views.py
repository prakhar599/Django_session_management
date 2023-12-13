from django.http import HttpResponse
from django.shortcuts import render


def setsession(request):
    request.session['name'] = 'Prakhar'
    return HttpResponse('Session set !')

def getsession(request):
    name = request.session['name']
    return render(request,'demo/get.html',{'name' : name} )

def delsession(request):
    # del request.session['name']
    request.session.flush()
    return HttpResponse('Session deleted !')