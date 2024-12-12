str=input("Enter a string: ")
if(len(str)>=3 and str[-3:]=="ing"):
	print(str[0:-3]+"ly")
else:
	print(str+"ing")
