from django.urls import path

from . import views

# todo 还有好多没有做
urlpatterns = [
    path('', views.index, name='index'),
    path('items', views.item_list, name='item_list'),
    path('collections', views.collection_list, name='collection_list'),

    # 这个作为主要的查询.所有的item有一个collection,如果没有明确指定,则为root
    path('collectionItems', views.collection_item_list, name='collection_item_list'),
]
