from Registry import Registry
from helperFunctions import jsonOutput, outputRender, getComputerName

objects_list = []
BHO_list = []
header = "Browser Helper Object"

bho_keys = ["Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects",
            "WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects"]

def getPlugin(reg_soft, reg_sys='', reg_nt=''):
    for b in bho_keys:
        try:
            k = reg_soft.open(b)
            for v in k.subkeys():
                BHO_list.append(v.name())
        
        except Registry.RegistryKeyNotFoundException as e:
            pass
    
    for clsids in BHO_list:
        try:
            k = reg_soft.open("Classes\\CLSID\\%s" % (clsids))
            try:
                key_name = k.name()
            except:
                key_name = "???"
            try:
                key_value = k.subkey("InProcServer32").value('').value()
            except:
                key_value = "???"
            try:
                last_write = str(k.timestamp())
            except:
                last_write = "???"

            objects_list.append(jsonOutput(header, \
                                            key_item = k.name(), \
                                            value_item1 = k.subkey("InProcServer32").value('').value(), \
                                            value_item2 = "???", \
                                            value_item3 = "???", \
                                            value_item4 = "???", \
                                            value_item5 = "???", \
                                            lastwrite_time = last_write, \
                                            sys_name = "???"))
        except Registry.RegistryKeyNotFoundException as e:
            pass

    outputRender(objects_list)
