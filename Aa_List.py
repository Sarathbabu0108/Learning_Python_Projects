'''my_list = ["january", "February", "March"]
print(my_list[0])
my_list.append("April")
print(my_list[3])'''

'''my_set = {"january", "February", "March"}
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)
my_set.remove("january")
print(my_set) '''

'''names = ["sarath", "sam", "samji", "arjun"]
l = []
for persons in names:
    l.append(persons)

print(l)

print([persons for persons in names])


l = []
for persons in names:
    l.append(persons + 'dumped me.')

print(l)
print([persons + 'dumped me.' for persons in names])'''

'''movies_and_ratings = {"interstellar":9, "dark knight":8, "joker":5, "avengers":7}

list_movies = []

for movie in movies_and_ratings:
  if movies_and_ratings[movie] > 6:
      list_movies.append(movie)

print(list_movies)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6])'''

import re

text = " i am batman"
pattern = re.compile("[a-z]")

result = pattern.search(text)

print(result)


