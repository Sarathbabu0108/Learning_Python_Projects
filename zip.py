list1 = [1, 2, 3, 4, 5, 6]
list2 = ["one", "two", "three", "four", "five", "six"]

zipped = list(zip(list1, list2))
print(zipped)

# unzipping

unzipped = list( zip(*zipped))
print(unzipped)