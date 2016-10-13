# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
num_add = 0 
num_count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num_str = line.find(":")
    num = float(line[num_str+1:].strip())
    num_count = num_count+1
    num_add = num_add+num

print "Average spam confidence:",num_add/num_count