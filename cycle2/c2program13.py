text=input("Enter a line of text: ")
words=text.split()
word_count={}
for word in words:
	words=word.lower()
	if words in word_count:
		word_count[words]+=1
	else:
		word_count[words]=1
print("word occurrence: ",word_count)
