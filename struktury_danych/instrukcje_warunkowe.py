# Conditionals and Booleans - If, Else, and Elif Statements

if True:
    print('Conditional was true')

language = 'java'

if language == 'python':
    print('language is Python')
elif language == 'java':
    print('language is Java')
else:
    print('No match')

# Python nie ma instruckji 'switch'

# and, or, not
user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('admin page')
else:
    print('bad creds')

logged_in = False

if not logged_in:
    print('please log in')
else:
    print('welcome')

# operator 'is' czyli rownosc obiektow w pamieci
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(id(a))
print(id(b))

b = a   # teraz operator 'is' zwroci True

print(a is b)
print(id(a))
print(id(b))

# False values :
#   False 
#   None
#   Zero of any numeric type
#   any empty sequence. For example : '', (), []
#   any empty mapping. For example : {}
# condition = False
# condition = None
# condition = 0
# condition = []
# condition = ''
condition = {}

if condition:
    print('evaluated to true')
else:
    print('evaluated to false')

