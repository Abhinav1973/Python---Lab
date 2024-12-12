words=input("Enter word separated by comma: ").split(',')
length=0
for word in words:
	if len(word)>length:
		length=len(word)

print("length of the longest word: ",length)
