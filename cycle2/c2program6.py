names=input("Enter the first names separated by comma: ")
names=names.lower()
count=sum(name.count('a') for name in names)
print("Occurence of 'a': ",count)
