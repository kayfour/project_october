from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
 return HttpResponse("Hello, Captain America!")

def responsewithhtml(request):
    data = {'first': '클린트', 'second': '바튼'}

    return render(request, 'hello/responsewithhtml.html', context=data)

def home(request):
    return render(request,'home.html')

def template(request):
    return render(request, 'hello/template.html')

def form(request):
    return render(request, 'hello/requestform.html')

def responsewithhtml(request):

    # data = {'first': 'Sanghun', 'second': 'Oh'}
    data = dict()
    data['first'] = request.GET['first'];
    data['second'] = request.GET['second']
    return render(request, 'hello/responsewithhtml.html', context=data)

def requestwithservice(request):
    data = request.GET.copy()
    data['result'] = cal(data['firstvalue'], data['secondvalue'])
    return render(request, 'hello/requestwithservice.html', context=data)

def cal(first, second):
    result = int(first) * int(second)
    return result    