# lists...
# A list is an ordered, mutable collection of items (numbers, strings, even other lists).

print("Lists...")

list = [1, 2, 3, "shahid", ["newlist", 99], True]

print(list)
print(list[2])

# modify
list[3] = "Shahid"
print(list)
print(type(list))

print("The list has length ", len(list))


# 🔧 List Methods
# Method	Description
# append(x)	Add item to the end
# insert(i, x)	Add item at position i
# remove(x)	Remove first occurrence of x
# pop(i)	Remove and return item at index i
# clear()	Remove all items
# index(x)	Return first index of x
# count(x)	Count how many times x appears
# sort()	Sort list (in-place)
# reverse()	Reverse the list
# copy()	Create a shallow copy


# Tuples
# A tuple is an ordered, immutable collection of items.
print("Tuples...")

tuple = (1, 2, 3, False, "Tuple")
# tuple[1] = "yellow"  # ❌ TypeErro

print(tuple)
print(type(tuple))
t2 = (
    "A",
    "B",
    22,
)
t3 = ()
t4 = (55,)  # # One-element tuple needs comma!
print(t2, "\n", t3, "\n", t4)
print(type(t2), type(t3), type(t4))


for p in tuple:
    print(p)


# 🔁 Tuple Methods
#  Tuples have only two built-in methods:


t = (1, 2, 2, 2, 2, 3)
print("line count ", t.count(2))  # 2
print(t.index(1))  # 0

# 🔄 Tuple Unpacking

person = ("Kumar", 30)
name, age = person
print(name)  # Kumar
print(age)  # 30

# 🧠 When to Use Tuples?
#       Use case	                             Why tuple?

# Fixed data	                        Data should not change
# Dictionary keys	               Tuples can be used as keys; lists can’t
# Function returns                 	Return multiple values cleanly
# Faster performance              	Tuples are lighter than lists
