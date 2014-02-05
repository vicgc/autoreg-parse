from Registry import Registry
from collections import OrderedDict
from helperFunctions import jsonOutput, outputRender, getControlSet

objects_list = []
service_list = []
header = "Services"

def getPlugin(reg_sys, reg_nt='', reg_soft=''):
    
    current = getControlSet(reg_sys)
    servicesnames = reg_sys.open('%s\\Services' % (current))

    for service in servicesnames.subkeys():
        service_list.append(service.name().lower())
    
    for service_name in service_list:
        k = reg_sys.open('%s\\Services\\%s' % (current, service_name))
        key_name = k.name()
        last_write = str(k.timestamp())
        try:
            type_name = k.value("Type").value()
        except:
            type_name = "???"
        try:
            image_path = k.value("ImagePath").value()
        except:
            image_path = "???"
        try:
            display_name = k.value("DisplayName").value()
        except:
            display_name = "???"
        try:
            start_type = k.value("Start").value()
        except:
            start_type = "???"
        try:
            service_dll = k.subkey("Parameters").value("ServiceDll").value()
        except:
            service_dll = "???"
            
        objects_list.append(jsonOutput(header, \
                                        key_item = key_name, \
                                        value_item1 = start_type, \
                                        value_item2 = image_path, \
                                        value_item3 = display_name, \
                                        value_item4 = type_name, \
                                        value_item5 = service_dll, \
                                        lastwrite_time = last_write))
    outputRender(objects_list)
