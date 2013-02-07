#! /usr/bin/env python
#use python 2.7.x

#This script will be invoked periodically as a Cron job.
#It will invoke various benchmark binaries and direct their output to files
#prefixed with a timestamp for this testrun

import datetime
#import sys not sure if need this
import os

#get the current timestamp, which will identify this benchmark run
#same as datetime.now(none)
timestamp = datetime.datetime.today() #unsure if need to worry about timezones or not
timestampFormatStr = "%m-%d-%y-%H_%M" #not sure if this is the format we want.

#Check /proc/cpuinfo and record the output
returncode = os.system("cat /proc/cpuinfo > results/{0}-cpuinfo.txt".format(timestamp.strftime(timestampFormatStr)))
#check returncode to make sure it worked ok
print "Return code for cat /proc/cpuinfo:{0}".format(returncode)

#run IOZONE
#Still need to figure out the options for iozone, they seem kind of complex
returncode = os.system("./benchmarks/iozone3_414/src/current/iozone > results/{0}-iozone.txt".format(timestamp.strftime(timestampFormatStr)))
print "Return code for iozone:{0}".format(returncode)

#run STREAM
#if the stream binary is not in, ./benchmarks/stream/ you will need to build it with make.
#stream_l precompiled binary doesnt seem to work, needs some other library
returncode = os.system("./benchmarks/stream/stream > results/{0}-stream.txt".format(timestamp.strftime(timestampFormatStr)))
print "Return code for stream:{0}".format(returncode)

#run iperf

#run SPECCPU2006


print "Tests completed"
