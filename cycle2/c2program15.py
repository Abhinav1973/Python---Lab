d = {1: 'banana', 3: 'apple', 2:'orange'}

sorted_dict = {}
for key in sorted(d.keys()):
    sorted_dict[key] = d[key]

print("Sorted by keys (ascending):", sorted_dict)

sorted_dict_desc = {}
for key in sorted(d.keys(), reverse=True):

    sorted_dict_desc[key] = d[key]

print("Sorted by keys (descending):", sorted_dict_desc)
