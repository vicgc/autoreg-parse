from Registry import Registry
from helperFunctions import jsonOutput, outputRender, getControlSet, getComputerName
import time

objects_list = []
header = "System Information"


def getPlugin(reg_soft, reg_sys, reg_nt=''):
    computer_name = getComputerName(reg_sys)
    current = getControlSet(reg_sys)
    timezone_key = [current + "\\Control\\TimeZoneInformation"]
    sysinfo_key = ["Microsoft\\Windows NT\\CurrentVersion"]
    

    for k in timezone_key:
        key = reg_sys.open(k)
        for v in key.values():
            if "StandardName" in v.name():
                time_zone = v.value()
            else:
                pass

    for k in sysinfo_key:
        key = reg_soft.open(k)
        for v in key.values():
            if "ProductName" in v.name():
                product_name = v.value()
            if "CurrentVersion" in v.name():
                current_version = v.value()
            if "CurrentBuildNumber" in v.name():
                current_build = v.value()
            if "CSDVersion" in v.name():
                csd_version = v.value()
            if "InstallDate" in v.name():
                install_date = time.strftime('%a %b %d %H:%M:%S %Y (UTC)', time.gmtime(v.value()))
            else:
                pass

        objects_list.append(jsonOutput(header, \
                            key_item = product_name, \
                            value_item1 = current_version, \
                            value_item2 = current_build, \
                            value_item3 = csd_version, \
                            value_item4 = install_date, \
                            value_item5 = time_zone, \
                            lastwrite_time = "???", \
                            sys_name = computer_name))

    outputRender(objects_list)
