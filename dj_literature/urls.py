from django.urls import path

from . import views

# todo 还有好多没有做
urlpatterns = [
    path('', views.index, name='index'),
    path('collections/', views.CollectionList.as_view(), name='collection_list'),
    path('collections/<int:pk>', views.CollectionDetail.as_view(), name='collection_detail'),

    path('items/', views.ItemList.as_view(), name='item_list'),
    path('items/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),

    path('tags/', views.TagList.as_view(), name='tag_list'),
    path('tags/<int:pk>', views.TagDetail.as_view(),name='tag_detail'),

    path('item_tags', views.ItemTagList.as_view(), name='item_tag_list'),
    path('item_tags/<int:pk>', views.ItemTagDetail.as_view(), name='item_tag_detail'),

    # 这个作为主要的查询.所有的item有一个collection,如果没有明确指定,则为root
    path('collection_items/', views.CollectionItemList.as_view(), name='collection_item_list'),
    path('collection_items/<int:pk>', views.CollectionItemDetail.as_view(), name='collection_item_detail'),


    path('creators/', views.CreatorList.as_view(), name='creator_list'),
    path('creators/<int:pk>', views.CreatorDetail.as_view(), name='creator_detail'),

    path('item_creators/', views.ItemCreators.as_view(), name='item_creator_list'),
    path('item_creators/<int:pk>', views.ItemCreatorDetail.as_view(), name='item_creator_detail'),

    path('item_type_creator_types/', views.ItemTypeCreatorTypeList.as_view(), name='item_type_creator_type_list'),
    path('item_type_creator_types/<int:pk>', views.ItemTypeCreatorTypeDetail.as_view(), name='item_type_creator_type_Detail'),

    path('item_types', views.ItemTypeList.as_view(), name='item_type_list'),
    path('item_types/<int:pk>', views.ItemTypeDetail.as_view(), name='item_type_detail'),

    path('creator_types/', views.CreatorTypeList.as_view(), name='creator_type_list'),
    path('creator_types/<int:pk>', views.CreatorTypeDetail.as_view(),name='creator_type_detail'),

    # value中没有值
    path('item_data_list/', views.ItemDataList.as_view(), name='item_data_list'),
    path('item_data_list/<int:pk>', views.ItemDataDetail.as_view(), name='item_data_detail'),

    path('item_type_fields/', views.ItemTypeFieldList.as_view(), name='item_type_field_list'),
    path('item_type_fields/<int:pk>', views.ItemTypeFieldDetail.as_view(), name='item_type_field_detail'),

    path('fields/', views.FieldList.as_view(), name='field_list'),
    path('fields/<int:pk>', views.FieldDetail.as_view(), name='field_detail'),

    path('item_notes/', views.ItemNoteList.as_view(), name='item_note_list'),
    path('item_notes/<int:pk>', views.ItemNoteDetail.as_view(), name='item_note_detail'),

    # path('file_types', views.file_type_list, name='file_type_list'),
    # path('file_type_mime_types', views.file_type_mime_type_list, name='file_type_mime_type_list'),

    # path('item_attachments', views.item_attachment_list, name='item_attachment_list'),
    # path('deleted_items', views.deleted_item_list, name='deleted_item_list'),
]
