def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(n, r):
    if n < r:
        return "Error: n must be >= r "
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    if n < r:
        return "Error n must be >= r "
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter the value of n : "))
r = int(input("Enter the value of r : "))

print(f"Permutations : {permutations(n, r)}")
print(f"Combinations : {combinations(n, r)}")
