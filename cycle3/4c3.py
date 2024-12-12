import math
ul=int(input("Enter the upper limit: "))
ll=int(input("Enter the lower limit: "))
for num in range(ll,ul+1):
	even=True
	for digit in str(num):
		if int(digit)%2!=0:
			even=False
			break
	if even and (math.sqrt(num))%2==0:
		print(num)
