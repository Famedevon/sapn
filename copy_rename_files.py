import os
import csv
import shutil
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
SrcFileName = "Source Path"
dest = "Destination Path"
log = open("Logger Path" + timestr + '.txt',
            "w+")
with open(SrcFileName) as csvfile:
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvrows:
        id = row[0]
        path = row[1]
        if not os.path.exists(path):
            log.write(id + '|' + path + '|0' '\n')
        else:
            path, dirs, files = next(os.walk(path))
            log.write(id + '|' + path + '|' + str(len(files)) + '\n')
            for root, dirs, filenames in os.walk(path):
                for f in filenames:
                    oldname = path + '/' + f
                    newname = id + '_' + f
                    shutil.copy(oldname, dest + newname)
