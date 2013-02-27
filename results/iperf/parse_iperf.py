#! /usr/bin/env python

import dateutil.parser
from glob import glob
import re

#match the line where the throughput number is in an iperf output
tputpattern = re.compile('(\d\.\d\d) Mbits/sec')

for file in glob('*-iperf.txt'):
    #parts = file.split('-')
    #time_stamp = "20" + parts[2] + "-" + parts[0] + "-" + parts[1] + "T" + parts[3] + ":" + parts[4] + ":00"
    filehdl = open(file)
    iperfOutput = filehdl.read()
    match = re.search(tputpattern,iperfOutput)
    print file, match.group(1)
