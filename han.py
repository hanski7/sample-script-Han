import requests
import csv
import sys
import sched
import time

s=sched.scheduler(time.time, time.sleep)

def get_status(site):
    l = requests.head(site)
    return l.status_code

def get_site():
    f = open(sys.argv[1], 'r')
    reader = csv.reader(f)
    for row in reader:
        for ele in row:
            print ele, (get_status(ele))
    f.close()


s.enter(0,1,get_site, ())
s.enter(300,1,get_site, ())
s.enter(600,1,get_site, ())
s.enter(900,1,get_site, ())
s.enter(1200,1,get_site, ())
s.enter(1500,1,get_site, ())
s.enter(1800,1,get_site, ())
s.run()

