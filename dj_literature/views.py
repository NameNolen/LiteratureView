from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .rest_models import *


# Create your views here.


def index(request):
    return render(request, 'dj_literature/index.html')


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


class CollectionItemList(generics.ListCreateAPIView):
    queryset = CollectionItem.objects.all()
    serializer_class = CollectionItemRest


class CollectionItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CollectionItem.objects.all()
    serializer_class = CollectionItemRest


class ItemCreators(generics.ListCreateAPIView):
    queryset = ItemCreator.objects.all()
    serializer_class = ItemCreatorRest


class ItemCreatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemCreator.objects.all()
    serializer_class = ItemCreatorRest


class ItemTypeCreatorTypeList(generics.ListCreateAPIView):
    queryset = ItemTypeCreatorType.objects.all()
    serializer_class = ItemTypeCreatorTypeRest


class ItemTypeCreatorTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemTypeCreatorType.objects.all()
    serializer_class = ItemTypeCreatorTypeRest


class CreatorTypeList(generics.ListCreateAPIView):
    queryset = CreatorType.objects.all()
    serializer_class = CreatorTypeRest


class CreatorTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreatorType.objects.all()
    serializer_class = CreatorTypeRest


class CreatorList(generics.ListCreateAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorRest


class CreatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorRest


class ItemTypeList(generics.ListCreateAPIView):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeRest


class ItemTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeRest


class ItemDataList(generics.ListCreateAPIView):
    queryset = ItemData.objects.all()
    serializer_class = ItemTagRest


class ItemDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemData.objects.all()
    serializer_class = ItemDataRest


class ItemTagList(generics.ListCreateAPIView):
    queryset = ItemTag.objects.all()
    serializer_class = ItemTagRest


class ItemTagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemTag.objects.all()
    serializer_class = ItemTagRest


class ItemTypeFieldList(generics.ListCreateAPIView):
    queryset = ItemTypeField.objects.all()
    serializer_class = ItemTypeFieldRest


class ItemTypeFieldDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemTypeField.objects.all()
    serializer_class = ItemTypeFieldRest


class FieldList(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldRest


class FieldDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldRest


class ItemNoteList(generics.ListCreateAPIView):
    queryset = ItemNote.objects.all()
    serializer_class = ItemNoteRest


class ItemNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemNote.objects.all()
    serializer_class = ItemNoteRest


class FileTypeList(generics.ListCreateAPIView):
    queryset = FileType.objects.all()
    serializer_class = FileTypeRest


class FileTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FileType.objects.all()
    serializer_class = FileTypeRest


class FileTypeMimeTypeList(generics.ListCreateAPIView):
    queryset = FileTypeMimeType.objects.all()
    serializer_class = FileTypeMimeTypeRest


class FileTypeMimeTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FileTypeMimeType.objects.all()
    serializer_class = FileTypeMimeTypeRest


class ItemAttachmentList(generics.ListCreateAPIView):
    queryset = ItemAttachment.objects.all()
    serializer_class = ItemAttachmentRest


class ItemAttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemAttachment.objects.all()
    serializer_class = ItemAttachmentRest


class DeletedItemList(generics.ListCreateAPIView):
    queryset = DeletedItem.objects.all()
    serializer_class = DeletedItemRest


class DeletedItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeletedItem.objects.all()
    serializer_class = DeletedItemRest


@api_view(['GET'])
def get_menus(request):
    """
    总菜单
    """
    return Response(["Dashboard", "All articles", "Collection", "Tags"])
