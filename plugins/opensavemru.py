from Registry import Registry

opensavemru_keys = []

def getPlugin(reg_nt, reg_soft='', reg_sys=''):
    k = reg_nt.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\OpenSaveMRU")
    for keys in k.subkeys():
        opensavemru_keys.append(keys.name())
    for m in opensavemru_keys:
    	f = reg_nt.open('Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\OpenSaveMRU\\%s' % (m))
    	for v in f.values():
    		print 'Key: {0:<10}\nSubkey: {1:<10}\nValue: {2:<10}\n'.format(f.name(), v.name(), v.value())