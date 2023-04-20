# String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates

# In this Python tutorial, we will be learning how to perform some advanced string formatting operations. 
# Formatting our strings allows us to display our information in exactly the way we would like it to be displayed. 
# Everyone, in almost all areas of Python programming, comes across a situation where they need to format a data type in a specific way. 
# Let's get started.

person = {'name': 'Jane', 'age': 23}

sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)

sentence = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
print(sentence)

tag = 'h1'
text = 'this is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

sentence = 'My name is {0[name]} and I am {1[age]} years old'.format(person, person)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence)

# object attributes
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', 33)

sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
print(sentence)

# unpacking dictionary
person = {'name': 'Jane', 'age': 23}

sentence = 'My name is {name} and I am {age} years old'.format(**person)
print(sentence)

# format numbers

# doklejanie zera z przodu
for i in range(1, 11):
    sentence = 'the value is {:02}'.format(i)
    print(sentence)

pi = 3.14159265

# liczxba miejsc po przecinku
sentence = 'pi is equal to {:.3f}'.format(pi)
print(sentence)

# separator tysiecy
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

# formatowanie daty
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year '.format(my_date)
print(sentence)
