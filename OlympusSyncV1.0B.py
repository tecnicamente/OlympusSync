# -*- coding: utf-8 -*-

# Created on  05/05/2015
# @author: Tecnicamente
# License GPL3
# Version 1.0Beta

import urllib
import urllib2
import string
import sys

# TODO LIST
# =========
# 1. PARAMETERS CHECK
# 2. HELP MANIUAL
# 3. CONTROL FOR EXISTING ALREADY DOWNLOADE FILES
# 4. LOG FILE
# 5. EXTERNAL SETTING FILE
# 6. ROBUST ERRORS CHECK

# CONFIGURATION PARAMETERS
UrlToOpen = "http://oishare/DCIM/100OLYMP"
# END


try:
    OlympusHost = urllib2.urlopen(UrlToOpen)
    print ">>	" +UrlToOpen + " open"

except:
    print ">>	An error occured"

#except URLError, e:
#    print "An error occured"
#    print e.reason

imagesName = []
rowNumber = 0

row = OlympusHost.readline()

while row:
	rowComponents = row.split(",")

	if "/DCIM/100OLYMP" in row:
		imagesName.append(rowComponents[1])
		numberOfImages = len(imagesName)
		
	rowNumber = rowNumber + 1
	row = OlympusHost.readline()

#print imagesName # DEBUG

print ">>	Found " + str(numberOfImages) + " images on the device"

page = urllib2.urlopen('http://192.168.0.10/DCIM').read()
for i in range(numberOfImages):
#	image = urllib2.urlopen("http://oishare/DCIM/100OLYMP/FILE.html?/DCIM/100OLYMP/"+(imagesName[i]))
#	outputFile = open("/tmp/"+imagesName[i], "wb")
#	outputFile.write(image.read())
#	outputFile.close()

	source = "http://oishare/DCIM/100OLYMP/" + imagesName[i]
	destination = "/tmp/" + imagesName[i]
	print ">>	" + source + " ---> " + destination
	urllib.urlretrieve(source ,destination)
	print ">> Image " + imagesName[i] + " downloaded"

print ">>	All files downloades"

OlympusHost.close()