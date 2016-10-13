import re

personlog = open('person.log')
for line in personlog:
	if "userName" not in line:continue
	line = line.strip()
	x =  re.findall("\S+=\S+",line)
	
	print x

	