import os


def walking(start_adr):
    #import os

    if os.path.isdir(start_adr):
        res = os.listdir(start_adr)
        print(res)
        for x in res:
            if os.path.isdir(start_adr+'/'+x):
                walking(start_adr + '/' + x)
                #print(res)


path = "/home/stanislav/PycharmProjects/pythonProject/ITEA_HW/hw8/"

walking(path)

