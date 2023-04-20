# classmethods and staticmethods

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

    @classmethod    # class method - metoda ktora jako pierwszy argument niejawnie dostaje klase
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod    # class method as alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Andrzej', 'Jablonski', 2000)
emp_2 = Employee('Joanna', 'Spreglewska', 900)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-24000'
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# static methods - nie dostaje zadnego automatycznego argumentu
# i dlatego zachowuje sie jak zwykkle funkcje

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))
