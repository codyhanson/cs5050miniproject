#! /usr/bin/env python
#use python 2.7.x

#This script will be invoked periodically as a Cron job.
#It will invoke various benchmark binaries and direct their output to files
#prefixed with a timestamp for this testrun

import datetime
import smtplib
import os

os.chdir('/home/ubuntu/cs5050miniproject')

#get the current timestamp, which will identify this benchmark run
#we will periodically refresh the timestamp for in between long running tests
#same as datetime.now(none)
timestamp = datetime.datetime.today() #unsure if need to worry about timezones or not
timestampFormatStr = "%m-%d-%y-%H_%M" #not sure if this is the format we want.

#set to indicate something went wrong, and fire off an email
error = False
retcodes = {}

#Check /proc/cpuinfo and record the output
returncode = os.system("cat /proc/cpuinfo > results/cpuinfo/{0}-cpuinfo.txt".format(timestamp.strftime(timestampFormatStr)))
#check returncode to make sure it worked ok
print "Return code for cat /proc/cpuinfo:{0}".format(returncode)
if (returncode != 0):
    error = True
retcodes["cpuinfo"] = returncode


#run STREAM
#if the stream binary is not in, ./benchmarks/stream/ you will need to build it with make.
#stream_l precompiled binary doesnt seem to work, needs some other library
timestamp = datetime.datetime.today() 
returncode = os.system("./benchmarks/stream/stream > results/stream/{0}-stream.txt".format(timestamp.strftime(timestampFormatStr)))
print "Return code for stream:{0}".format(returncode)
if (returncode != 0):
    error = True
retcodes["stream"] = returncode

#run iperf
#connect as a client to another machine running the server.
#port 5001 
iperfServer = "ec2-54-234-43-118.compute-1.amazonaws.com"
timestamp = datetime.datetime.today() 
returncode = os.system("iperf -c {1} > results/iperf/{0}-iperf.txt".format(timestamp.strftime(timestampFormatStr), iperfServer))
print "Return code for iperf client:{0}".format(returncode)
if (returncode != 0):
    error = True
retcodes["iperf"] = returncode

#run NASA benchmarks 
nasapath = "../nasa/NPB3.3.1/NPB3.3-SER/bin/"
nasabenchmarks = ["bt.W.x","cg.W.x","ft.W.x","is.W.x","lu.W.x","mg.W.x","sp.W.x","ua.W.x"]

for bench in (nasabenchmarks):
    timestamp = datetime.datetime.today() 
    returncode = os.system("{1}{2} > results/nasa/{0}-NASA-{2}.txt".format(timestamp.strftime(timestampFormatStr),nasapath,bench))
    print "Return code for nasa benchmark {1}:{0}".format(returncode,bench)
    if (returncode != 0):
        error = True
    retcodes[bench] = returncode

#run IOZONE
# -a is 'shorter' auto mode. -R outputs a summary in excel format
timestamp = datetime.datetime.today() 
returncode = os.system("./benchmarks/iozone3_414/src/current/iozone -a -R > results/iozone/{0}-iozone.txt".format(timestamp.strftime(timestampFormatStr)))
print "Return code for iozone:{0}".format(returncode)
if (returncode != 0):
    error = True
retcodes["iozone"] = returncode

error = True #always send email for now
if (error):
    #send email in case of an error
    FROM = 'uccsawsbench@gmail.com'

    #read our pw from a file
    fhandle = open('/home/ubuntu/pwfile')
    pw = fhandle.read()

    TO = 'chanson@uccs.edu'
    # Send the mail
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(FROM, pw)
    header = 'To:' + TO + '\n' + 'From: ' + FROM + '\n' + 'Subject:AWS bench error\n'
    msg = header + '\n'
    for key in retcodes:
       msg = msg + "Test:{0}, retcode{1}\n".format(key,retcodes[key]) 
    smtpserver.sendmail(FROM, TO, msg)
    smtpserver.close()
    print "error email sent"

print "Tests completed"
