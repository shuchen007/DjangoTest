from django.http import HttpResponse
from django.shortcuts import render_to_response, render

# 表单
def search_form(request):
    return render_to_response('search_post.html')
# 接收请求数据
def search_get(request):
    request.encoding = 'utf-8'
    print('get=',request)
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    elif 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
    # return render(request, "search_get.html")

# 接收POST请求数据
def search_post(request):
    ctx ={}
    print('post=',request)
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "search_post.html", ctx)

# 接收request请求数据
def search_request(request):
    if request.method == 'GET':
        print('get')
    elif request.method == 'POST':
        print('post')
    return HttpResponse("do")