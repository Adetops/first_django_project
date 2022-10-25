from django.http import HttpResponse

def index(Request):
    return HttpResponse("This is a musicapp")