import os
import unittest
from apps.main import Data
from apps.main import Count


class TestCount(unittest.TestCase):
    """Test task1 Count class."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(_file_) + "/data"
        dataset = Data().read(f"{data_dir}/all.csv")
        self.tasks_all = Count(dataset)

        def test_valid_name(self):
            """Test case 1 using all.csv."""
            actual_result = self.tasks_all.count(city_name="Mumbai")
            expected_result = {'Full Time': 22, 'Contractor': 2, 'Intern': 1}
            self.assertEqual(actual_result, expected_result)

        def test_empty_name(self):
            """Test case 2 using all.csv."""
            actual_result = self.tasks_all.count(city_name="")
            expected_result = {}
            self.assertEqual(actual_result, expected_result)

        def test_wrong_name(self):
            """Test case 3 using all.csv."""
            actual_result = self.tasks_all.count(city_name="Bang")
            expected_result = {}
            self.assertEqual(actual_result, expected_result)

    if _name_ == "_main_":
        unittest.main()
