import json
import datetime
import os


def log(data):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename =  'files_download/day_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.txt'
    f = os.path.join(fileDir, filename)
    with open(f, 'a') as outfile:
        json.dump(data, outfile)
        outfile.write("\n")
    outfile.close()


