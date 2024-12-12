age=int(input("Enter the age: "))
if(age<10 and age>=0):
	print("The ticket rate is 7")
elif(age>=10 and age<60):
        print("The ticket rate is 10")
elif(age>=60):
        print("The ticket rate is 5")
else:
        print("invalid")
