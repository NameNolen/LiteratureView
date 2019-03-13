from django.db import models
from dj_literature.utils import *
import os, mimetypes, time
from bs4 import BeautifulSoup

"""
## TODO:
* update to new django version
* replace raise statement for mild error, record them.
"""


# method
def insert_itemdata(item, fieldname, itemtype, value):
    try:
        field = Field.objects.get(fieldname=fieldname)
    except:
        msg = 'Error: Can\'t get field ' + fieldname
        return False, msg
    # validate_ItemTypeField(itemtype,field)
    itemtypefield = ItemTypeField.objects.filter(field=field, itemtype=itemtype)
    if not itemtypefield:
        msg = 'Error: ItemType %d:%s don\'t match field %d:%s' % (
        itemtype.id, itemtype.typename, field.id, field.fieldname)
        return False, msg
    # insert_ItemData(item,field)
    for v in value:
        itemdata = ItemData(field=field, item=item, value=v)
        itemdata.save()
    return True, itemdata


def insert_itemtag(item, taglist, tagtype=1):
    for tag in taglist:
        try:
            tagmodel = Tag.objects.get(name=tag)
        except:
            tagmodel = Tag(name=tag, tagtype=tagtype)
            tagmodel.save()
        itemtag = ItemTag(item=item, tag=tagmodel)
        itemtag.save()
    return True, itemtag


def insert_creator(fieldname, item, itemtype, value):
    creatortype = CreatorType.objects.get(creatortype=fieldname)
    # validate_ItemTypeCreatorType(itemtype,creatortype)
    itemtypecreatortype = ItemTypeCreatorType.objects.filter(creatortype=creatortype, itemtype=itemtype)
    if not itemtypecreatortype:
        msg = 'Error: ItemType %d:%s don\'t match CreatorType %d:%s' % (
        itemtype.id, itemtype, creatortype.creatortype, creatortype.id)
        return False, msg
    order = 0
    for person in value:
        if not getpersonname(person)[0]:
            msg = getpersonname(person)[1]
            return False, msg
        lastname, firstname = getpersonname(person)[1]
        # try to find exsist creator
        creator = Creator.objects.filter(lastname=lastname, firstname=firstname)
        if not creator:
            creator = Creator(lastname=lastname, firstname=firstname)
            creator.save()
        elif len(creator) == 1:
            creator = creator[0]
        else:
            msg = 'Duplicate creator ' + str(creator)
            return False, msg
        # insert_ItemCreator(item,creator)
        itemcreator = ItemCreator(item=item, creator=creator, creatortype=creatortype, orderindex=order)
        itemcreator.save()
        order += 1
    return True, itemcreator


def insert_attachment(fieldname, item, filepath):
    itemtype = ItemType.objects.get(typename='attachment')
    sourceitem = Item(itemtype=itemtype, key=randomkey())
    sourceitem.save()
    import django.core.files
    # filetype = FileType.objects.get(filetype=fieldname)
    if not os.path.isfile(filepath):
        msg = 'It\'s not a file ' + filepath
        return False, msg
    # mimetype = get_FileTypeMimeType
    mimetype = mimetypes.guess_type(filepath)[0]
    # insert_ItemAttachment(item,mimetype)
    myfile = open(filepath, 'r')
    djfile = django.core.files.File(myfile)
    itemattachment = ItemAttachment(item=item, sourceitem=sourceitem, mimetype=mimetype, attachment=djfile)
    itemattachment.save()
    return True, itemattachment


def insert_itemnote(item, note):
    for inote in note:
        itemtype = ItemType.objects.get(typename='note')
        sourceitem = Item(itemtype=itemtype, key=randomkey())
        sourceitem.save()
        soup = BeautifulSoup(inote, 'lxml')
        [s.extract() for s in soup('script')]
        [s.extract() for s in soup('style')]
        if soup.title:
            title = soup.title.string
        else:
            for i in soup.stripped_strings:
                if i:
                    title = i
                    break
        itemnote = ItemNote(item=item, sourceitem=sourceitem, title=title, note=inote)
        itemnote.save()
    return True, itemnote


def importris(risfile):
    bibliography_file = open(risfile, 'r', encoding='UTF-8')
    entries = readris(bibliography_file)
    return list(entries)


def insertitem(entries):
    successentry = []
    problementry = []
    msg = []
    totalitem = len(entries)

    for entry in entries:
        # get itemtype
        type_name = entry.pop('itemtype')
        itemtype = ItemType.objects.get(typename=type_name)
        # item = insert_Item(itemtype,key)
        item = Item(itemtype=itemtype, key=randomkey())
        item.save()
        for k in entry:
            isok, result = getfieldtype(k)
            if isok:
                ftype, fname = result
            else:
                problementry.append({'msg': result, 'content': entry})
                item.delete()
                break
            if ftype == 'field':
                if fname == 'tags':
                    isok, result = insert_itemtag(item=item, taglist=entry[k])
                    if not isok:
                        problementry.append({'msg': result, 'content': entry})
                        item.delete()
                        break
                elif fname == 'notes':
                    isok, result = insert_itemnote(item=item, note=entry[k])
                    if not isok:
                        problementry.append({'msg': result, 'content': entry})
                        item.delete()
                        break
                else:
                    isok, result = insert_itemdata(item=item, fieldname=fname, itemtype=itemtype, value=entry[k])
                    if not isok:
                        problementry.append({'msg': result, 'content': entry})
                        item.delete()
                        break
            elif ftype == 'creators':
                isok, result = insert_creator(fieldname=fname, item=item, itemtype=itemtype, value=entry[k])
                if not isok:
                    problementry.append({'msg': result, 'content': entry})
                    item.delete()
                    break
        for k in entry:
            isok, result = getfieldtype(k)
            if isok:
                ftype, fname = result
            else:
                problementry.append({'msg': result, 'content': entry})
                item.delete()
                break
            if ftype == 'attachments':
                # pass
                # Should revise!!
                for ifile in entry[k]:
                    #                    filepath = os.path.join(os.path.dirname(risfile),ifile)
                    #                    isok,result = insert_attachment(fieldname=fname,item=item,filepath=filepath)
                    isok = True
                    result = 'Cant insert attachments'
                    if not isok:
                        problementry.append({'msg': result, 'content': entry})
                        item.delete()
                        break
            elif (ftype != 'field') and (ftype != 'creators'):
                if not isok:
                    problementry.append({'msg': result, 'content': entry})
                    item.delete()
                    break

        successentry.append(item)
    msg.append('Import Item from RIS File, Total Item Number: ' + str(totalitem))
    msg.append('Error Import Number: ' + str(len(problementry)))
    print('msg', msg, '\nsuccessentry', successentry, '\nproblementry', problementry)
    return msg, successentry, problementry


class CreatorType(models.Model):
    creatortype = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.creatortype


# class CreatorData(models.Model):
#    firstname = models.CharField(max_length=200)
#    lastname = models.CharField(max_length=200)
#    def __unicode__(self):
#        return ' '.join([self.firstname,self.lastname])

# Problem: People with same name?
class Creator(models.Model):
    # creatordata = models.OneToOne(CreatorData)
    firstname = models.CharField(max_length=200, blank=True, null=False, default='')
    lastname = models.CharField(max_length=200)
    dateadded = models.DateTimeField('create date', auto_now_add=True)
    datemodified = models.DateTimeField('last modified', auto_now=True)

    # key = models.CharField(max_length=200, unique=True)
    def __unicode__(self):
        return ' '.join([self.firstname, self.lastname])


class Field(models.Model):
    fieldname = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.fieldname


# File model
class FileType(models.Model):
    filetype = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.filetype


class FileTypeMimeType(models.Model):
    filetype = models.ForeignKey(FileType, on_delete=models.CASCADE, )
    mimetype = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.mimetype


# Item model
class ItemType(models.Model):
    typename = models.CharField(max_length=200, unique=True)
    display = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.typename


class ItemTypeField(models.Model):
    itemtype = models.ForeignKey(ItemType, on_delete=models.CASCADE, )
    field = models.ForeignKey(Field, on_delete=models.CASCADE, )
    orderindex = models.PositiveSmallIntegerField()


class ItemTypeCreatorType(models.Model):
    itemtype = models.ForeignKey(ItemType, on_delete=models.CASCADE, )
    creatortype = models.ForeignKey(CreatorType, on_delete=models.CASCADE, )
    primaryfield = models.PositiveSmallIntegerField()


# class ItemDataValue(models.Model):
#    value = models.TextField()

class Item(models.Model):
    itemtype = models.ForeignKey(ItemType, on_delete=models.CASCADE, )
    dateadded = models.DateTimeField('create date', auto_now_add=True)
    datemodified = models.DateTimeField('last modified', auto_now=True)
    key = models.CharField(max_length=200, unique=True)

    def title(self):
        fieldname = 'title'
        titlefield = Field.objects.get(fieldname=fieldname)
        title = self.itemdata_set.filter(field=titlefield)
        if len(title) == 1:
            return title[0].value
        else:
            return ''

    def creator(self):
        creatorlist = []
        for i in self.itemcreator_set.all():
            creatorlist.append(' '.join([i.creator.firstname, i.creator.lastname]))

        return creatorlist

    def __unicode__(self):
        return '/'.join([self.itemtype.typename, self.title()])


class ItemData(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    field = models.ForeignKey(Field, on_delete=models.CASCADE, )
    #    value = models.ForeignKey(ItemDataValue)
    value = models.TextField()

    def __unicode__(self):
        return self.field.fieldname + ': ' + self.value


class ItemCreator(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, )
    creatortype = models.ForeignKey(CreatorType, on_delete=models.CASCADE, )
    orderindex = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return str(self.item.id)


class Collection(models.Model):
    collectionname = models.CharField(max_length=200, unique=True)
    parentcollection = models.ForeignKey('self', blank=True, on_delete=models.CASCADE, )
    dateadded = models.DateTimeField('create date', auto_now_add=True)
    datemodified = models.DateTimeField('last modified', auto_now=True)
    key = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.collectionname


class CollectionItem(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, )
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    orderindex = models.PositiveSmallIntegerField()


class DeletedItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    datedeleted = models.DateTimeField('deleted date', auto_now_add=True)

    def __unicode__(self):
        return str(self.item.id)


def itemattachment_filename(instance, filename):
    namelist = []
    author_list = instance.item.itemcreator_set.all()
    authorname_list = [author.creator.lastname for author in author_list]
    if len(authorname_list) > 2:
        authorname = authorname_list[0] + ' et al.'
        namelist.append(authorname)
    elif (len(authorname_list) == 2) or (len(authorname_list) == 1):
        authorname = ' and '.join(authorname_list)
        namelist.append(authorname)

    datefield = Field.objects.get(fieldname='date')
    date = instance.item.itemdata_set.filter(field=datefield)
    for idate in date:
        try:
            ftime = time.strptime(idate.value, '%Y/%m/%d/')
            year = str(ftime.tm_year)
            namelist.append(year)
            break
        except:
            continue

    titlefield = Field.objects.get(fieldname='title')
    title = instance.item.itemdata_set.filter(field=titlefield)
    if title:
        namelist.append(title[0].value)
    else:
        titlefield = Field.objects.get(fieldname='shortTitle')
        title = instance.item.itemdata_set.filter(field=titlefield)
        if title:
            namelist.append(title[0].value)

    if not namelist:
        namelist.append('Unknown')
    filetype = filename.split('.')
    if filetype[-1] == 'gz':
        filetype = '.'.join(filetype[-2:])
    else:
        filetype = filetype[-1]
    namelist = map(safepath, namelist)
    newname = '-'.join(namelist) + '.' + filetype
    return os.path.join('literature/attachments', instance.item.key, newname)


class ItemAttachment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    sourceitem = models.ForeignKey(Item, related_name='+', on_delete=models.CASCADE, )
    attachment = models.FileField(upload_to=itemattachment_filename)
    mimetype = models.CharField(max_length=200)

    # ?? filetype
    def __unicode__(self):
        return str(self.item.id)


def attachment_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    filename = instance.attachment.path
    instance.attachment.delete(False)
    dirpath = os.path.dirname(filename)
    fatherpath = os.path.basename(dirpath)
    if fatherpath == instance.item.key:
        try:
            os.rmdir(dirpath)
        except:
            pass


models.signals.post_delete.connect(attachment_delete, sender=ItemAttachment)


class ItemNote(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField('Content')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    sourceitem = models.ForeignKey(Item, related_name='+',
                                   on_delete=models.CASCADE, )  # maybe don't delete along the source item

    def __unicode__(self):
        return str(self.item.id)


# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    tagtype = models.PositiveSmallIntegerField(default=1)
    dateadded = models.DateTimeField('create date', auto_now_add=True)
    datemodified = models.DateTimeField('last modified', auto_now=True)

    # key = models.CharField(max_length=200, unique=True)
    def __unicode__(self):
        return self.name


class ItemTag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, )
