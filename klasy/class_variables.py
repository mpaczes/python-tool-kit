# Class Variables

# mamy : instance variables i class variables

# instance variables - sa unikatowe (rozne) dla kazdej instancji klasy

# class variables - sa takie same dla wszystkich instacji klasy

class Employee:
    raise_amount = 1.04 # class variable

    num_of_emps = 0

    def __init__(self, first, last, pay): # konstruktor
        self.first = first  # instance variable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Andrzej', 'Jablonski', 2000)
emp_2 = Employee('Joanna', 'Spreglewska', 900)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__) # namespace -> {'first': 'Andrzej', 'last': 'Jablonski', 'pay': 2000, 'email': 'Andrzej.Jablonski@company.com'}
print(Employee.__dict__) # namespace

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)
