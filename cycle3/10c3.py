num=int(input("Enter a no: "))
i=1
print(f"factors of {num} are: ")
while i<num:
	if num%i == 0:
		print(i)
	i+=1
