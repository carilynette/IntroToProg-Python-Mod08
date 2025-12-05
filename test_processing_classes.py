# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# CWilliams, 11/20/25, Modified Script
# ------------------------------------------------------------------------------- #

import unittest
import tempfile
import json

import data_classes as data
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()


    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2025-11-30","ReviewRating": 3},
            {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2025-11-30","ReviewRating": 3},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(
            self.temp_file_name,
            self.employee_data,
            employee_type=data.Employee,
        )

        # Assert that the employees list contains the expected employee objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[0].last_name, "Doe")
        self.assertEqual(self.employee_data[0].review_date.isoformat(),"2025-11-30")
        self.assertEqual(self.employee_data[0].review_rating, 3)

        #testing sample date #2.
        self.assertEqual(self.employee_data[1].first_name, "Alice")
        self.assertEqual(self.employee_data[1].last_name, "Smith")
        self.assertEqual(self.employee_data[1].review_date.isoformat(),"2025-11-30")
        self.assertEqual(self.employee_data[1].review_rating, 3)

if __name__ == "__main__":
    unittest.main()
