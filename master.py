#!/usr/bin/env python

import time
import datetime
import commands


def execute(command):
    status, output = commands.getstatusoutput(command)
    if status != 0:
        print('ERROR: Command %s gave status %s and output %s' %(command, status, output))
    else:
        print('INFO: This worked.')

while True:
    execute("/app/stockreport.py")
    # execute(loadreport.rb)
    time.sleep(60)

