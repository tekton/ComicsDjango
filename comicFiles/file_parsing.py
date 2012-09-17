import os
import re
from comicFiles.models import ComicFile
from comicFiles.models import RootFolder


def parse_file(FOLDER, FILE, date=""):
    #file = open(FILE.RootFolder+"/"+FILE.name+"."+FILE.extension)
    regex   =   "(.*?)[\(\[](.*)";
    regex2  =   "(.*)\s(\d+)";
    ### should really only get files with the way it's done now...
#    print date + " :: " + FILE
    ### CHECK TO SEE IF FILE IS IN DB!
    
    extension = os.path.splitext(FILE)[1][1:]
    print extension
    
    try: 
        print "checking for db item..."
        ComicFile.objects.get(name=FILE,dir_path=FOLDER)
    except ComicFile.DoesNotExist:
        print "No Object exist...that's good!"
#        return False
    else:
        print "No exceptions, but there was a file already in there, so no processing!"
        return
    
    f = ComicFile(name=FILE,dir_path=FOLDER,comic_date=date)
    
    ##IT ISN'T?! Then lets start parsing!
    file_parse = re.match(regex, FILE)
    if file_parse:
        # DO STUFF
        #print file_parse.group(1)
        f.comic_name = file_parse.group(1)
        #print file_parse.group(2)
        number_parse = re.match(regex2, file_parse.group(1))
        if number_parse:
            f.comic_name = number_parse.group(1)
            f.comic_issue = number_parse.group(2)
            #print number_parse.group(1) + " :: " + number_parse.group(2)
    f.save()
#    file_parse = re.match(regex2, FILE)
#    if file_parse:
#        #do more stuff
#        print file_parse

def parse_folder(FOLDER):
    ### take the FOLDER object and assign out the variables to local renditions
    ### folder = FOLDER.uri
    possible_date = None
    for dir_path,dir_names,files in os.walk(FOLDER.uri):
        #print dir_path
        date_regex = "(.*)(\d\d\d\d[\./-]\d\d[\./-]\d\d)(.*)"
        d = re.match(date_regex,dir_path)
        if d:
            possible_date = d.group(2)
        #print dir_names
        for name in files:
            if name != ".DS_Store":
                #print os.path.join(dir_path,name)
                parse_file(dir_path, name, possible_date)