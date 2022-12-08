import os
import unittest
from apps.main import Data
from apps.main import EmployeeStatus


class EmployeeStatus(unittest.TestCase):
    """Test task 3 EmployeeStatus class."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(_file_) + "/data"
        df_10 = Data().read(f"{data_dir}/ten.csv")
        self.tasks_10 = EmployeeStatus(df_10)
        df_50 = Data().read(f"{data_dir}/fifty.csv")
        self.tasks_50 = EmployeeStatus(df_50)
        df = Data().read(f"{data_dir}/all.csv")
        self.tasks_all = EmployeeStatus(df)
