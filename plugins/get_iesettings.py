from Registry import Registry

def getPlugin(reg_nt, reg_soft='', reg_sys=''):
    
    try:
        k = reg_nt.open("Software\\Microsoft\\Internet Explorer\\Main")
        for v in k.values():
            print 'Key: {0:<10}\nValue: {1:<15}\n'.format(v.name(), v.value())
    
    except Registry.RegistryKeyNotFoundException as e:
        pass
