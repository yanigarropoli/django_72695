from django.shortcuts import render

from django.http import HttpResponse

def inicio (request):
    #return HttpResponse("<h1>Esta es mi primiera vista</h1>")
    return render(request, 'inicio.html')
 