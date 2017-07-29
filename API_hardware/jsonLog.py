import json
import datetime


def log(data):
    if platform.system() == 'Windows':
        f = 'files_download/day_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.txt'
    else:
        f = ' /home/pi/Temperature_Controller/files_download/day_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.txt'
    with open(f, 'a') as outfile:
        json.dump(data, outfile)
        outfile.write("\n")
    outfile.close()


