# -*- coding: utf-8 -*-

# Created on  05/05/2015
# @author: Tecnicamente
# License GPL3
# Version 1.1Beta

import urllib
import urllib2
import string
import sys
import getopt

# TODO LIST
# =========
# 1. PARAMETERS CHECK
# 2. HELP MANIUAL
# 3. CONTROL FOR EXISTING ALREADY DOWNLOADE FILES
# 4. LOG FILE
# 5. EXTERNAL SETTING FILE
# 6. ROBUST ERRORS CHECK
# 7. INCREMAENTAL COUNTWER AND  % OF DOWNLOAD

# VERSION LIST
# ============
# 1.0Beta 
#first running concept
# 1.1Betta
# + Error management wifi connection

# CONFIGURATION PARAMETERS
UrlToOpen = "http://oishare/DCIM/100OLYMP"
StringToSearch = "/DCIM/100OLYMP"
WiFiCameraName = "E-M10 WiFi"
# END

# FUNCTIONS
def StartConnection(url):
	try:
		OlympusHost = urllib2.urlopen(UrlToOpen)
		print ">>[INFO]	" +UrlToOpen + " open"
		return OlympusHost

	except IOError, e:
		print '>>[ERROR]	Failed to open the connection to ' + WiFiCameraName
		if hasattr(e, 'code'):
				print '>>[ERROR]	We failed with error code - ' + e.code
		elif hasattr(e, 'reason'):
				print ">>[ERROR]	The error object has the following 'reason' attribute :"
				print ">>[ERROR]	" + str(e.reason)
				print ">>[ERROR]	This usually means the server doesn't exist or is down."
		exit()

def Warning(par):
	print ">>[WARNING]	" + par[0] + ": " + "missing parameter"
	print ">>[WARNING]	Usage: " + par[0] + " [OPTION]"
	print ">>[WARNING]	"
	print ">>[WARNING]	Try " + par[0] + " '-h' for support"
	sys.exit(2)

def Help():
	#print '>>[HELP]	"-v" or "--verbose"	: verbose output, the parameter will show alla data managed by the software'
	print '>>[HELP]	"-h" or "--help"	:help indication, the parameter will print the help indications'
	print '>>[HELP]	"-d" or "--destination="	: output directory, the parameter will define where store the output files'
	print '>>[HELP]	"-j" or "--jpeg"	: download only .JPG files'
	print '>>[HELP]	"-o" or "--orf"		: download only .ORF files'
	#print '>>[HELP]	"-s" or "--split"	: save .JPG and .ORF in separate JPG and ORF directory'
	#print '>>[HELP]	"-f" or "--force"	: overwrite the existing files in the destination directory'
	#print '>>[HELP]	"-c" or "--choose"	: choose a specific file to download'
	#print '>>[HELP]	"-r" or "--release"	: print software release
	print '>>[HELP] "-l" or "--list"	: print file list prensent on the device'
	print '>>[HELP] "-L" or "--last="	: download last <n> images'
	return
	
def CheckParameter(par):
# quando la funzione viene chiamata le si deve passare il comando "sys.argv"
# Allowed parameters:
# "-v": verbose output, the parameter will show alla data managed by the software
# "-h":	help indication, the parameter will print the help indications
# "-d": output directory, the parameter will define where store the output files
# "-j": download only .JPG files
# "-o": download only .ORF files
# "-s": save .JPG and .ORF in separate JPG and ORF directory
# "-f": overwrite the existing files in the destination directory
# "-c": choose a specific file to download
# "-r": print release
# Parameters priority:
# h, 
	if len(par)<2:
		Warning(par)
		sys.exit(2)
	else:
		try:
			options, args = getopt.getopt(par[1:], "vhd:josfcrlL:",["verbose","help","destination=","onlyjpg","onlyorf","splittype","overwrite","choose=","release","list","last="])
		except getopt.GetOptError:
			Warning(par)		
	return options
	
def showFileList(urlToOpen):
	OlympusHost = StartConnection(UrlToOpen)
	imagesName=[]
	row = OlympusHost.readline()
	while row:
		rowComponents = row.split(",")

		if StringToSearch in row:
			imagesName.append(rowComponents[1])
			numberOfImages = len(imagesName)
		
		rowNumber = rowNumber + 1
		row = OlympusHost.readline()
	
	print ">>	[INFO]	Found " + str(numberOfImages) + " images on the device"

	for i in range(numberOfImages):
		print ">>[INFO]	" + imagesName[i]
	return

###### MAIN #########
imagesName = []
rowNumber = 0
imagesDownloaded = 0
percentageDonwload = 0



options = CheckParameter(sys.argv)
#print options # DEBUG
for o,a in options:
	if o in ('-h','--help'):
		Help()
		sys.exit(2)
	if o in ('l','--list'):
		showFilelist(UrlToOpen)
		sys.exit(2)
	if o in ('-v','--verbose'):
		verboseValue = True
	else:
		verboseValue = False
	if o in ('-d','--destination'):
		destination = a
	else:
		print ">>[WARNING]	Please add destionation using '-d' or '--destionation='"
		sys.exit(2)
	if o in ('-j','-jpeg'):
		OnlyJpeg = True
	else:
		OnlyJpeg = False
	if o in ('-o','--orf'):
		OnlyOrf = True
	else:
		OnlyOrf = False
	if o in ('-s','--split'):
		SplitFile = True
	else:
		SplitFile = False
	if o in ('-f','--force'):
		Force = True
	else:
		Force = False
	if o in ('-c','--choose'):
		FileToDownload = a
	if o in ('r','--release'):
		printRelease()

	

OlympusHost = StartConnection(UrlToOpen)
		
row = OlympusHost.readline()
while row:
	rowComponents = row.split(",")

	if StringToSearch in row:
		imagesName.append(rowComponents[1])
		numberOfImages = len(imagesName)
		
	rowNumber = rowNumber + 1
	row = OlympusHost.readline()


print ">>	[INFO]	Found " + str(numberOfImages) + " images on the device"

page = urllib2.urlopen('http://192.168.0.10/DCIM/100OLYMP').read()
for i in range(numberOfImages):

	source = "http://oishare/DCIM/100OLYMP/" + imagesName[i]
	#destination = "/tmp/" + imagesName[i]
	destination = destination + imagesName[i]
	print ">>	[INFO]	" + source + " ---> " + destination
	urllib.urlretrieve(source ,destination)
	imagesDownloaded = imagesDownloaded + 1
	percentageDownload = double(imageDownloaded)/ len(numberOfImages)
	print ">>	[INFO]	Image " + imagesName[i] + " downloaded" + "(" + str(imagesDownloaded/numberOfImages) + ")"
	print ">>	[INFO]	Downloaded images:	" + str(imagesDownloaded)

print ">>	[INFO]	All files downloades"

OlympusHost.close()