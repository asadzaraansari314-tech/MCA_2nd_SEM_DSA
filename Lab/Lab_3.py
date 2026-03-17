#Program to Demonstrate Basic Operations on Data Structures (List) 
# Basic operations on list 
lst = [] 
# Insertion 
lst.append(10) 
lst.append(20) 
lst.append(30) 
print("After insertion:", lst) 
# Traversal 
print("Traversing list:") 
for item in lst: 
 print(item, end=" ") 
# Searching 
key = 20 
if key in lst: 
 print("\nElement", key, "found") 
else: 
 print("\nElement not found") 
# Deletion 
lst.remove(20) 
print("After deletion:", lst) 
# Length 
print("Length of list:", len(lst))