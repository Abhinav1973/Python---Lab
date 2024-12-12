def Compare(n,s1,s2):
	if s1[:n]==s2[:n]:
		return True
	else:
		return False
s1=input("Enter first String: ")
s2=input("Enter second String: ")
n=int(input("Enter n value: "))
r=Compare(n,s1,s2)
if r==True:
	print(f"first {n} characters of {s1} and {s2} are same")
elif r==False:
	print(f"first {n} characters of {s1} and {s2} are not same")
