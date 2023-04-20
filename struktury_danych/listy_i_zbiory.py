# Lists, Tuples, and Sets

#lista
courses = ['History', 'Math', 'Physics']

print(courses[0])
print(courses[-1])  # minus pobiera elementyz  koncza listy; -1 oznacza ostatni element

# slicing
print(courses[0:2])
print(courses[:2])  # to samo co wyzej

# metody list
courses.append('Art')
print(courses)

courses.insert(0, 'Art')
print(courses)

# extend
courses_2 = ['Education']
courses.extend(courses_2)   # dodaje inna liste do naszej listy
print(courses)

# usuwanie
courses.remove('Math')
courses.pop() # usuwa ostatni element
print(courses)

courses.reverse()
courses.sort()      # porzadek alfabetyczny
courses.sort(reverse=True)
print(courses)

# wyszukiwanie
print(courses.index('History')) # Raises ValueError if the value is not present.
print('Education' in courses)

# iterowanie po liscie
for item in courses:
    print(item)

for index, item in enumerate(courses):
    print(index, item)

# laczenie elementow listy
course_str = ', '.join(courses)
print(course_str)

# tuples - podobne do list, ale sa immutable, czyli niemodyfikowalne
tuple_1 = ('History', 'Math')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'  # TypeError: 'tuple' object does not support item assignment

# zbiory - nie zachowuja kolejnosci wstaiwania i nie zawieraja duplikatow
cs_courses = {'Math', 'History', 'Math'}
art_courses = {'Math', 'Design'}

print(cs_courses)
print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# empty
empty_list = []
empty_list = list() # to samo co wyzej

empty_tuple = ()
empty_tuple = tuple() # to samo co wyzej

# empty_set = {}  # this is not right. It is a dictionary
empty_set = set()

