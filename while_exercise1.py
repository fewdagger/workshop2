i = 2
while i <= 12:
    j = 1
    print("  [", i, "]")
    while j <= 12:
        print(i, "*", j, ":", i * j, end="\n")
        j += 1
    print("---------------")
    i += 1
