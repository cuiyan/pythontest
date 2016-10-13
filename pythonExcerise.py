def multi(x,y):
	print (x/y)
	
while True:
	try:
		x = raw_input("please input divisor:")
		x = float(x)
	except:
		print("plese input a number")
		continue
		
	try:
		y = raw_input("please input dividend:")
		y = float(y)
	except:
		print("plese input a number")
		continue
	
	if(y==0):
		print("dividend can not be 0")
		continue
		
	multi(x,y)
	
