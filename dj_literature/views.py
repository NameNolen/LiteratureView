from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
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


class CollectionList(generics.ListCreateAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionRest


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionRest


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemRest


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemRest


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagRest


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagRest




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


@csrf_exempt
def creator_type_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = CreatorType.objects.all()
        serializer = CreatorTypeRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreatorTypeRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def creator_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = Creator.objects.all()
        serializer = CreatorRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreatorRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def field_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = Field.objects.all()
        serializer = FieldRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FieldRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def file_type_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = FileType.objects.all()
        serializer = FileTypeRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FileTypeRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def file_type_mime_type_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = FileTypeMimeType.objects.all()
        serializer = FileTypeMimeTypeRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FileTypeMimeTypeRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item_type_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = ItemType.objects.all()
        serializer = ItemTypeRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemTypeRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item_type_field_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = ItemTypeField.objects.all()
        serializer = ItemTypeFieldRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemTypeFieldRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item_type_creator_type_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = ItemTypeCreatorType.objects.all()
        serializer = ItemTypeCreatorTypeRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemTypeCreatorTypeRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item_data_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = ItemData.objects.all()
        serializer = ItemDataRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemDataRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item_creator_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = ItemCreator.objects.all()
        serializer = ItemCreatorRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemCreatorRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def deleted_item_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = DeletedItem.objects.all()
        serializer = DeletedItemRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeletedItemRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item_attachment_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = ItemAttachment.objects.all()
        serializer = ItemAttachmentRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemAttachmentRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item_note_list(request):
    """
    List all item.
    """
    if request.method == 'GET':
        collections = ItemNote.objects.all()
        serializer = ItemNoteRest(collections, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemNoteRest(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



