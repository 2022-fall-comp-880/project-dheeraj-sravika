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
        return str(self.dataset)

    @staticmethod
    def read(file: str):
        """Reads the data file."""
        list_data = []
        with open(file, newline="", encoding="utf-8") as f:
            op = csv.reader(f)
            next(op, None)
            for row in op:
                list_data.append(row)
        return list_data

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

    def status(self) -> dict:
        """List of job roles with an employment status for each city."""
        output = {}
        for row in self.dataset:
            if row[5] not in output:
                output[row[5]] = dict()
            if row[-2] in output[row[5]]:
                output[row[5]][row[-2]].add(row[-1])
            else:
                output[row[5]][row[-2]] = {row[-1]}
        return output


if __name__ == "__main__":

    data = Data()
    input_text = data.read("../data/data.txt")

    city = "Hyderabad"
    value = Data.count(dataset=input_text)
    print("Counts: ", value.count(city_name=city))

