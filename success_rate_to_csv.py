import csv
import os
import datetime

#variables
filename = 'success_rate2019-08-12.csv'
rawcsv = 'success_rate_raw.csv'
finalcsv = 'success_rate_final.csv'
customer = 'atos-imo-tooling-prod'
date = datetime.datetime.now().strftime('%Y%m%d')


with open(filename, 'r') as fh:
    with open(rawcsv, 'w') as wf:
        for line in fh.readlines()[8:]:
            wf.write(line)
    wf.close()
fh.close()

with open(rawcsv, 'r') as nicecsv:
    with open(finalcsv, 'w') as fcsv:
        reader = csv.reader(nicecsv, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        writer = csv.writer(fcsv, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        header = 'Customer, ServerName, BkpStarted, BkpSuccess, BkpWarning, BkpError, Date'

        fcsv.write("%s\n" % header)
        for row in reader:
            line = customer, row[0], row[4],row[5],row[7],row[6],date
            writer.writerow(line)

fcsv.close()
nicecsv.close()

#Implement sending the report to storage bucket
#os.system(gsutil )
