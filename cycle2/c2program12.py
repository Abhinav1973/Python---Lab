list1=[]
list2=[]
size1=int(input("Enter the size of list 1: "))
size2=int(input("Enter the size of list 2: "))
print("Enter list1 values: ")
for i in range(size1):
	list1.append(int(input()))
print("Enter list2 values:")
for i in range(size2):
	list2.append(int(input()))
if(len(list1)==len(list2)):
	print("Both list have same length")
else:
	print("Both list are not same length")
sumone=0
samevalue=[]
for i in list1:
	sumone = sumone+i
	sumtwo=0
	for j  in list2:
		sumtwo=sumtwo+j
		if i == j:
			samevalue.append(i)
if(sumone==sumtwo):
	print("Sum is equal;sum is",sumone)
else:
	print("sum is not equal ; L1 = ",sumone, " L2 =  ",sumtwo)
if(samevalue)==0:
	print("there is no same value")
else:
	print("value occur in both list",samevalue)
