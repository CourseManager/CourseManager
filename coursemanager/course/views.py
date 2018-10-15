from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'course/index.html')


def select(request,page):
    username = request.POST.get("username")
    password = request.POST.get("password")
    ret = {"username": username, "password": password}
    return render(request, 'course/select.html', ret)
