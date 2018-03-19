# Mobin Anandwala
# 02/05/2017
# This script will generate a list of voltages starting at 6 V
# It will then log these voltages to a csv file
# Current will be calculated based on a gain of 100 for an op amp circuit
# current will be logged to that csv file

import csv
import datetime as dt
import time
from time import sleep

low_current = 3
medium_current = 20
high_current = 90
voltage = list(range(6,0,-1))
date = dt.date.today()

def generate_log_filename(date):
    filename = 'SafeLog-' + str(date) + '.csv'
    return filename

filename = generate_log_filename(date)

def initialize_log(filename):
    log = open(filename,'w')
    log_writer = csv.writer(log)
    log_writer.writerow(['Time,Voltage,Notes'])
    log.close()

initialize_log(filename)

def Log_Voltage(filename,voltage):
    log = open(filename,'a',newline='')
    log_writer = csv.writer(log)
    for i in voltage:
        if i <=len(voltage)-1:
            log_writer.writerow([str(dt.datetime.now),voltage[i],'Test'])
        else:
            break
    log.close()

Log_Voltage(filename,voltage)
