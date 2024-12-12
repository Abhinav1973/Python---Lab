result = []
count=int(input("Enter how many integers do you want :"))
print("Enter",count , "integers :")
for i in range(1,count + 1):
	nums = int(input())
	if (nums > 100):
		result.append("over")
	else:
		result.append(nums)
print("Final list: ",result)
