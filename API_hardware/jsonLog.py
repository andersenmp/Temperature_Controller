import json
import datetime


def log(data):
    f = 'files_download/day_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.txt'
   # with open(f, 'a') as outfile:
   #     json.dump(data, outfile)
   #     outfile.write("\n")
   # outfile.close()
