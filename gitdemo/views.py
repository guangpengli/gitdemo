from django.http import HttpResponse

def index_view(requset):
    return HttpResponse('hello git!')