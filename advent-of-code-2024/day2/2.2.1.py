from collections import deque

def read_to_list(filepath):
    with open(filepath) as file:
        return file.read().split("\n")

def report_handler(content):
    total = 0
    for line in content:
        report = list(map(int, line.split(" ")))
        total += check_report(report)
    return total
    
def check_report(report):
    print("\n" + 50*"=")
    if validate_report(report):
        return 1
    else:
        for i in range(0, len(report)):
            if validate_report(report[:i]+report[i+1:]):
                return 1
    return 0

def validate_report(report):
    if report == sorted(report,reverse=False):
            return check_levels(report)
    elif report == sorted(report,reverse=True):
        return check_levels(report[::-1])
    return 0

def check_levels(report):
    working_report = report
    print("")
    print(working_report)
    while len(working_report) > 1:
        working_report = deque(map(lambda x : x - working_report[0], working_report))
        working_report.popleft()
        print(working_report)
        if not _validate_levels(working_report[0]):
            return 0
    return 1

def _validate_levels(num):
    return num in {1,2,3}

def solver():
    return \
    report_handler(
        read_to_list("input.txt")
    )