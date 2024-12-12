n=int(input("Enter the no of terms: "))
fibonacci=[0,1]
for i in range(2,n):
	next_term=fibonacci[i-1]+fibonacci[i-2]
	fibonacci.append(next_term)
print("fibonacci series is:",fibonacci[:n])
