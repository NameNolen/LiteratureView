from django.contrib import admin

# Register your models here.

from .models import Item, Collection
# todo 自动生成后没有itemtype，保存不了
admin.site.register(Item)
# todo 自动生成的的view保存时报错，没有父id
admin.site.register(Collection)
