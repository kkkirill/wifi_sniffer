#!usr/bin/python3
import re
import subprocess
import time
from datetime import datetime

import schedule

previous = []


def send_data(data):
    result = '\n'.join([datetime.now().strftime('%d.%m.%Y %H:%M:%S'), 'Devices (%s):' % len(data)] + data)
    print(result)


def scan_job():
    global previous
    scan = subprocess.Popen(['lanscan', 'scan'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    grep = subprocess.Popen(['grep', '-e', 'True'], stdin=scan.stdout, stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL)
    clear_grep = subprocess.Popen(['grep', '-v', '-e', '_gateway'], stdin=grep.stdout, stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL)
    output = [re.sub(r'\s+', ' ', line.decode()).strip() for line in clear_grep.stdout.readlines()]
    if output != previous:
        previous = output
        send_data(output)


schedule.every(5).seconds.do(scan_job)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    pass
