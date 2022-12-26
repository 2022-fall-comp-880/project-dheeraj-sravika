class Count:
    """Class module for job employment status count."""

    def __init__(self, dataset) -> None:
        """Initialize the class attributes."""
        self.dataset = dataset

    def count(self, city_name: str) -> dict:
        """Count of employment status in a particular city."""
        output = {}
        for row in self.dataset:
            if row[5] == city_name:
                if row[-2] in output:
                    output[row[-2]] += 1
                else:
                    output[row[-2]] = 1
        return output
