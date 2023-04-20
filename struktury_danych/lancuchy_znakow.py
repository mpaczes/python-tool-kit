# Strings - Working with Textual Data

message = 'Hello world !'

print(message)
print(len(message))

# slicing
print(message[0])
print(message[0:5])
print(message[6:])

# metody
print(message.lower())
print(message.upper())
print(message.count('Hello'))
# zwraca -1 jezeli nie moze znalezc lancucha
print(message.find('world'))
print(message.replace('world', 'universe'))

# laczenie lancuchow
greeting = 'Hello'
name = 'Michael'

print(greeting + ', ' + name)

# {} oznacza placeholder
message = '{}, {}'.format(greeting, name)
print(message)

# od wersji Pythona 3.6 mozna uzywac fstringów
message = f'{greeting} : {name}'
print(message)

#przydatne metody

# pokaze wszsytkie dostepne metody i atrybuty zmiennej
print(dir(name))

# informacje o klasie 'str' czyli string
print(help(str))
print(help(str.lower))
