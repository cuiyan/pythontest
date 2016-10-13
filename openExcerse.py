# Use words.txt as the file name

fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
    for f in fh :
      f = f.rstrip()
      print f.upper()
except:
    print "not find the file"