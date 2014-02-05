Auto Registry Parser (autoreg-parse) 
=====================================  

The idea of this started out as one to duplicate Microsoft's autoruns tool to the extent possible with only offline registry hives. Then I started adding extra non-autorun keys. I couldn't think of a better name after that so I just left the "auto" part in there. If you don't like the name you can name it what you want once it's downloaded to your desktop.

If you want to add plugins feel free. I would appreciate it actually :)

Purpose/Reason
===============

Why not use the tools that already exist?

- All the new/cools guys/gals are writing code in Python.
- I wanted to learn to code in Python better. What better way than to write a tool in Python?
- I didn't like the output of the alternatives. It's complex and not consistent. It doesn't scale well either if you want to analyze multiple systems.
- I wanted something that's easy to write plugins for. I personally found the alternatives cryptic.

Output
=======

The default output for autoreg-parse is now JSON. JSON is much easier to process across multiple systems. Current registry tools don't make it easy. I wanted autoreg-parse to be useful when analyzing multiple systems vs. one. Current reg parsing tools didn't support this so I decided to start writing my own.

See Example.txt - https://github.com/sysforensics/autoreg-parse/blob/master/Example_Output.txt

How to Install
===============

(Going off memory here)

Python

- Python 2.7

Python Registry

- Download: https://github.com/williballenthin/python-registry
- python setup.py build
- python setup.py install

That should be all you need. It will work in Windows and Linux/OSX. Email me at: patrickolsen[at]sysforensics.org if you have issues. I am happy to help.

How-to
=======

python autoreg-parse.py -h
                usage: autoreg-parse.py [-h] [-nt NTUSER] [-sys SYSTEM] [-soft SOFTWARE]
                                        [-p PLUGIN [PLUGIN ...]] [-lp]
                
                Parse the Windows registry for malware-ish related artifacts.
                
                optional arguments:
                  -h, --help            show this help message and exit
                  -nt NTUSER, --ntuser NTUSER
                                        Path to the NTUSER.DAT hive you want parsed.
                  -sys SYSTEM, --system SYSTEM
                                        Path to the SYSTEM hive you want parsed.
                  -soft SOFTWARE, --software SOFTWARE
                                        Path to the SOFTWARE hive you want parsed.
                  -p PLUGIN [PLUGIN ...], --plugin PLUGIN [PLUGIN ...]
                                        Specify plugin your plugin name.
                  -lp, --listplugins    This plugin lists the available plugins.

Todo
=======
Key

- X = Done
- O = Partially done and implemented
- [ ] = Not started

In no specific order....


[ ] Error handling

- [ ] Add some better error handling.

[O] User Assist

- [ ] Add counts, etc. to the output. Right now it's just pulling the names.

[O] System and User Information

- [ ] Last logged on user
- [ ] Shutdown time
- [ ] SIDS and User Profile Information

[O] Services

- [ ] Write some JSON parsing code to look for anaomolies

[ ] LastWrite Times

- [ ] Add last write time to everything and then it can be filtered via JSON parsing.

[ ] Output

- [X] JSON is the default
- [X] CSV -> I've written a json2csv.py file. See the Output Example for details.
- [ ] json2sqlite?

Thanks to:
==============

@williballenthin - http://www.williballenthin.com for writing python-registry, which is what I am using. It's great.

@hiddenillusion - This example got me started on the idea. https://github.com/williballenthin/python-registry/blob/master/samples/forensicating.py

Wingware for providing a great Python IDE and supporting the Open Source community. http://www.wingware.com/
