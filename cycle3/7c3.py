ul=int(input("Enter upper limit: "))
total=0
for i in range(1,ul):
	if i % 6 == 0 and i % 4 != 0:
		print(i,end=" ")
		total+=i
print("sum is ",total)
