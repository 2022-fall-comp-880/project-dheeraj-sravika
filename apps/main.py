"""
Program for IT Salaries in India.

Authors:
  Dheeraj - https://github.com/sk1591
  Sravika - https://github.com/ss1883
"""
import csv
"""Reads & Writes data from csv file."""


class Data:
    """Data class reads the CSV file and
    stores the data into list of lists."""

    @classmethod
    def read(cls, file: str):
        """Reads the data file."""
        list_data = []
        with open(file, newline="", encoding="utf-8") as f:
            op = csv.reader(f)
            next(op, None)
            for row in op:
                list_data.append(row)
        return list_data


def main():
    """Program Starts from here."""
    from status_count import Count
    from employee_status import EmployeeStatus

    my_data = Data()
    dataset = my_data.read("../data/data.csv")

    city = "Hyderabad"
    count = Count(dataset=dataset)
    print(f"Job Role Counts at {city}: ", count.count(city_name=city))

    employee_status = EmployeeStatus(dataset=dataset)
    print(employee_status.result())


if __name__ == "__main__":
    main()
