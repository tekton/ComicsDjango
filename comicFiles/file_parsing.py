import os
import re
from comicFiles.models import ComicFile, ComicReadAndOwn, RootFolder
from comicFiles.models import TransferRoot
from comicFiles.images import thumbnail_parse_task

import celery

from shutil import copy2


@celery.task
def parse_file(FOLDER, FILE, rootFolder, date="", check_override=False):
    #file = open(FILE.RootFolder+"/"+FILE.name+"."+FILE.extension)
    regex = "(.*?)[\(\[](.*)"
    regex2 = "(.*)[\s_](\d+)"
    parse_file = FILE.replace("_", " ")
    ### should really only get files with the way it's done now...
    # print(date + " :: " + FILE)
    ### CHECK TO SEE IF FILE IS IN DB!
    extension = os.path.splitext(FILE)[1][1:]
    #print(extension)
    if extension == "txt":
        return False
    elif extension == "com":
        return False
    elif extension == "com.txt":
        return False
    '''
        Check the DB to see if we already parsed this one; don't if we already have
    '''

    try:
        print("checking for db item...")
        f = ComicFile.objects.get(name=FILE, dir_path=FOLDER)
    except ComicFile.DoesNotExist:
        print("No Object exist...that's good!")
        f = ComicFile(name=FILE, dir_path=FOLDER, comic_date=date, rootFolder=rootFolder)
        #return False
    else:
        print("No exceptions, but there was a file already in there...")
        if check_override is False:
            print("...override is false, don't parse")
            return
        else:
            print("override is true, please parse")

    ##IT ISN'T?! Then lets start parsing!
    file_parse = re.match(regex, parse_file)
    if file_parse:
        # DO STUFF
        #print(file_parse.group(1))
        f.comic_name = file_parse.group(1)
        #print(file_parse.group(2))
        number_parse = re.match(regex2, file_parse.group(1))
        if number_parse:
            f.comic_name = number_parse.group(1)
            f.comic_issue = number_parse.group(2)
            #print(number_parse.group(1) + " :: " + number_parse.group(2))
    f.extension = extension
    f.save()
#    file_parse = re.match(regex2, FILE)
#    if file_parse:
#        #do more stuff
#        print(file_parse)
    # now that the file is saved; add to image processing queue!
    thumbnail_parse_task.delay(f)


@celery.task
def re_parse_file(comic):
    """function will change over time as regex changes for other sections..."""
    print(comic)
    # date???
    #
    #name! -- since we didn't fix the _ problem in the initial import we'll fix it now...
    parse_file(comic.dir_path, comic.name, comic.rootFolder, comic.comic_date, True)
    #
    return


@celery.task
def parse_folder(FOLDER):
    ### take the FOLDER object and assign out the variables to local renditions
    ### folder = FOLDER.uri
    possible_date = None
    for dir_path, dir_names, files in os.walk(FOLDER.uri):
        #print(dir_path)
        date_regex = "(.*)(\d\d\d\d[\./-]\d\d[\./-]\d\d)(.*)"
        d = re.match(date_regex, dir_path)
        if d:
            possible_date = d.group(2)
        #print(dir_names)
        for name in files:
            if name != ".DS_Store":
                #print(os.path.join(dir_path,name))
                #print("DIR_PATH :: "+dir_path)
                #print("NAME :: " + name)
                #print("DATE :: "+possible_date)
                if "@eaDir" in dir_path:
                    ### for ignoring synology nas "special" files
                    ### TODO add this to settings, an outside conf, or a DB entry
                    pass
                else:
                    parse_file.delay(dir_path, name, FOLDER, possible_date)


@celery.task
def copy_file_to_transfer(comic):
    #print(comic.dir_path)
    #print(comic.name)
    orig = comic.dir_path + "/" + comic.name
    loc = TransferRoot.objects.get(status="primary")
    print(loc.uri)
    print(orig)
    copy2(orig, loc.uri)


@celery.task
def parsePrimaryFolder():
    rootFolders = RootFolder.objects.filter(primary=True)
    for FOLDER in rootFolders:
        parse_folder.delay(FOLDER)

@celery.task
def toggleTrade(q):
    try:
        entry = ComicReadAndOwn.objects.get(pk=q)
    except Exception as e:
        print(e)
        return False
    entry.trade = not entry.trade
    entry.save()