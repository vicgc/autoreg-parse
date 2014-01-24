'''
Todo:
[ ] Sort the numbered values so they are easier to read.

d1 = defaultdict(list)
for k, v in l:
    d1[k].append(v)

d = dict((k, tuple(v)) for k, v in d1.iteritems())
'''

from Registry import Registry
from collections import defaultdict
from itertools import izip

def getPlugin(reg_nt, reg_sys='', reg_soft=''):

    recentdocs_dict = defaultdict(list)
    recentdocs_dict_subk = defaultdict(list)

    print ("\n" + ("=" * 51) + "\nRECENT DOCUMENTS\n" + ("=" * 51))

    try:
        recentdocs = reg_nt.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RecentDocs")

        for docs in recentdocs.values():
            if "mrulistex" in docs.name().lower() or "viewstream" in docs.name().lower():
                pass
            else:
                recentdocs_dict['ValueName'].append(int(docs.name()))
                recentdocs_dict['ValueData'].append(docs.value())
        for vname in izip(sorted(recentdocs_dict['ValueName'])):
            print vname #'{0:<10} {1:<5} {2:>20}'.format(recentdocs.name(), vname)
        '''
        for vname, vdata in izip(sorted(recentdocs_dict['ValueName']), recentdocs_dict['ValueData']):
            print '{0:<10} {1:<5} {2:>20}'.format(recentdocs.name(), vname, vdata)
        
        for sk in recentdocs.subkeys():
            for v in sk.values():
                if "mrulistex" in v.name().lower():
                    pass
                else:
                    recentdocs_dict_subk['ValueName'].append(int(v.name()))
                    recentdocs_dict_subk['ValueData'].append(v.value())
                    recentdocs_dict_subk['KeyName'].append(sk.name())
                #print recentdocs_dict_subk['KeyName']


        #for vname, vdata, kname in izip(sorted(recentdocs_dict_subk['ValueName']), recentdocs_dict_subk['ValueData'], sorted(recentdocs_dict_subk['KeyName'])):
        #    print vname, vdata
        '''

    except Registry.RegistryKeyNotFoundException as e:
        pass