# Dictionaries - Working with Key-Value Pairs

student = {'name' : 'John', 'age' : 25, 'courses' : ['Math', 'CompSci']}

print(student['courses'])
print(student.get('name'))
print(student.get('phone', 'Not found'))

# aktualizacja pojedynczej pary mapy
student['phone'] = '555-9999'
student['name'] = 'Jane'
print(student)

# aktualizacja wielu par mapy
student.update({'name' : 'Emma', 'age' : 19})
print(student)

# usuwanie
del student['age']
# albo tak
phone = student.pop('phone')
print(student)

# klucze mapy
print(len(student)) # liczba kluczy mapy

print(student.keys())
print(student.values())
print(student.items())  # klucze i wartosci

# iterowanie po mapie
for key in student:     # iterowanie po kluczach
    print(key)

for key, value in student.items():     # iterowanie po kluczach
    print(key, value)
