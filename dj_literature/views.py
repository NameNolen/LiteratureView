from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .models import *
from .rest_models import *


# Create your views here.
# todo 只是做了index。

def index(request):
    return render(request, 'dj_literature/index.html')


@csrf_exempt
def item_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemRest(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def collection_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = Collection.objects.all()
        serializer = CollectionRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CollectionRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def collection_item_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = CollectionItem.objects.all()
        serializer = CollectionItemRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CollectionItemRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
