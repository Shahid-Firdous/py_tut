# # In Python, a dictionary is a built-in data type used to store collections of key-value pairs.
# # It's similar to a real-life dictionary where you look up a word (key) and get its definition (value).

# print("Dictionary...")

# student = {"name": "Shahid", "RollNo": 22511, "Friend": "Abrar"}
# student2 = {"age": 21, "reg": 2889}

# print(student.get("RollNo"))  # To avoid errors if key does`nt exist

# print(type(student))
# student["name"] = "showkat"  # Update key
# print(student)
# student["semester"] = 6  # Add new key
# print(student)
# print(student["name"])
# print(student.pop("name"))  # Removes and returns the value
# print(student)
# del student["RollNo"]  # Deletes the key..
# print(student)

# print(dict.items(student))
# print(dict.keys(student))
# print(dict.values(student))
# student.update(student2)  # Updates with another dict  (Merging)
# print(student)
# student.update(job="none",married= "no")    # Updates with keyword arguments  (Merging)
# print(student)
# print(dict.clear(student))
# empty={}  #Creates empty dictionary

# Sets in Python are a built-in data type used to store unordered, unique items.
# Think of a set like a mathematical set: no duplicates, and the order doesn’t matter.

print("Sets...")

# Mutable.
# Non indexabe.

set1 = {"Shahid", "nag", "Shaowkat", "RP", 19}  # using curly braces

print(set1)  # Prints random elements no order is followed.

print(type(set1))

set2 = [1, 2, 3, 4, 5, 6]  # Creating using the set() function

print(set2)
print(type(set2))

eset = set()  # Empty set..
print(eset)
set1.add("SP")  # Adds element but only one..
print(set1)
set1.remove("SP")  # Removes element, raises error if item does`nt exist
print(set1)

set1.discard(19)  # doesn`t raise error if item doest`t exist
print(set1)
print("Shahid" in set1)  # Checks element.

# Some set operations...

A = {1, 2, 3}
B = {4, 5, 6}
print("Set A =", A)
print("Set B =", B)

print("A union B=", A | B)  # Union
print("A intersection B=", A & B)  # Intersection
print("A difference B =", A - B)  # Difference
print("A s difference B=", A ^ B)  # Symetric difference (in A or B, but not both)

set1.add("NewSet")  # – Adds an element
print(set1)
set1.remove("NewSet")  # – Removes an element (errors if not present)
print(set1)

set1.discard("nnn")  # – Removes an element (no error if not present)
print(set1)

A.clear()  # – Empties the set
print(A)

set1.pop()  # – Removes and returns an arbitrary element
print(set1)

# set1.updateother_set(A)  # – Adds elements from another set
print(set1)

