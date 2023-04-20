
import sqlite3  # nie trzeba sqlite3 instalowac, bo ta baza jest w instalacji Pythona
from employee import Employee

emp_1 = Employee('John', 'Doe', 14000)
emp_2 = Employee('Jane', 'Doe', 15000)

conn = sqlite3.connect(':memory:') # connect to a database in RAM

c = conn.cursor()

c.execute(""" CREATE TABLE employees(
            first text,
            last text,
            pay integer
) """)

# c.execute("INSERT INTO employees VALUES ('John', 'Doe', 12000)")

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first' : emp_1.first, 'last': emp_1.last, 'pay' : emp_1.pay})
# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first' : emp_2.first, 'last': emp_2.last, 'pay' : emp_2.pay})
# conn.commit()

# c.execute("SELECT * FROM employees WHERE last = 'Doe'")

# print(c.fetchone())
# print(c.fetchall())

def insert_emp(emp):
    with conn: # niejawnie wywoluje commit i rollback (jezeli sa bledy)
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first' : emp.first, 'last': emp.last, 'pay' : emp.pay})

def get_emps_by_name(lastname): # w select nie potrzeba transakcji
    c.execute("SELECT * FROM employees WHERE last = :last", {'last' : lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn: # niejawnie wywoluje commit i rollback (jezeli sa bledy)
        c.execute(""" UPDATE employees SET pay = :pay 
                    WHERE first = :first AND last = :last """,
                  {'first' : emp.first, 'last' : emp.last, 'pay' : pay})

def remove_emp(emp):
    with conn: # niejawnie wywoluje commit i rollback (jezeli sa bledy)
        c.execute(" DELETE FROM employees WHERE first = :first AND last = :last ",
                  {'first' : emp.first, 'last' : emp.last})

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 34000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

c.close()
conn.close()
