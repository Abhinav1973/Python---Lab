str=input("Entr the string: ")
freq={}
for char in str:
	freq[char]=freq.get(char,0)+1
print(freq)
