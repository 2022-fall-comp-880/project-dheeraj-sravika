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

    def read(self, file: str):
        data = []
        with open(file, newline="", encoding="utf-8") as f:
            op = csv.reader(f)
            next(op, None)
            for row in op:
                data.append(row)
        return data

