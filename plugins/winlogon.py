from Registry import Registry
from helperFunctions import jsonOutput, outputRender, getComputerName

objects_list = []
header = "Winlogon"

winlogon_list = ["Microsoft\\Windows NT\\CurrentVersion\\Winlogon"]

def getPlugin(reg_soft, reg_nt='', reg_sys=''):

    try:
        for k in winlogon_list:
            key = reg_soft.open(k)
            last_write = key.timestamp()
            for v in key.values():
                if v.name().lower() == "shell":
                    shell = v.name()
                    shell_path = v.value()
                elif v.name().lower() == "userinit":
                    userinit = v.name()
                    userinit_path = v.value()
                elif v.name().lower() == "taskman":
                    taskman = v.name()
                    taskman_path = v.value()
                else:
                    taskman = "???"
                    taskman_path = "???"
            
            objects_list.append(jsonOutput(header, \
                                            key_item = k, \
                                            value_item1 = shell, \
                                            value_item2 = shell_path, \
                                            value_item3 = userinit, \
                                            value_item4 = userinit_path, \
                                            value_item5 = taskman, \
                                            lastwrite_time = last_write, \
                                            sys_name = "???"))
    except Registry.RegistryKeyNotFoundException as e:
        pass

    outputRender(objects_list)