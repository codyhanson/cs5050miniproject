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
timestampFormatStr = "%m-%d-%y-%H_%M" #not sure if this is the format we want.




#Check /proc/cpuinfo and record the output
returncode = os.system("cat /proc/cpuinfo > results/{0}-cpuinfo.txt".format(timestamp.strftime(timestampFormatStr)))

#check returncode to make sure it worked ok?
print returncode 

#run IOZONE



#run iperf




#run STREAM



#run SPECCPU2006



print "hello!"
