from Registry import Registry
from helperFunctions import jsonOutput, outputRender, getComputerName

objects_list = []
header = "Run Keys"

def getPlugin(reg_soft, reg_nt, reg_sys):
    computer_name = getComputerName(reg_sys)
    reg_hives = [reg_sys, reg_soft, reg_nt]
    run_entries =   ["Microsoft\\Windows\\CurrentVersion\\Run",
                     "Microsoft\\Windows\\CurrentVersion\\RunOnce",
                     "Microsoft\\Windows\\CurrentVersion\\RunOnceEx",
                     "Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
                     "Microsoft\\Windows\\CurrentVersion\\RunServicesOnce"
                     "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run",
                     "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                     "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                     "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                     "Software\\Microsoft\\Windows\\CurrentVersion\\RunServices",
                     "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run"]
    
    for k in run_entries:
        for hive in reg_hives:
            try:
                key = hive.open(k)
                for v in key.values():
                    try:
                        key_name = v.name()
                    except:
                        key_name = "???"
                    try:
                        key_value = v.value()
                    except:
                        key_value = "???"
                    try:
                        last_write = str(key.timestamp())
                    except:
                        last_write = "???"

                    objects_list.append(jsonOutput(header, \
                                            key_item = key_name, \
                                            value_item1 = key_value, \
                                            value_item2 = "???", \
                                            value_item3 = "???", \
                                            value_item4 = "???", \
                                            value_item5 = "???", \
                                            lastwrite_time = last_write,\
                                            sys_name = computer_name))
            except Registry.RegistryKeyNotFoundException as e:
                pass

    outputRender(objects_list)
