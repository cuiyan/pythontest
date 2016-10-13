import re
text_name = raw_input('Enter the file name:')
if len(text_name) == 0 : text_name = 'regex_sum_313637.txt'
text = open(text_name)
text = text.read()
numbers = re.findall('[0-9]+',text)
number_sum = 0
for n in numbers:
	number_sum = number_sum+int(n)
	
print number_sum