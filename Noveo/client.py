#!/usr/bin/env python
import sys
import getopt
import requests

inputfile='file.txt'
destination='127.0.0.1'
try:
   opts, args = getopt.getopt(sys.argv[1:],"hi:d:",["ifile=","ddestination="])
except getopt.GetoptError:
   print 'client.py -i <inputfile> -d <destination address>'
   sys.exit(2)
for opt, arg in opts:
   if opt == '-h':
      print 'client.py -i <inputfile> -d <destiantion address>'
      sys.exit()
   elif opt in ("-i", "--ifile"):
      inputfile = arg
   elif opt in ("-d", "--destination"):
      destination = arg

data = open(inputfile, 'r')
url='http://' + destination
r = requests.post(url, data)
print (r.text)
