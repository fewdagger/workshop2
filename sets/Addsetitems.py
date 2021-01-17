# EX1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# OP : {'cherry','apple',''banana',}

# EX2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# OP : {"apple", "banana", "cherry","pineapple","mango","papaya"}