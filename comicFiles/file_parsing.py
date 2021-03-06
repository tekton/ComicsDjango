import os
import re
from comicFiles.models import ComicFile, ComicReadAndOwn, RootFolder
from comicFiles.models import TransferRoot
from comicFiles.images import thumbnail_parse_task

import celery

from shutil import copy2
###
from difflib import unified_diff

import ast


def x(start_path):
    full_folder = []

    try:
        # check to make sure path is valid
        if not os.path.isdir(start_path):
            return False
    except Exception as e:
        print(e)
        return False

    for root, dirs, files in os.walk(start_path):
        for file in files:
            full_folder.append(os.path.join(root, file))
    print(full_folder)
    return full_folder


def diff_check(y, z):
    files = []
    for line in unified_diff(y, z):
        if line.startswith("+"):
            if not line.startswith("+++"):
                files.append(line.lstrip("+"))
    return files
###


@celery.task
def procFolder(folder_path, old_value, rootFolder, check_override=False):
    b = x(folder_path)
    try:
        if not old_value:
            old_value = []
    except:
        old_value = []
    files_to_parse = diff_check(old_value, b)
    for f in files_to_parse:
        folder = os.path.dirname(f)
        file_name = os.path.basename(f)
        parse_file.delay(folder, file_name, rootFolder, check_override=check_override)
    return b


@celery.task
def parse_file(FOLDER, FILE, rootFolder, date="", check_override=False):
    # file = open(FILE.RootFolder+"/"+FILE.name+"."+FILE.extension)
    regex = "(.*?)[\(\[](.*)"
    regex2 = "(.*)[\s_](\d+)"
    parse_file = FILE.replace("_", " ")
    # should really only get files with the way it's done now...
    # print(date + " :: " + FILE)
    # CHECK TO SEE IF FILE IS IN DB!
    extension = os.path.splitext(FILE)[1][1:]
    # print(extension)
    ignore_ext_set = set(["txt", "com", "com.txt", "part"])
    if extension in ignore_ext_set:
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
        # return False
    else:
        print("No exceptions, but there was a file already in there...")
        if check_override is False:
            print("...override is false, don't parse")
            return
        else:
            print("override is true, please parse")

    # IT ISN'T?! Then lets start parsing!
    file_parse = re.match(regex, parse_file)
    if file_parse:
        # DO STUFF
        # print(file_parse.group(1))
        f.comic_name = file_parse.group(1)
        # print(file_parse.group(2))
        number_parse = re.match(regex2, file_parse.group(1))
        if number_parse:
            f.comic_name = number_parse.group(1)
            f.comic_issue = number_parse.group(2)
            # print(number_parse.group(1) + " :: " + number_parse.group(2))
    f.extension = extension
    f.save()
    #    file_parse = re.match(regex2, FILE)
    #    if file_parse:
    # do more stuff
    #        print(file_parse)
    # now that the file is saved; add to image processing queue!
    thumbnail_parse_task.delay(f)


@celery.task
def re_parse_file(comic):
    """function will change over time as regex changes for other sections..."""
    print(comic)
    # date???
    #
    # name! -- since we didn't fix the _ problem in the initial import we'll fix it now...
    parse_file(comic.dir_path, comic.name, comic.rootFolder, comic.comic_date, True)
    #
    return


@celery.task
def parse_folder(FOLDER):
    # take the FOLDER object and assign out the variables to local renditions
    # folder = FOLDER.uri
    possible_date = None
    for dir_path, dir_names, files in os.walk(FOLDER.uri):
        # print(dir_path)
        date_regex = "(.*)(\d\d\d\d[\./-]\d\d[\./-]\d\d)(.*)"
        d = re.match(date_regex, dir_path)
        if d:
            possible_date = d.group(2)
        # print(dir_names)
        for name in files:
            if name != ".DS_Store":
                # print(os.path.join(dir_path,name))
                # print("DIR_PATH :: "+dir_path)
                # print("NAME :: " + name)
                # print("DATE :: "+possible_date)
                if "@eaDir" in dir_path:
                    # for ignoring synology nas "special" files
                    # TODO add this to settings, an outside conf, or a DB entry
                    pass
                else:
                    parse_file.delay(dir_path, name, FOLDER, possible_date)


@celery.task
def copy_file_to_transfer(comic):
    # print(comic.dir_path)
    # print(comic.name)
    orig = comic.dir_path + "/" + comic.name
    loc = TransferRoot.objects.get(status="primary")
    print(loc.uri)
    print(orig)
    copy2(orig, loc.uri)


@celery.task
def parsePrimaryFolder(check_override=False):
    print("parsePrimaryFolder")
    rootFolders = RootFolder.objects.filter(primary=True)
    for FOLDER in rootFolders:
        print(FOLDER)
        print(FOLDER.os_blob)
        if FOLDER.os_blob:
            folder_list = ast.literal_eval(FOLDER.os_blob)
        else:
            folder_list = None
        blob = procFolder(FOLDER.uri, folder_list, FOLDER, check_override)
        # parse_folder.delay(FOLDER)
        FOLDER.os_blob = blob
        FOLDER.save()


@celery.task
def toggleTrade(q):
    try:
        entry = ComicReadAndOwn.objects.get(pk=q)
    except Exception as e:
        print(e)
        return False
    entry.trade = not entry.trade
    entry.save()


def makeRootPrimary(ROOT):
    ROOT.primary = True
    try:
        ROOT.save()
        return True
    except Exception as e:
        print(e)
        print("Unable to set as primary")
        print(ROOT)
        return False
