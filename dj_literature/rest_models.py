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
        fields = '__all__'


# class CreatorData(serializers.ModelSerializer):
#    firstname = models.CharField(max_length=200)
#    lastname = models.CharField(max_length=200)
#    def __unicode__(self):
#        return ' '.join([self.firstname,self.lastname])

# Problem: People with same name?
class CreatorRest(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'


class FieldRest(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


# File model
class FileTypeRest(serializers.ModelSerializer):
    class Meta:
        model = FileType
        fields = '__all__'


class FileTypeMimeTypeRest(serializers.ModelSerializer):
    class Meta:
        model = FileTypeMimeType
        fields = '__all__'
        depth = 2


# Item model
class ItemTypeRest(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'


class ItemTypeFieldRest(serializers.ModelSerializer):
    class Meta:
        model = ItemTypeField
        fields = '__all__'
        depth = 2


class ItemTypeCreatorTypeRest(serializers.ModelSerializer):
    class Meta:
        model = ItemTypeCreatorType
        fields = '__all__'
        depth = 2


# class ItemDataValue(serializers.ModelSerializer):
#    value = models.TextField()

class ItemRest(serializers.ModelSerializer):
    dateadded = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    datemodified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class ItemDataRest(serializers.ModelSerializer):
    class Meta:
        model = ItemData
        fields = '__all__'


class ItemCreatorRest(serializers.ModelSerializer):
    class Meta:
        model = ItemCreator
        fields = '__all__'
        depth = 3


class CollectionRest(serializers.ModelSerializer):
    dateadded = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    datemodified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'
        depth = 2


class CollectionItemRest(serializers.ModelSerializer):
    class Meta:
        model = CollectionItem
        fields = '__all__'
        depth=2


class DeletedItemRest(serializers.ModelSerializer):
    class Meta:
        model = DeletedItem
        fields = '__all__'
        depth = 2


class ItemAttachmentRest(serializers.ModelSerializer):
    class Meta:
        model = ItemAttachment
        fields = '__all__'
        depth = 2


class ItemNoteRest(serializers.ModelSerializer):
    class Meta:
        model = ItemNote
        fields = '__all__'
        depth = 1


# Tag model
class TagRest(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ItemTagRest(serializers.ModelSerializer):
    class Meta:
        model = ItemTag
        fields = '__all__'
        depth = 2
