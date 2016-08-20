import json, datetime


def log(data):
    f = 'log/app_log_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.log'
    with open(f, 'a') as outfile:
        json.dump(data, outfile)
        outfile.write("\n")
    outfile.close()
