# jak uruchomic te testy z linii komend -> python -m unittest .\test_employee.py

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    # uruchamia sie raz przed wszystkimi testami
    @classmethod
    def setUpClass(cls):
        pass

    # uruchamia sie raz po wszystkich testach
    @classmethod
    def tearDownClass(cls):
        pass

    # uruchamia sie przed kazdym testem
    def setUp(self):
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    # uruchamia sie po kazdym tescie
    def tearDown(self):
        pass
    
    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        
        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
    # ta linia pozwala uruchomić testy tak : python .\test_employee.py
    if __name__ == '__main__':
        unittest.main()