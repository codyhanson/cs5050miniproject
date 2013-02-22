#! /usr/bin/env python

#hash all the txt files and export their md5sum.
#for visual inspection to see if files are different

import hashlib
import glob

#dictionary of all the hashs we've seen
hashs = {}

files = glob.glob("*.txt")
for file in (files):
   handle = open(file) 
   filehash = hashlib.md5(handle.read()).hexdigest()
   if filehash in hashs:
       hashs[filehash].append(file)  
   else:
       hashs[filehash] = [file] #initialize the new list
      

for key in hashs.keys():
    print "Files with md5: {0}".format(key)
    for filename in hashs[key]:
        print filename

print "Number of different filehashs: {0}".format(len(hashs.keys()))
