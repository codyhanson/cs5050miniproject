#! /usr/bin/env python

import dateutil.parser
from glob import glob
import re

#match the line where the throughput number is in an iperf output
#not pretty, but it works
tputpatternMbit = re.compile('Bytes (.*?) Mbits/sec')
tputpatternKbit = re.compile('Bytes (.*?) Kbits/sec')

values = {}

for file in glob('*-iperf.txt'):
    tputval = 0
    parts = file.split('-')
    time_stamp = "20" + parts[2] + "-" + parts[0] + "-" + parts[1] + "T" + parts[3] + ":" + parts[4] + ":00"
    time_stamp = dateutil.parser.parse(time_stamp)
    filehdl = open(file)
    iperfOutput = filehdl.read()
    matchMbit = re.search(tputpatternMbit,iperfOutput)
    matchKbit = re.search(tputpatternKbit,iperfOutput)
    if (matchMbit != None):
        tputval = float(matchMbit.group(1))
        print time_stamp, tputval, 'mbit match'
    elif (matchKbit != None):
        tputval = float(matchKbit.group(1))/1000.0 #convert Kbits to Mbits
        print time_stamp, tputval, 'kbit match'
    else:
        print file, 'no match'

    values[time_stamp] = tputval


outFile = open('iperf-summary.csv','w')

for key in (sorted(values.keys())):
    line = "{0}, {1}\n".format(key,values[key])
    outFile.write(line)
