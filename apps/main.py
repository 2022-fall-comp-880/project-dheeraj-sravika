"""
Program for IT Salaries in India.

Authors:
  Dheeraj - https://github.com/sk1591
  Sravika - https://github.com/ss1883
"""
import csv


class Data:
    """Data class reads the CSV file and
    stores the data into list of lists."""

    def __init__(self, dataset) -> None:
        """Initializes the class attributes"""
        self.dataset = dataset

    def __str__(self):
        """Convert to string representation."""
        return self.dataset

    def read(self, file: str):
        """Reads the data file."""
        data = []
        with open(file, newline="", encoding="utf-8") as f:
            op = csv.reader(f)
            next(op, None)
            for row in op:
                data.append(row)
        return data

    def count(self, city_name: str) -> dict:
        """Counts the employment status in a particular city."""
        output = {}
        for row in self.dataset:
            if row[5] == city_name:
                if row[-2] in output:
                    output[row[-2]] += 1
                else:
                    output[row[-2]] = 1
        return output
