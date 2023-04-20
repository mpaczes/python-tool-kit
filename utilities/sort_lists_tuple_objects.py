# Sorting Lists, Tuples, and Objects

li = [9,1,8,2,7,3,6,4,5]

# ascending
s_li = sorted(li) # zwraca nowa posortowana liste

print('sorted variable asc: \t', s_li)

li.sort() # sortuje liste zwraca null

print('original variable asc: \t', li)

# descending
s_li = sorted(li, reverse=True)

print('sorted variable desc: \t', s_li)

li.sort(reverse=True)

print('original variable desc: \t', li)

# tuples nie maja metody sortujacej i daltego musimy uzyc 'sorted'

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('tuple asc \t', s_tup)

# mapa - domyslnie sortuje klucze
di = {'name': 'Andrzej', 'job': 'cieć', 'age': None}
s_di = sorted(di)
print('dictionary asc: \t', s_di)

# sortowanie po roznych kryteriach
li = [-4,-5,-6,3,2,1]
s_li = sorted(li, key = abs) # na kazdym elelemencie jest wolana funkcja w czasie sortowania
print(s_li)

# sortowanie obiektow
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self): # mowi Pythonowi jak ma wygladac klasa podczas wyswietlania na ekranie
        return '({},{},${})'.format(self.name, self.age, self.salary)
    
e1 = Employee('carl', 37, 70000)
e2 = Employee('sarah', 29, 80000)
e3 = Employee('john', 43, 90000)

employees = [e1, e2, e3]

# custom sorting function
def e_sort(emp):
    # return emp.name
    return emp.age

# s_employees = sorted(employees, key = e_sort)
# s_employees = sorted(employees, key = e_sort, reverse = True)
s_employees = sorted(employees, key = lambda e: e.name) # sortowanie z uzyciem wyrazen lamda

print(s_employees)
