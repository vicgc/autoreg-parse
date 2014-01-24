'''
Author: Patrick Olsen
Email: patrickolsen@sysforensics.org
Twitter: @patrickrolsen
'''
import sys, os
import argparse
import glob
from Registry import Registry

parser = argparse.ArgumentParser(description='Parse the Windows registry for malware-ish related artifacts.')
parser.add_argument('-nt', '--ntuser', help='Path to the NTUSER.DAT hive you want parsed.')
parser.add_argument('-sys', '--system', help='Path to the SYSTEM hive you want parsed.')
parser.add_argument('-soft', '--software', help='Path to the SOFTWARE hive you want parsed.')
parser.add_argument('-p', '--plugin', nargs='+', help='Specify plugin your plugin name.')
parser.add_argument('-lp', '--listplugins', action='store_true', help='This plugin lists the available plugins.')

args = parser.parse_args()

if args.ntuser:
    reg_nt = Registry.Registry(args.ntuser)
else:
    reg_nt = ''
    pass
if args.software:
    reg_soft = Registry.Registry(args.software)
else:
    reg_soft = ''
    pass
if args.system:
    reg_sys = Registry.Registry(args.system)
else:
    reg_sys = ''
    pass
if args.listplugins:
    for plugs in glob.glob(os.path.join("plugins", "*.py")):
        if "None" in plugs:
            pass
        else:
            print plugs.replace("plugins/", "").replace(".py", "").strip()

if not args.plugin:
    print parser.usage
    exit(0)

def main():
    for plugin_name in args.plugin:
        sys.path.insert(0, 'plugins')
        module = __import__(plugin_name)
        module.getPlugin(reg_nt=reg_nt, reg_soft=reg_soft, reg_sys=reg_sys)
if __name__ == "__main__":
    main()