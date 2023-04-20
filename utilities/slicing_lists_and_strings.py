# How to slice lists and strings in Python. 
# Slicing allows us to extract certain elements from these lists and strings. 
# This can be extremely useful for stripping out certain values from lists or getting a substring of a characters from a string.

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list[5])

print(my_list[-1]) # ostatni element

# list[start:end:step]
print(my_list[0:6])
print(my_list[1:-2])
print(my_list[1:])
print(my_list[:]) # cala lista

# slicing strings
sample_url = 'http://mpaczes.com'
print(sample_url)

print(sample_url[::-1]) # reverse

print(sample_url[-4:]) # zwroci napis '.com'

print(sample_url[7:]) # zwroci 'mpaczes.com'

print(sample_url[7:-4]) # zwroci 'mpaczes'
