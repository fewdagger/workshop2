# Example 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # output : ['apple' , 'cherry']

# Example 2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # output : ['apple' , 'cherry']

# Example 3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # output : ['apple' , 'banana']

# Example 4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # output : ['apple' , 'cherry']

# Example 5
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # output : []