from glob import glob
import dateutil.parser

# Available benchmarks
benchmarks = ['bt', 'cg', 'ft', 'is', 'lu', 'mg', 'sp', 'ua']
benchmark_class = 'W'


def extractDate(filename):
    parts = filename.split('-')
    return "20{0}-{1}-{2}T{3}:{4}:00".format(parts[2], parts[0], parts[1], parts[3], parts[4])

def parseFile(filename):

    time = None
    mops = None

    with open(filename) as file:
        for line in file:
            if "Time in seconds" in line:
                time = line.split("=")[1].lstrip().rstrip()
            elif "Mop" in line:
                mops = line.split("=")[1].lstrip().rstrip()

    return time, mops

def writeSummary(benchmark, benchmark_class, benchmark_results):
    summary_file_name = "{0}_{1}.csv".format(benchmark, benchmark_class)
    with open(summary_file_name, 'w') as summary_file:
        summary_file.write("run time,execution length,total mop/s\n")
        for time_stamp in sorted(benchmark_results.iterkeys()):
            execution_results = benchmark_results[time_stamp]
            summary_file.write("{0},{1},{2}\n".format(time_stamp, execution_results["execution_time"], execution_results["total_mops"]))


for benchmark in benchmarks:
    benchmark_results = {}
    for file_name in glob("*-NASA-{0}.{1}.x.txt".format(benchmark, benchmark_class)):
        time_stamp =  extractDate(file_name)
        execution_time, mops = parseFile(file_name)
        time_stamp_value = dateutil.parser.parse(time_stamp)
        execution_results = {}
        execution_results["execution_time"] = execution_time
        execution_results["total_mops"] = mops
        benchmark_results[time_stamp_value] = execution_results
    writeSummary(benchmark, benchmark_class, benchmark_results)

