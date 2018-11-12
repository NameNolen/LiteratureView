from django.http import HttpResponse


# Create your views here.
# todo 只是做了index。

def index(request):
    return HttpResponse("Hello, world. You're at the literature index.")
