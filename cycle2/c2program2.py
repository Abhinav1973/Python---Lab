str=input("Enter a string: ")
first_char=str[0]
new_str=first_char+str[1:].replace(first_char,"$")
print("Modified string:",new_str)
