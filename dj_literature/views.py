from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from collections import OrderedDict
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
    return Response(["Dashboard", "Collections", "Tags"])


@api_view(['GET'])
def get_dashboard(request):
    """
    总菜单
    """
    return Response([{"name": "All articles", "key": "all"}, {"name": "Unread", "Key": "unread"}])


@api_view(['GET'])
def get_all_articles(request):
    """
    所有文章
    """
    title = Field.objects.get(fieldname='title')
    items = Item.objects.all()
    item_datas = ItemData.objects.filter(item__in=items).filter(field=title)
    itemdata_serializer = ItemDataRest(item_datas, many=True)
    item_title = []
    for temp in itemdata_serializer.data:
        dic = temp.items()
        odict = OrderedDict(dic)
        item_title += [{'id': odict.pop('item'), 'title': odict.pop('value')}]
    return JsonResponse(item_title, safe=False)


@api_view(['GET'])
def get_itemdata(request, item_id):
    """
    所有文章
    """
    field = Field.objects.all()
    field_dic = {}
    for fi in list(field):
        field_dic[fi.id] = fi.fieldname
    item = Item.objects.get(id=item_id)
    item_datas = ItemData.objects.filter(item=item).filter(field__in=field)
    item_data_serializer = ItemDataRest(item_datas, many=True)
    item_data_title = {}
    for temp in item_data_serializer.data:
        temp_dic = OrderedDict(temp.items())
        item_data_title[field_dic.get(temp_dic.pop('field'))] = temp_dic.pop('value')
    return JsonResponse(item_data_title, safe=False)


@api_view(['GET'])
def get_articles_by_tag_name(request, tag_name):
    """
    所有tag下的文章
    """
    item_tags = []
    items = []
    tags = Tag.objects.filter(name=tag_name)
    for tag in tags:
        item_tags += list(ItemTag.objects.filter(tag=tag.id))
    print(item_tags)
    for item_tag in item_tags:
        print(item_tag)
        items += list(Item.objects.filter(id=item_tag.item_id))
    serializer = ItemRest(items, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_articles_by_collection_name(request, collectionName):
    """
    所有collectionname下的文章
    """
    items = []
    parent = list(Collection.objects.filter(collectionname=collectionName))[0]
    collections = list(Collection.objects.filter(parentcollection=parent.id))
    collection_items = list(CollectionItem.objects.filter(collection=parent.id))
    for collection_item in collection_items:
        items += list(Item.objects.filter(id=collection_item.item_id))
    item_serializer = ItemRest(items, many=True)
    collection_serializer = CollectionRest(collections, many=True)

    return JsonResponse(item_serializer.data, safe=False)


@api_view(['GET'])
def get_tags_4_item(request, id):
    """
    所有collectionname下的文章
    """
    item_tags = list(ItemTag.objects.filter(item=id))
    print(item_tags)
    tags = []
    for item_tag in item_tags:
        tags += list(Tag.objects.filter(id=item_tag.tag_id))

    print(tags)
    serializer = TagRest(tags, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def url_test(request):
    """
    测试ris导入
    """
    # risfile = "D:\\github\\LiteratureView\\tests\\Exported_Items\\Exported_Items.ris"
    risfile = "D:\\gitspace\\LiteratureView\\tests\\Exported_Items\\Exported_Items.ris"
    entries = importris(risfile)
    # insertitem(entries)
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET', 'POST'])
def collection_(request):
    """
    添加collection
    """
    if request.method == 'GET':
        params = request.data
        parentid = params['parentcollection']
        print(parentid)
        if parentid is None:
            collection = Collection.objects.filter(parent_collection=None)
        else:
            parent_collection = Collection.objects.get(id=parentid)
            collection = Collection.objects.filter(parentcollection=parent_collection)
        serializer = CollectionRest(collection, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        params = request.data
        parentid = params['parentcollection']
        collectionname = params['collectionname']
        if parentid is None:
            # //todo 这里面想要把引用引用到自己。parentid或者为null；不要建一个基础的；null数据是他们的祖id
            collection = Collection(parentcollection=None, key=randomkey(), collectionname=collectionname)
        else:
            parent_collection = Collection.objects.get(id=parentid)
            collection = Collection(parentcollection=parent_collection, key=randomkey(), collectionname=collectionname)

        if collection.save():
            serializer = CollectionRest(collection)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"state": "success"})


@api_view(['GET', 'POST'])
def tag_(request):
    """
    添加collection
    """
    if request.method == 'GET':
        params = request.data
        id_ = ""
        tag_name = ""
        if 'id' in params:
            id_ = params['id']
        if 'tag_name' in params:
            tag_name = params['tag_name']
        if id_ is not None and id_ is not "":
            tag = Tag.objects.get(id=id_)
            serializer = TagRest(tag)
            return JsonResponse(serializer.data)
        elif tag_name is not None and tag_name is not "":
            tag = Tag.objects.all().filter(name=tag_name)
            serializer = TagRest(tag, many=True)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        params = request.data
        tagtype = ""
        if 'tagtype' in params:
            tagtype = params['tagtype']
        name = params['name']
        if tagtype is None or tagtype is "":
            tagtype = "1"
        tag_1 = Tag(tagtype=tagtype, name=name)
        tag_1.save()
        serializer = TagRest(tag_1)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({"state": "success"})


@api_view(['GET', 'POST'])
def itemtag(request):
    """
    添加collection
    """
    if request.method == 'GET':
        return JsonResponse({"hello": "world"}, safe=False)
    elif request.method == 'POST':
        params = request.data
        # item_id = request.POST.get('item', 37)
        # tag_id = request.POST.get('tag', 1)
        item_id = params['item']
        tag_id = params['tag']
        print(item_id)
        print(tag_id)
        item = Item.objects.get(id=item_id)
        tag = Tag.objects.get(id=tag_id)
        item_tag = ItemTag(item=item,tag=tag)
        item_tag.save()
        serializer = ItemTagRest(item_tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({"state": "success"})


@api_view(['GET', 'POST'])
def collection_item(request):
    """
    添加collection
    """
    if request.method == 'GET':
        return JsonResponse({"hello": "world"}, safe=False)
    elif request.method == 'POST':
        params = request.data
        # item_id = request.POST.get('item', 37)
        # tag_id = request.POST.get('tag', 1)
        item_id = params['item']
        collection_id = params['collection']
        item = Item.objects.get(id=item_id)
        collection = Collection.objects.get(id=collection_id)
        item_collection = CollectionItem(item=item, collection=collection,
                                         orderindex=random.randint(0, 1000000000))
        item_collection.save()
        serializer = CollectionItemRest(item_collection)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({"state": "success"})
