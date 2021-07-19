list1 = [1, 2, 3, 4, 5, 6]
list2 = ["one", "two", "three", "four", "five", "six"]

zipped = list(zip(list1, list2))
print(zipped)

# unzipping

unzipped = list(zip(*zipped))
print(unzipped)

items = ['apple', 'banana', 'orange']
counts = [3, 6, 4]
prices = [0.99, 0.25, 0.50]
sentances = []
for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = 'I bought ' + count + '  ' + item + 's at ' + price + 'rupees.'
    sentances.append(sentence)
print(sentances)