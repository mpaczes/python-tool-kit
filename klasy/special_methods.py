# Special (Magic/Dunder) Methods

# In this Python Object-Oriented Tutorial, we will be learning about special methods. 
# These are also called magic or dunder methods. 
# These methods allow us to emulate built-in types or implement operator overloading. 
# These can be extremely powerful if used correctly. 
# We will start by writing a few special methods of our own and then look at how some of them are used in the Standard Library. 
# Let's get started.

class Employee:
    raise_amt = 1.04 # class variable

    def __init__(self, first, last, pay): # jest wolana niejawnie podczas tworzenia obiektu
        self.first = first  # instance variable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): # jest wolana niejawnie gdy wywolujemy metode 'repr(our_object)' na obiekcie
        return 'Employee({}, {}, {})'.format(self.first, self.last, self.pay)

    def __str__(self): # jest wolana niejawnie gdy wywolujemy metode 'str(our_object)' na obiekcie
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other): # dunder add method
        return self.pay + other.pay
    
    def __len__(self): # dunder len method
        return len(self.fullname())

# metoda repr(obiekt) - jednoznaczna reprezaentacja obiektu; uzywac ja mozna podczas debugowania kodu i logowania

# metoda str(obiekt) - czytelna reprezentacja obiektu; jest uzywana podczas wyswietlania informacji end userowi

emp_1 = Employee('Andrzej', 'Jablonski', 200)
print(emp_1)

print(repr(emp_1))

print(str(emp_1))
