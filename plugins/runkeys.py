from Registry import Registry
from helperFunctions import jsonOutput, outputRender, getControlSet

def getPlugin(reg_soft, reg_nt, reg_sys):

    print ("\n" + ("=" * 51) + "\nTRADITIONAL \"RUN\" KEYS\n" + ("=" * 51))

    hklm_run_list = ["Microsoft\\Windows\\CurrentVersion\\Run",
                     "Microsoft\\Windows\\CurrentVersion\\RunOnce",
                     "Microsoft\\Windows\\CurrentVersion\\RunOnceEx",
                     "Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run",
                     "Microsoft\\Windows\\CurrentVersion\\RunServicesOnce"
                     "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run",
                     "Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce"]

    ntuser_run_list = ["Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                       "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
                       "Software\\Microsoft\\Windows\\CurrentVersion\\RunServices",
                       "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run"]

    try:

        for k in hklm_run_list:
            key = reg_soft.open(k)
            for v in key.values():
                if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    print 'Key: %s\nValue: %s\nRegPath: %s\n' % (v.name().encode('ascii', 'ignore'), v.value().encode('ascii', 'ignore'), k)

        for k in hklm_run_list:
            print k
            key = reg_sys.open(k)
            for v in key.values():
                if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    print 'Key: %s\nValue: %s\nRegPath: %s\n' % (v.name().encode('ascii', 'ignore'), v.value().encode('ascii', 'ignore'), k)

        for k in ntuser_run_list:
            key = reg_nt.open(k)
            for v in key.values():
                if v.value_type() == Registry.RegSZ or v.value_type() == Registry.RegExpandSZ or v.value_type() == Registry.RegMultiSZ:
                    print 'Key: %s\nValue: %s\nRegPath: %s\n' % (v.name().encode('ascii', 'ignore'), v.value().encode('ascii', 'ignore'), k)

    except Registry.RegistryKeyNotFoundException as e:
        pass
