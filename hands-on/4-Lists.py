# Ordered sequences
# Mutable
# Can contain different types of objects

# Definition

list = ["Michael Jackson", 10.1, 1004]
print("First item in the list is : ", list[1])

# List can contains any objects
listOfList = [[1,2], "deneme", (1.2)] 

list[1:2]

# Append
list.append([3])
list

# Extend: append multiple elements
list.extend([2,3,4])
list

# Mutable
list[0] = 'Cet'
list

# delete
del(list[len(list) - 1])
list

# Convert string into a list
type("Split".split())

# Clone
clone = list[:]
clone
print(clone)