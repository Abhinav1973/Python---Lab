size=int(input("Enter the size of the list: "))
list=[]
sum=0
for i in range(size):
	val=int(input("Enter the values: "))
	list.append(val)
	sum=sum+val
print("sum: ",sum)
