from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    return HttpResponse("<b>Hello World! ^^/</b>")

class HelloWorldClass(TemplateView):
    template_name = "hello.html"
