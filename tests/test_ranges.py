import os
import unittest
from apps.main import Data
from apps.salary_range import Ranges
"""Import required packages for the test cases."""


class TestJobRoles(unittest.TestCase):
    """Test task3 JobRoles class."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "\\..\\data"
        dataset = Data.read(f"{data_dir}\\data.csv")
        self.tasks_all = Ranges(dataset)

    def test_valid_city(self):
        """Test case 1 using all.csv and valid city name."""
        actual_result = self.tasks_all.roles("Bangalore", 10000, 5023000)
        expected_result = {'Android', 'Backend', 'Database',
                           'Frontend', 'IOS', 'Mobile', 'Python',
                           'SDE', 'Testing', 'Web'}
        self.assertEqual(actual_result, expected_result)

    def test_empty(self):
        """Test case 2 using all.csv and empty city name."""
        actual_result = self.tasks_all.roles("", 30000, 999999)
        expected_result = set()
        self.assertEqual(actual_result, expected_result)

    def test_another(self):
        """Test case 3 using all.csv and valid city."""
        actual_result = self.tasks_all.roles("Pune", 439999, 2040249)
        expected_result = {'Android', 'Frontend', 'IOS', 'SDE'}
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
