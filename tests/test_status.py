"""Import required packages for the test cases."""
import os
import unittest
from apps.main import Data
from apps.employee_status import EmployeeStatus


class Status(unittest.TestCase):
    """Test EmployeeStatus class."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "//..//data"
        df_10 = Data.read(f"{data_dir}//data_10.csv")
        self.tasks_10 = EmployeeStatus(df_10)

        df_50 = Data.read(f"{data_dir}//data_50.csv")
        self.tasks_50 = EmployeeStatus(df_50)
        df = Data.read(f"{data_dir}//data.csv")
        self.tasks_all = EmployeeStatus(df)

    def test_multiple_entries(self):
        """Test case 1 using data.csv."""
        actual_result = self.tasks_all.result()
        expected_result = {
            "Bangalore": {
                "Full Time": {
                    "Mobile",
                    "Backend",
                    "SDE",
                    "Android",
                    "Python",
                    "IOS",
                    "Testing",
                    "Frontend",
                    "Database",
                    "Web",
                },
                "Intern": {"Frontend"},
            },
            "Chennai": {
                "Full Time": {"SDE", "Android", "Python", "Frontend", "Java"},
                "Intern": {"Python", "SDE"},
            },
            "Hyderabad": {
                "Full Time": {
                    "Backend",
                    "SDE",
                    "Android",
                    "Python",
                    "Testing",
                    "Frontend",
                    "Java",
                },
                "Intern": {"SDE", "Android", "Python", "Frontend", "Java"},
            },
            "Jaipur": {"Intern": {"SDE"}, "Full Time": {"SDE"}},
            "Kerala": {"Full Time": {"SDE"}, "Contractor": {"SDE"}},
            "Kolkata": {"Intern": {"SDE"}, "Full Time": {"SDE"}},
            "Madhya Pradesh": {"Full Time": {"SDE"}, "Intern": {"SDE"}},
            "Mumbai": {"Full Time": {"SDE"}, "Contractor": {"SDE"},
                       "Intern": {"SDE"}},
            "New Delhi": {
                "Full Time": {"Backend", "SDE", "Android", "IOS", "Frontend"},
                "Intern": {"Android", "SDE"},
            },
            "Pune": {
                "Full Time": {"Backend", "SDE", "Android", "IOS", "Frontend"},
                "Intern": {"Frontend"},
            },
        }
        self.assertEqual(actual_result, expected_result)

    def test_fifty_entries(self):
        """Test case 2 using fifty.csv with fifty rows."""
        actual_result = self.tasks_50.result()
        expected_result = {
            "Bangalore": {
                "Full Time": {
                    "Android",
                    "Backend",
                    "Database",
                    "Frontend",
                    "IOS",
                    "Mobile",
                    "Python",
                    "SDE",
                    "Testing",
                    "Web",
                },
                "Intern": {"Frontend"},
            },
            "Chennai": {
                "Full Time": {"Java", "SDE", "Python", "Android", "Frontend"},
                "Intern": {"SDE", "Python"},
            },
        }
        self.assertEqual(actual_result, expected_result)

    def test_ten_entries(self):
        """Test case 3 using ten.csv with ten rows."""
        actual_result = self.tasks_10.result()
        expected_result = {
            "Bangalore": {
                "Full Time": {"Backend", "Database", "Frontend", "Mobile",
                              "SDE", "Web"}
            }
        }
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
