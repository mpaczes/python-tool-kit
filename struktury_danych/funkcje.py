# Functions

# definicja - w Pythonie mozna nie deklarowac typow argumentow i typu zwracanego
# parametr 'greeting' jest obowiazkowy
# parametr 'name' jest opcjonalny
# nazywa sie to : 'positional and keywords arguments'
def hello_func(greeting: str, name: str = 'you') -> str:
    # pass    # oznacza brak ciala funkcji i dzieki temu nie pokaze sie blad
    # print('hello function')
    return '{}, {} function'.format(greeting, name)

# wywolanie
# print(hello_func())
# print(hello_func().upper())
# hello_func()
print(hello_func('hi'))
print(hello_func('hi', name = 'john')) # nazwane argumenty musza byc zdefiniowane na koncu

# mdefinicja obowiazkowych i opcjonalnych parametrow jezeli nie znamy ich ilosci
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'John', age = 24)
# ('Math', 'Art')
# {'name': 'John', 'age': 24}
# czyli '*args' to jest tuple czyli niezmienna lista (immutable)
# natomiast '**kwargs' to jest mapa (dictionary)

courses = ['Design', 'CompSc']
info = {'name': 'Jane', 'age': 19}

# musimy tutaj uzyc '*' i '**' zeby zrobic 'unpack sequence and dictionary'
student_info(*courses, **info)

# przykłady
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """ Return true for leap years, false for non-leap years """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """ Return number of days in thata month in that year """
    if not 1 <= month <= 12:
        return 'invalid month'

    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2017))
print(is_leap(2020))

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))