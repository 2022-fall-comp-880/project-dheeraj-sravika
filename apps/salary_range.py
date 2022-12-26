"""Salary Ranges Module."""


class Ranges:
    """Represent a module for of job roles between the given salary range."""

    def __init__(self, dataset) -> None:
        """Initialize the class attributes."""
        self.dataset = dataset

    def roles(self, city_name: str, low: int, high: int) -> set:
        """Retrieve the job roles for given salary range."""
        output = set()
        for row in self.dataset:
            if (row[5] == city_name) and (low < int(row[3]) < high):
                output.add(row[-1])
        return output
