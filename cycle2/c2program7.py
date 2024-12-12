list1=input("Enter color for list1 separated by comma: ").split(',')
list2=input("Enter color for list1 separated by comma: ").split(',')
print([color for color in list1 if color not in list2])

