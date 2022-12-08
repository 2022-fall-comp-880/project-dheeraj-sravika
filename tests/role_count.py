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
