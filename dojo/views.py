# dojo/views.py
import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

#def mysum(request, x, y=0, z=0):
    # request: HttpRequest
    #return HttpResponse(int(x) + int(y) + int(z))

def mysum(request, numbers):
    # numbers = "1/23/3143/32131251/123"
    #result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('Hi, {}. {} years old.'.format(name, age))

def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>'''.format(name=name))

def post_list2(request):
    name = '공유'
    response = render(request, 'myapp/post_list.html', {'name': name})
    return response

def post_list3(request): #'FBV: JSON 형식 응답하기'
    return JsonResponse({
        'message': '안녕, 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'], }, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
#filepath = '/other/path/excel.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response