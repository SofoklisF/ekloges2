lefta=0

while True:
	
	x=float(input("Euro: "))
	
	if x>=0:
		lefta=lefta+float(x) 
	
	if x<0:
		lefta=lefta+float(x) 
	
	print "Kilikeio: ",lefta,"Euro"
