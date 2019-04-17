"""
视图函数
将函数和路由绑定
"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from django.template import loader
# Create your views here.


def index(request):
    # return HttpResponse('首页')
    # 加载模板
    # temp = loader.get_template('booktests/index.html')
    # # 渲染模板
    # con = {'username':'董昊'}
    # tes = temp.render(con)
    # return HttpResponse(tes)
    return render(request,'booktests/index.html', {'username':'董昊'})

def list(request):
    # return HttpResponse('列表页')
    # temp = loader.get_template('booktests/lists.html')
    # tes = temp.render({})
    # return HttpResponse(tes)
    booklist = BookInfo.objects.all()
    return render(request,'booktests/lists.html', {'booklist':booklist})

def detail(request,id):
    book = BookInfo.objects.get(pk=id)
    return render(request, 'booktests/deile.html', {'id':book})







