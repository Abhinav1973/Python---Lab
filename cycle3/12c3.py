N=int(input("Enter step number: "))
for i in range(1,N+1):
	for j in range(1,i+1):
		print(i*j , end=" ")
	print()