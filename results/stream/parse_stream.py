#! /usr/bin/env python

#extract memory bandwidth and latency from Stream benchmarks

#import dateutil.parser
from glob import glob
import re

values = {}

pattern = re.compile('Copy:\s+([\d\.]+)\s+([\d\.]+)')

for file in glob('*.txt'):
    latency = 0
    bwidth = 0
    parts = file.split('-')
    time_stamp = "20" + parts[2] + "-" + parts[0] + "-" + parts[1] + "T" + parts[3] + ":" + parts[4] + ":00"
    time_stamp = dateutil.parser.parse(time_stamp)
    filehdl = open(file)
    streamoutput = filehdl.read()
    match = re.search(pattern,streamoutput)
    if (match != None):
        latency = float(match.group(2))
        bwidth = float(match.group(1))
        print file, bwidth, latency 
    else:
        print file, 'no match'

    values[time_stamp] = [bwidth,latency]


outFile = open('stream-summary.csv','w')

for key in (sorted(values.keys())):
    line = "{0}, {1}, {2}\n".format(key,values[key][0],values[key][1])
    outFile.write(line)


