from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# todo 只是做了index。

def index(request):
    return render(request, 'dj_literature/index.html')
