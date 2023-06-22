import unittest
from program import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
    
    def setUp(self):
        self.emp_1 = Employee('saif', 'rehman', 62000)
        self.emp_2 = Employee('saad', 'sameer', 57000)
        self.emp_3 = Employee('huzefa', 'anwer', 57500)

    def tearDown(self):
        pass
    
    def test_email(self):
        self.assertEqual(self.emp_1.gmail, 'saif.rehman@gmail.com')
        self.assertEqual(self.emp_2.gmail, 'saad.sameer@gmail.com')
        self.assertEqual(self.emp_3.gmail, 'huzefa.anwer@gmail.com')

        # emails should change when names change
        emp_1, emp_2, emp_3 = 'Saif', 'Saad', 'Huzefa'

        self.assertEqual(self.emp_1.gmail, 'Saif.rehman@gmail.com')
        self.assertEqual(self.emp_2.gmail, 'Saad.sameer@gmail.com')
        self.assertEqual(self.emp_3.gmail, 'Huzefa.anwer@gmail.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'saif rehman')
        self.assertEqual(self.emp_2.fullname, 'saad sameer')
        self.assertEqual(self.emp_3.fullname, 'huzefa anwer')

    def test_apply_raise(self):
        self.assertEqual(self.emp_1.apply_raise, 65100)
        self.assertEqual(self.emp_1.apply_raise, 59850)
        self.assertEqual(self.emp_1.apply_raise, 60375)

if __name__ == '__main__':
    unittest.main()