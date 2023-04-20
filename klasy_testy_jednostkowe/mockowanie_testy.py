# uruchamianie testów : python -m unittest mockowanie_testy.py

import unittest
from unittest.mock import patch
from mockowanie_klasa_do_testow import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('John', 'Doe', 1200)
        self.emp_2 = Employee('Jane', 'Doe', 800)

    def tearDown(self):
        print('tearDown')

    def test_monthly_schedule_success(self):
        with patch('mockowanie_klasa_do_testow.requests.get') as mocked_get:
            # given
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'success'

            # when
            schedule = self.emp_1.monhtly_schedule('May')

            # then
            mocked_get.assert_called_with('http://company.com/Doe/May') # assert that the last call was made with the specified arguments
            self.assertEqual(schedule, 'success')

    def test_monthly_schedule_failure(self):
        with patch('mockowanie_klasa_do_testow.requests.get') as mocked_get:
            # given
            mocked_get.return_value.ok = False

            # when
            schedule = self.emp_2.monhtly_schedule('June')

            # then
            mocked_get.assert_called_with('http://company.com/Doe/June')    # assert that the last call was made with the specified arguments
            self.assertEqual(schedule, 'bad response')


# dzieki temu co nizej mozna testy uruchomic tak : python mockowanie_testy.py
if __name__ == '__main__':
    unittest.main()

