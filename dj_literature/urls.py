from django.urls import path

from . import views

# todo 还有好多没有做
urlpatterns = [
    path('', views.index, name='index'),
    path('items', views.item_list, name='item_list'),
    path('collections', views.collection_list, name='collection_list'),
    path('item_datas', views.item_data_list, name='item_data_list'),

    # 这个作为主要的查询.所有的item有一个collection,如果没有明确指定,则为root
    path('collection_items', views.collection_item_list, name='collection_item_list'),

    path('creator_types', views.creator_type_list, name='creator_type_list'),
    path('creators', views.creator_list, name='creator_list'),
    path('fields', views.field_list, name='field_list'),
    path('file_types', views.file_type_list, name='file_type_list'),
    path('file_type_mime_types', views.file_type_mime_type_list, name='file_type_mime_type_list'),
    path('item_types', views.item_type_list, name='item_type_list'),
    path('item_type_fields', views.item_type_field_list, name='item_type_field_list'),
    path('item_type_creator_types', views.item_type_creator_type_list, name='item_type_creator_type_list'),
    path('item_creators', views.item_creator_list, name='item_creator_list'),
    path('deleted_items', views.deleted_item_list, name='deleted_item_list'),
    path('item_attachments', views.item_attachment_list, name='item_attachment_list'),
    path('item_notes', views.item_note_list, name='item_note_list'),
    path('tags', views.tag_list, name='tag_list'),
    path('item_tags', views.item_tag_list, name='item_tag_list'),
]
