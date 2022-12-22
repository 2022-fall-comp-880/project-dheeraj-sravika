"""
Program for IT Salaries in India.

Authors:
  Dheeraj - https://github.com/sk1591
  Sravika - https://github.com/ss1883
"""
import csv

from apps.salary_range import Ranges

"""Reads & Writes data from csv file."""


class Data:
    """Data class reads the CSV file and
    stores the data into list of lists."""

    @classmethod
    def read(cls, data_file: str):
        """Reads the data file."""
        list_data = []
        with open(data_file, newline="", encoding="utf-8") as f:
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

    # Investigation Question 1
    print("Q1. List of Job Roles with an employment status for "
          "each city in the dataset:")
    employee_status = EmployeeStatus(dataset=dataset)
    print(employee_status.result())
    print("\n")

    # Investigation Question 2
    city = "Hyderabad"
    print("Q2. Count of Employment Status in a particular city:")
    count = Count(dataset=dataset)
    print(f"Count of Job Roles at {city}: ", count.count(city_name=city))
    print("\n")

    # Investigation Question 3
    print("Q3. List of job roles that fall between the given salary "
          "range of a city:")
    job_roles = Ranges(dataset=dataset)
    low = 500000
    high = 1000000
    print(f"Job Roles at {city} with salary range between {low} and {high}: ")
    print(job_roles.roles(city_name=city, low=low, high=high))


if __name__ == "__main__":
    main()
