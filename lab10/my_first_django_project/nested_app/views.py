
from django.http import HttpResponse

def nested_home(request):
    return HttpResponse("<h2>This is nested app home.</h2>")

def nested_about(request):
    return HttpResponse("<h2>About nested app.</h2>")
