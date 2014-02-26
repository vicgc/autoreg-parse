#Reference http://stackoverflow.com/questions/1871524/convert-from-json-to-csv-using-python
#Example: python json2csv.py services.json > mehmeh.csv

import csv, json, sys

json_input_file = open(sys.argv[1])
data = json.load(json_input_file)
json_input_file.close()

output = csv.writer(sys.stdout)

output.writerow(data[0].keys())

for jdata in data:
	output.writerow(jdata.values())