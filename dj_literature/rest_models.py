from rest_framework import serializers
from .models import *

"""
## TODO:
* update to new django version
* replace raise statement for mild error, record them.
"""


class CreatorTypeRest(serializers.ModelSerializer):
    class Meta:
        model = CreatorType
        fields = ('creatortype')


# class CreatorData(serializers.ModelSerializer):
#    firstname = models.CharField(max_length=200)
#    lastname = models.CharField(max_length=200)
#    def __unicode__(self):
#        return ' '.join([self.firstname,self.lastname])

# Problem: People with same name?
class CreatorRest(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ('firstname', 'lastname', 'dateadded', 'datemodified')


class FieldRest(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('fieldname')


# File model
class FileTypeRest(serializers.ModelSerializer):
    class Meta:
        model = FileType
        fields = ('filetype')


class FileTypeMimeTypeRest(serializers.ModelSerializer):
    class Meta:
        model = FileTypeMimeType
        fields = ('filetype', 'mimetype')


# Item model
class ItemTypeRest(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = ('typename', 'display')


class ItemTypeFieldRest(serializers.ModelSerializer):
    class Meta:
        model = ItemTypeField
        fields = ('itemtype', 'field', 'orderindex')


class ItemTypeCreatorTypeRest(serializers.ModelSerializer):
    class Meta:
        model = ItemTypeCreatorType
        fields = ('itemtype', 'creatortype', 'primaryfield')


# class ItemDataValue(serializers.ModelSerializer):
#    value = models.TextField()

class ItemRest(serializers.ModelSerializer):
    dateadded = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    datemodified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Item
        fields = ('itemtype', 'dateadded', 'datemodified', 'key')


class ItemDataRest(serializers.ModelSerializer):
    class Meta:
        model = ItemData
        fields = ('item', 'field', 'value')


class ItemCreatorRest(serializers.ModelSerializer):
    class Meta:
        model = ItemCreator
        fields = ('item', 'creator', 'creatortype', 'orderindex')


class CollectionRest(serializers.ModelSerializer):
    dateadded = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    datemodified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Collection
        fields = ('collectionname', 'parentcollection', 'dateadded', 'datemodified', 'key')
        depth = 2


class CollectionItemRest(serializers.ModelSerializer):
    class Meta:
        model = CollectionItem
        fields = ('collection', 'item', 'orderindex')
        depth=2


class DeletedItemRest(serializers.ModelSerializer):
    class Meta:
        model = DeletedItem
        fields = ('item', 'datedeleted')


class ItemAttachmentRest(serializers.ModelSerializer):
    class Meta:
        model = ItemAttachment
        fields = ('item', 'sourceitem', 'attachment', 'mimetype')


class ItemNoteRest(serializers.ModelSerializer):
    class Meta:
        model = ItemNote
        fields = ('title', 'note', 'item', 'sourceitem')


# Tag model
class TagRest(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'tagtype', 'dateadded', 'datemodified')


class ItemTagRest(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('item', 'tag')
