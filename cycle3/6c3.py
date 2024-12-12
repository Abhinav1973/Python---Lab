N=int(input("Enter a number: "))
count=0
flag=1
for num in range(2,N+1):
	prime=True
	for i in range(2,num):
		if num % i == 0:
			prime=False
			break
	if prime:
		flag+=1
		if flag % 2 == 0:
			print(num)
	count+=1
