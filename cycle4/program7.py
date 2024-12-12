def factorial(num):
        if num==1 or num==0:
                return 1
        else:
                fact=1
                for i in range(2,num+1):
                        fact=fact*i
                return fact
def nth_term(n):
	return (n**n)/(factorial(n))
def sum_series(n):
	total_sum=0
	for i in range(1,n+1):
		total_sum+=nth_term(i)
	return total_sum

n=int(input("Enter the number of terms: "))
print(f"The sum of the Series upto {n} term is : {sum_series(n)}")
