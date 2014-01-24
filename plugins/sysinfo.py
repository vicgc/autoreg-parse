from Registry import Registry
from controlset import getControlSet
import time
from collections import defaultdict
from itertools import izip

def getPlugin(reg_soft, reg_sys, reg_nt=''):

    os_dict = {}
    sid_dict = defaultdict(list)
    username_dict = defaultdict(list)
    
    k = reg_soft.open("Microsoft\\Windows NT\\CurrentVersion")

    try:
        for v in k.values():
            if v.name() == "ProductName":
                os_dict['ProductName'] = v.value()
            if v.name() == "EditionID":
                os_dict['EditionID'] = v.value()
            if v.name() == "CurrentBuild":
                os_dict['CurrentBuild'] = v.value()
            if v.name() == "CurrentVersion":
                os_dict['CurrentVersion'] = v.value()
            if v.name() == "InstallDate":
                os_dict['InstallDate'] = time.strftime('%a %b %d %H:%M:%S %Y (UTC)', time.gmtime(v.value()))
            else:
                pass

    except Registry.RegistryKeyNotFoundException as e:
        pass
    
    
    current = getControlSet(reg_sys)
    
    computerName = reg_sys.open("%s\\Control\\ComputerName\\ComputerName" % (current))

    try:
        for v in computerName.values():
            if v.name() == "ComputerName":
                os_dict["ComputerName"] = v.value()
            else:
                pass

    except Registry.RegistryKeyNotFoundException as e:
        pass

    timeZone = reg_sys.open("%s\\Control\\TimeZoneInformation" % (current))

    try:
        for v in timeZone.values():
            if v.name() == "StandardName":
                os_dict["TimeZoneName"] = v.value()
            else:
                pass

    except Registry.RegistryKeyNotFoundException as e:
        pass

    try:
        profileList = reg_soft.open("Microsoft\\Windows NT\\CurrentVersion\\ProfileList")

        for sid in profileList.subkeys():
            sid_dict['SIDs'].append(sid.name())
            sid_dict['UserNames'].append(sid.value("ProfileImagePath").value())
    except Registry.RegistryKeyNotFoundException as e:
        pass

    '''
    Output.....
    '''
    print ("\n" + ("=" * 51) + "\nSYSTEM INFORMATION\n" + ("=" * 51))
    print "Computer Name: " + os_dict['ComputerName']
    print "Operating System: " + os_dict['ProductName'], os_dict['CurrentVersion']
    print "Install Date: " + os_dict['InstallDate']
    print "Time Zone: " + os_dict['TimeZoneName'] + "\n"
    print "Usernames:"
    for u, s in izip(sid_dict["SIDs"], sid_dict["UserNames"]):
        print 'SID: {0:<10}\nUsername: {1:<10}'.format(u, \
            str(s.replace("%SystemDrive%\\Documents and Settings\\", \
            "").replace("%systemroot%\\system32\\config\\", "")))
    print "\n"