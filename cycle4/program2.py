def add(a,b):
	return a+b

def subtract(a,b):
	return	a-b

def multiply(a,b):
	return a*b

def divide(a,b):
	if b!=0:
       		 return  a/b
	else:
		print("Division by 0 not posiible")

def modulus(a,b):
	if b!=0:
        	return a%b 
	else:
		print("modulus by 0 not possible")

print("1.Add\n2.subtract\n3.multiply\n4.divide\n5.modulus\n")
choice = int(input("Enter your choice: "))

if(choice>5 or choice<=0):
	print("invalid choice")

else:
	a=float(input("Enter first number: \n"))
	b=float(input("Enter second number: \n"))

	if choice == 1:
		print(f"{a}+{b}={add(a,b)}")
	elif choice == 2:
       		print(f"{a}-{b}={subtract(a,b)}")
	elif choice == 3:
        	print(f"{a}*{b}={multiply(a,b)}")
	elif choice == 4:
       		print(f"{a}/{b}={divide(a,b)}")
	else:
        	print(f"{a}%{b}={modulus(a,b)}")
