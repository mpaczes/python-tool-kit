# Classes and Instances

class Employee:
    def __init__(self, first, last, pay): # konstruktor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Andrzej', 'Jablonski', 2000)
emp_2 = Employee('Joanna', 'Spreglewska', 900)

print(emp_1.fullname())
print(emp_2.fullname())
