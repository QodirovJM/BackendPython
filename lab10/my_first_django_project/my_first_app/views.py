
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

def hello_world(request, name='World'):
    age = request.GET.get('age', 'unknown')
    response = HttpResponse(f"<h1>Hello, {name}! You are {age} years old.</h1>")
    response.set_cookie('username', name)
    return response

def redirect_example(request):
    return redirect('/hello/Guest/?age=25')

def json_example(request):
    data = {'name': 'Alice', 'age': 30}
    return JsonResponse(data)

def show_cookies(request):
    return HttpResponse(f"<pre>{{request.COOKIES}}</pre>")
