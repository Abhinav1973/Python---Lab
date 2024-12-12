values=lambda x:2**x
terms=list(map(int,input("Enter the list of item:").split(" ")))
power_of_2=list(map(values,terms))
print("power of 2 for the given terms:")
for i in range(len(terms)):
	print(f"2 * {terms[i]} = {power_of_2[i]}")
