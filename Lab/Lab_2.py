#Program to Search an Element in a List 
# Search element in a list 
lst = [5, 15, 25, 35, 45] 
print("List:", lst) 
key = int(input("Enter element to search: ")) 
if key in lst: 
 print("Element found at index:", lst.index(key)) 
else: 
 print("Element not found") 