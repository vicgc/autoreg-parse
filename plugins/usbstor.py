from Registry import Registry
from helperFunctions import jsonOutput, outputRender, getControlSet, getComputerName

header = "USB Storage"
objects_list = []

def getPlugin(reg_sys, reg_nt='', reg_soft=''):     
    computer_name = getComputerName(reg_sys)
    current = getControlSet(reg_sys)

    try:
        usbstor = reg_sys.open('%s\\Enum\USBSTOR' % (current))
        for k in usbstor.subkeys():
            last_write = k.timestamp()
            for usbstorsk in k.subkeys():
                #Vendor/Make/Version = k.name() 
                venmakever = k.name().split("&")
                #Serial Number = usbstorsk.name()
                serial_number = (str(usbstorsk.name().encode('ascii'))).split("&")
                #Populate the S/N list so we can search for it in Enum\USB
                # Using [0] since we split on the &0 above, which makes comparing easier below.
                vendor = venmakever[1].lstrip("Ven_").encode('ascii')
                make = venmakever[2].lstrip("Prod_").encode('ascii')
                ver = venmakever[3].lstrip("Rev_").encode('ascii')

                for usbstorv in usbstorsk.values():
                    if "ParentIdPrefix" in usbstorv.name():
                        #ParentIdPrefix = usbstorv.value()
                        pip = usbstorv.value()
                    else:
                        pass

                objects_list.append(jsonOutput(header, \
                                    key_item = usbstor.name(), \
                                    value_item1 = vendor + " " + make, \
                                    value_item2 = serial_number[0], \
                                    value_item3 = pip, \
                                    value_item4 = "", \
                                    value_item5 = "", \
                                    lastwrite_time = last_write, \
                                    sys_name = computer_name)) 
                
    except Registry.RegistryKeyNotFoundException as e:
        print "There is no USBSTOR Key."

    outputRender(objects_list)

    






