import  math
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value c: "))
d = b ** 2 - 4 * a * c
if (d > 0):

	root1 = (-b + math.sqrt(d)) / (2 * a)
	root2 = (-b - math.sqrt(d)) / (2 * a)
	print(f"The roots are: {root1} and {root2}")
elif (d == 0):
	root = -b / (2 * a)
	print(f"The roots are the same: {root}")
else:
	real_part = -b / (2 * a)
	imaginary_part = math.sqrt(-d) / (2 * a)
	print("It doesnot have real solution")
	print("complex solutions  are:")
	print(f"Root 1: {real_part} + {imaginary_part}i")
	print(f"Root 2: {real_part} - {imaginary_part}i")
