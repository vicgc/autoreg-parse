import re
from Registry import Registry

def getPlugin(reg_soft, reg_nt='', reg_sys=''):

    print ("\n" + ("=" * 51) + "\nTASK SCHEDULER\n" + ("=" * 51))

    task_list = ["Microsoft\\Windows\\CurrentVersion\\Explorer\\SharedTaskScheduler"]
    
    for k in task_list:
        key = reg_soft.open(k)
        #print key
        for keys in key.values():
            print keys.value()