import os
import re
import zipfile
import rarfile

import PIL
from PIL import Image

from django.conf import settings

#dir_root = "/Users/tyler/Projects/Comics/static/comics/Week of 2012-06-20/DC"
#img_root = settings.IMG_ROOT

def rar_parse(dir_path,name):
	img_root = settings.IMG_ROOT
	r = rarfile.RarFile(dir_path+"/"+name)
	try:
		r.extract(r.namelist()[0],img_root)
	except:
		print "No unrar image for you..."
	f_name = str(r.namelist()[0]).replace("\\","/")
	return thumbnail_create(f_name)
	
def zip_parse(dir_path,name):
	img_root = settings.IMG_ROOT
	z = zipfile.ZipFile(dir_path+"/"+name)
	try:
		z.extract(z.namelist()[0],img_root)
	except:
		print "No unzipped image for you!"
	### don't need to edit the rar directory seperator
	return thumbnail_create(z.namelist()[0])
	
def thumbnail_create(f_name):
	img_root = settings.IMG_ROOT
	if os.path.isfile(img_root+"/"+f_name):
		print "should resize it to a real thumbnail..."
	
		try:
			img = Image.open(img_root+"/"+f_name)
		except:
			print "no img?!"
	
		basewidth = 200
		wpercent = (basewidth / float(img.size[0]))
		hsize = int((float(img.size[1]) * float(wpercent)))
		img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
		img.save(img_root+"/"+f_name)
		return f_name
	else:
		print "Can't find the image that should have been extracted..."
		return False

def walkit():
	for dir_path,dir_names,files in os.walk(dir_root):
		for name in files:
			extension = os.path.splitext(name)[1][1:]
			z = zipfile
			r = rarfile
		
			if extension == "cbz":
				print "process as zip!"
				if z.is_zipfile(name):
					z = zipfile.ZipFile(name)
					#for a in z.namelist():
						#print a
					print z.namelist()[0]
				
					z.extract(z.namelist()[0],img_root)
					print "zip: "+str(z.namelist()[0])
					if os.path.isfile(img_root+z.namelist()[0]):
						print "should resize it to a real thumbnail..."
				else:
					print "not a zip..."
			elif extension == "cbr":
				print "process as rar!"
				if r.is_rarfile(name):
					print "rar to process"
					r = rarfile.RarFile(name)
					print r.namelist()[0]
					#print r.infolist()[0]
					#for f in r.infolist():
					#	print f.filename, f.file_size
					#	r.extract(f)
				
					#### TODO: check to see if the file exists and if we need to make a thumbnail...
				
					try:
						r.extract(r.namelist()[0],img_root)
						print "rar: "+str(r.namelist()[0])
					except:
						print "No image for you..."
					
					f_name = str(r.namelist()[0]).replace("\\","/")
					if os.path.isfile(img_root+f_name):
						print "should resize it to a real thumbnail..."
					
						try:
							img = Image.open(img_root+f_name)
						except:
							print "no img?!"
					
						basewidth = 160
						wpercent = (basewidth / float(img.size[0]))
						hsize = int((float(img.size[1]) * float(wpercent)))
						img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
						img.save(img_root+f_name+".jpg")
					

					'''
					try:
						r.extract(r.namelist()[0],"./images")
					except:
						print "extraction failed..."
					'''