""" NOT WORKING """
import urllib
import urllib2

""" CONFIGURATION PARAMETERS """

UrlToOpen = "http://oishare/DCIM/100OLYMP"

""" END						 """
import string
import sys
import urllib2

try:
    OlympusHost = urllib2.urlopen(UrlToOpen)
    print ">>	" +UrlToOpen + " open"
    """ DEBUG """

except:
    print ">>	An error occured"

"""
except URLError, e:
    print "An error occured"
    print e.reason
"""


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

print imagesName # DEBUG

print ">>	Found " + str(numberOfImages) + " images on the device"

for i in range(numberOfImages):
	image = urllib2.urlopen("http://oishare/DCIM/100OLYMP/FILE.html?/DCIM/100OLYMP/"+(imagesName[i]))
#	outputFile = open("/tmp/"+imagesName[i], "wb")
#	outputFile.write(image.read())
#	outputFile.close()
	source = "http://oishare/DCIM/100OLYMP/FILE.html?/DCIM/100OLYMP/" + imagesName[i]
	destination = "/tmp/" + imagesName[i]
	urllib.urlretrieve(source ,destination)
	print ">> Image " + imagesName[i] + " downloaded"

print ">>	All files downloades"

OlympusHost.close()