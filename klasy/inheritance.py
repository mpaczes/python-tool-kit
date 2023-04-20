# Inheritance - Creating Subclasses

class Employee:
    raise_amt = 1.04 # class variable

    def __init__(self, first, last, pay): # konstruktor
        self.first = first  # instance variable
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):  # klasa Developer dziedziczy z Employee
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->>', emp.fullname())

dev_1 = Developer('Andrzej', 'Jablonski', 2000, 'VBA')
dev_2 = Developer('Joanna', 'Spreglewska', 900, 'NIC')

mgr_1 = Manager('Sue', 'Smith', 200, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# print(help(Developer))

print(dev_1.email)
print(dev_1.prog_lang)

# czy cos jest instacja klasy
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# czy cos jest podklasa klasy
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))
