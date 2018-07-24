import os
import csv
import shutil

SrcFileName = "Source csv file"
dest = "Destination Path"
with open(SrcFileName) as csvfile:
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')

    for row in csvrows:
        filepath = dest
        url = row[4]
        if os.path.isfile(url):
            shutil.copy2(url, dest)
        else:
            pass
