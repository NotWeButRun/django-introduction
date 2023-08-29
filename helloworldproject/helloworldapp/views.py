from django.shortcuts import render
from django.http import HttpResponse

def helloworldfunction(request):
    return HttpResponse("<b>Hello World! '='</b>")

# Create your views here.
