def fibonacci(n):
	if(n<=1):
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)

terms = int(input("Enter number of terms: "))
if(terms<0):
	print("please enter positive integer")
else:
	for i in range(terms):
		print(fibonacci(i),end=" ")
