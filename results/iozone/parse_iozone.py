import dateutil.parser
from glob import glob
import re


# Parses a line from a report file and organizes it according to data size, then record size, then time stamp
# The data is a dictionary (data sizes) of a dictionary (of record sizes) of a dictionary (time stamps)
def add_to_dict(time_stamp, line):
    parts = line.split()
    d_size = int(parts[0])
    r_size = int(parts[1])
    time_stamp_value = dateutil.parser.parse(time_stamp)

    record_sizes = data_sizes.get(d_size, {})
    time_stamps = record_sizes.get(r_size, {})
    time_stamps[time_stamp_value] = time_stamp + " " + line
    record_sizes[r_size] = time_stamps
    data_sizes[d_size] = record_sizes

# Global variables
regex = re.compile(r"\A\d+.")
data_sizes = {}
reports = {}
summary_file_name = "iozone-summary.txt"
summary_file_header_1 = "                                                                    random  random    bkwd   record   stride\n"
summary_file_header_2 = "                    KB  reclen   write rewrite    read    reread    read   write    read  rewrite     read   fwrite frewrite   fread  freread\n"

# Get all the report files
for file in glob('*-iozone.txt'):
    parts = file.split('-')
    time_stamp = "20" + parts[2] + "-" + parts[0] + "-" + parts[1] + "T" + parts[3] + ":" + parts[4] + ":00"
    reports[file] = time_stamp

# Parse each file and extract the data lines
for report_file_name in sorted(reports.iterkeys()):
    print 'Parsing file:', report_file_name
    with open(report_file_name) as report_file:
        lines = (l.lstrip() for l in report_file)
        matches = ((regex.search(l), l) for l in lines)
        for m in matches:
            if m[0]:
                add_to_dict(reports[report_file_name], m[1])

# Write out a summary report with the combined data
with open(summary_file_name, 'w') as summary_file:
    summary_file.write(summary_file_header_1)
    summary_file.write(summary_file_header_2)
    for data_size_value in sorted(data_sizes.iterkeys()):
        record_sizes = data_sizes[data_size_value]
        for record_size_value in sorted(record_sizes.iterkeys()):
            time_stamps = record_sizes[record_size_value]
            for time_stamp_value in sorted(time_stamps.iterkeys()):
                summary_file.write(time_stamps[time_stamp_value])




