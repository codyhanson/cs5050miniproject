#! /usr/bin/env python

#hash all the txt files and export their md5sum.
#for visual inspection to see if files are different

import hashlib
import glob

files = glob.glob("*.txt")
for file in (files):
   handle = open(file) 
   print "File: {0}, md5: {1}".format(file,hashlib.md5(handle.read()).hexdigest())
