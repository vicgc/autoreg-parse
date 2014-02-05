from collections import OrderedDict
from Registry import Registry
import sys
import json

def jsonOutput(header, \
			   key_item, \
			   value_item1, \
			   value_item2, \
			   value_item3, \
			   value_item4, \
			   value_item5, \
			   lastwrite_time,\
               sys_name):
    d = OrderedDict()
    d['Title']   = header
    d['Name']    = key_item
    d['Value1']  = value_item1
    d['Value2']  = value_item2
    d['Value3']  = value_item3
    d['Value4']  = value_item4
    d['Value5']  = value_item5
    d['LWTime']  = str(lastwrite_time)
    d['CompName'] = sys_name
    return d

def getControlSet(reg_sys):
    try:
        select = reg_sys.open("Select")
        current = select.value("Current").value()
        controlsetnum = "ControlSet00%d" % (current)
        return controlsetnum

    except Registry.RegistryKeyNotFoundException as e:
        pass

def outputRender(objects_list):
	sys.stdout.write(json.dumps(objects_list, indent=4))

def getComputerName(reg_sys):
    
    current = getControlSet(reg_sys)
    computerName = reg_sys.open("%s\\Control\\ComputerName\\ComputerName" % (current))
    for v in computerName.values():
        if v.name() == "ComputerName":
            comp_name = v.value()
        return comp_name
