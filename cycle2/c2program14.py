size=int(input("total numbers in numberlist: "))
numbers=[]
print("Enter number in number list")
for num in range(size):
        nums=int(input())
        numbers.append(nums)
print(numbers)

pos_num=[num for num in numbers if num > 0]
print("positive numbers are: ",pos_num)

for i in numbers:
	print("square of ", i,"=",i*i) 
word = input("Enter a word: ")
word = word.lower()
vowels=[]
ordvalue=[]
for char in word:
	ordvalue.append(ord(char))
	if char in 'aeiou':
		vowels.append(char)
print("vowels : ",vowels)
print("ordinal values: ",ordvalue)
