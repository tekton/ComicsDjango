import os
#import re
import zipfile
import rarfile

import PIL
from PIL import Image

from django.conf import settings

from comicFiles.models import ComicFile

import celery

#### moving some image processing to tasks,  consolidating here
#from ratings.models import UserRating
#from issues.models import Series
#from issues.models import Comic
#from comicFiles.models import ComicFile
#from comicFiles.models import RootFolder

#dir_root = "/Users/tyler/Projects/Comics/static/comics/DC"
#img_root = settings.IMG_ROOT

"""
    TODO bug to investigate

    [2014-06-22 00:50:23,126: ERROR/MainProcess] Task comicFiles.images.thumbnail_parse_task[4c5d128b-2b80-4721-ab12-b7dba8d44acd] raised unexpected: TypeError("cannot concatenate 'str' and 'ZipInfo' objects",)
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/celery/app/trace.py", line 240, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/celery/app/trace.py", line 437, in __protected_call__
    return self.run(*args, **kwargs)
  File "/projects/Projects/ComicsDjango/comicFiles/images.py", line 67, in thumbnail_parse_task
    q.thumbnail = str(q.id) + "/" + zip_parse(q.dir_path, q.name, q.id)
  File "/usr/local/lib/python2.7/dist-packages/celery/app/trace.py", line 438, in __protected_call__
    return orig(self, *args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/celery/app/task.py", line 420, in __call__
    return self.run(*args, **kwargs)
  File "/projects/Projects/ComicsDjango/comicFiles/images.py", line 54, in zip_parse
    return thumbnail_create(z.infolist()[0], img_root)
  File "/projects/Projects/ComicsDjango/comicFiles/images.py", line 75, in thumbnail_create
    if os.path.isfile(img_root + "/" + f_name):
TypeError: cannot concatenate 'str' and 'ZipInfo' objects


-----


[2014-06-22 00:51:02,236: ERROR/MainProcess] Task comicFiles.images.thumbnail_parse_task[3bd5f035-f8ce-461f-aab3-254ce2c4fd9a] raised unexpected: TypeError("cannot concatenate 'str' and 'bool' objects",)
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/celery/app/trace.py", line 240, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/celery/app/trace.py", line 437, in __protected_call__
    return self.run(*args, **kwargs)
  File "/projects/Projects/ComicsDjango/comicFiles/images.py", line 65, in thumbnail_parse_task
    q.thumbnail = str(q.id) + "/" + rar_parse(q.dir_path, q.name, q.id)
TypeError: cannot concatenate 'str' and 'bool' objects

[2014-08-11 09:13:34,464: WARNING/Worker-8] No unrar image for you...
[2014-08-11 09:13:34,464: WARNING/Worker-8] Can't find the image that should have been extracted for:: page1.jpg
[2014-08-11 09:13:34,465: ERROR/MainProcess] Task comicFiles.images.thumbnail_parse_task[53e5cc84-e6f5-440c-8d9d-b5c71687736d] raised unexpected: TypeError("cannot concatenate 'str' and 'bool' objects",)
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/celery/app/trace.py", line 240, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/celery/app/trace.py", line 437, in __protected_call__
    return self.run(*args, **kwargs)
  File "/projects/Projects/ComicsDjango/comicFiles/images.py", line 111, in thumbnail_parse_task
    q.thumbnail = str(q.id) + "/" + rar_parse(q.dir_path, q.name, q.id)
TypeError: cannot concatenate 'str' and 'bool' objects

"""

"""
    IDEA: take the first item in the extracted folder as the image to get processed instead of the one from the zip/rar file given the stuff from home scanners are sometimes silly with the order they actually send things to get compressed
"""

@celery.task
def rar_parse(dir_path, name, num):
    img_root = settings.IMG_ROOT + "/" + str(num)
    print(img_root)
    r = rarfile
    if r.is_rarfile(dir_path + "/" + name):
        r = rarfile.RarFile(dir_path + "/" + name)
        try:
            r.extract(r.namelist()[0], img_root)
        except:
            print("No unrar image for you...")
        f_name = str(r.namelist()[0]).replace("\\", "/")
        ### todo: check for if the replace worked,  or for \ ???
        return thumbnail_create(f_name, img_root)
    else:
        print("Not actually a RAR :(")
        return False


@celery.task
def zip_parse(dir_path, name, num):
    img_root = settings.IMG_ROOT + "/" + str(num)
    z = zipfile
    if z.is_zipfile(dir_path + "/" + name):
        z = zipfile.ZipFile(dir_path + "/" + name)
        try:
            z.extract(z.infolist()[0], img_root)
        except:
            print("No unzipped image for you!")
        ### don't need to edit the rar directory seperator
        f_name = z.infolist()[0]
        return thumbnail_create(f_name, img_root)
    else:
        print("Not actually a zip :(")
        return False


@celery.task
def thumbnail_parse_task(i):
    """ q is used to represent a queryset item """
    #if q.thumbnail is None:

    try:
        q = ComicFile.objects.get(pk=i.id)
    except Exception as e:
        print("Unable to find comic file requested for thumbnail: ", e)

    if q.extension == "cbr":
        q.thumbnail = str(q.id) + "/" + rar_parse(q.dir_path, q.name, q.id)
    elif q.extension == "cbz":
        q.thumbnail = str(q.id) + "/" + zip_parse(q.dir_path, q.name, q.id)
    #else:
    #    print("Thumbnail already exist...most likely.")
    print("saving updated thumbnail location: ", q.thumbnail)
    try:
        q.save()
    except Exception as e:
        print("Unable to save thumbnail location: ", e)


def thumbnail_create(f_name, img_root):
    """
        Runs once the images are extracted to save on space

        Returns the image path or False if it fails
    """
    #img_root = settings.IMG_ROOT
    if os.path.isfile(img_root + "/" + f_name):
        print("should resize it to a real thumbnail...")

        try:
            img = Image.open(img_root + "/" + f_name)
        except:
            print("no img?!")
            return False

        basewidth = 200
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth,  hsize),  PIL.Image.ANTIALIAS)
        img.save(img_root + "/" + f_name)
        return f_name
    else:
        print("Can't find the image that should have been extracted for:: " + f_name)
        return False


def walkit(dir_root):
    img_root = ""
    for dir_path, dir_names, files in os.walk(dir_root):
        for name in files:
            extension = os.path.splitext(name)[1][1:]

            if extension == "cbz":
                z = zipfile
                print("process as zip!")
                if z.is_zipfile(name):
                    z = zipfile.ZipFile(name)
                    #for a in z.namelist():
                        #print(a)
                    print(z.namelist()[0])

                    z.extract(z.namelist()[0], img_root)
                    print("zip: " + str(z.namelist()[0]))
                    if os.path.isfile(img_root + z.namelist()[0]):
                        print("should resize it to a real thumbnail...")
                else:
                    print("not a zip...")
            elif extension == "cbr":
                r = rarfile
                print("process as rar!")
                if r.is_rarfile(name):
                    print("rar to process")
                    r = rarfile.RarFile(name)
                    print(r.namelist()[0])
                    #print(r.infolist()[0])
                    #for f in r.infolist():
                    #   print(f.filename,  f.file_size)
                    #   r.extract(f)

                    #### TODO: check to see if the file exists and if we need to make a thumbnail...

                    try:
                        r.extract(r.namelist()[0], img_root)
                        print("rar: " + str(r.namelist()[0]))
                    except:
                        print("No image for you...")

                    f_name = str(r.namelist()[0]).replace("\\", "/")
                    if os.path.isfile(img_root + f_name):
                        print("should resize it to a real thumbnail...")

                        try:
                            img = Image.open(img_root + f_name)
                        except:
                            print("no img?!")

                        basewidth = 160
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        img = img.resize((basewidth,  hsize),  PIL.Image.ANTIALIAS)
                        img.save(img_root + f_name + ".jpg")

                    '''
                    try:
                        r.extract(r.namelist()[0], "./images")
                    except:
                        print("extraction failed...")
                    '''
