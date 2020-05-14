from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    #return HttpResponse("Hello world ! ")

    context = {}
    context['hello'] = 'Hello World!'  # 数据绑定
    return render(request, 'hello.html', context)  # 将绑定的数据传入前台

