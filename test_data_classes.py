# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# CWilliams, 11/30/25, Modified Script
# ------------------------------------------------------------------------------- #

import unittest
from datetime import date

from data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")

class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor (default values)
        employee = Employee()
        self.assertEqual(employee.first_name, "")
        self.assertEqual(employee.last_name, "")
        self.assertEqual(employee.review_date, date(1900,1,1))
        self.assertEqual(employee.review_rating, 3)

    def test_employee_init_with_values(self):  # Test the constructor with valid data.
        employee = Employee("Alice", "Smith", "2025-11-30", 3)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, date(2025, 11, 30))
        self.assertEqual(employee.review_rating, 3)

    def test_employee_invalid_review_date(self):
        with self.assertRaises(ValueError):
            Employee("Bob","Jones", "11/30/2025",3) #wrong format

    def test_employee_invalid_review_rating(self):
        with self.assertRaises(ValueError):
            Employee("Eve", "Brown", "2025-11-30", 10)  #tests invalid rating

if __name__ == '__main__':
    unittest.main()


