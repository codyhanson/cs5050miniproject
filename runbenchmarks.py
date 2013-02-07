#! /usr/bin/env python
#use python 2.7.x

#This script will be invoked periodically as a Cron job.
#It will invoke various benchmark binaries and direct their output to files
#prefixed with a timestamp for this testrun

import datetime
import sys
import os

#get the current timestamp, which will identify this benchmark run
#same as datetime.now(none)
timestamp = datetime.datetime.today() #unsure if need to worry about timezones or not



#os.execv or os.execl can be used to invoke executeables with arguments
#still figuring out how to redirect their output to a file


#Check /proc/cpuinfo and record the output
os.execv('/bin/cat',['/bin/cat','/proc/cpuinfo'])

#run IOZONE



#run iperf




#run STREAM



#run SPECCPU2006



print "hello!"
