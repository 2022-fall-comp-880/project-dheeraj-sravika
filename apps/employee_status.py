class EmployeeStatus:
    """Class module for employment status for each city."""

    def __init__(self, dataset) -> None:
        """Initializes the class attributes."""
        self.dataset = dataset

    def result(self) -> dict:
        """List of job roles with an employment status for each city."""
        output = {}
        # with open('data.csv', newline='') as csvfile:
        #   reader = csv.DictReader(csvfile)
        for row in self.dataset:
            if row[5] not in output:
                output[row[5]] = dict()
            if row[-2] in output[row[5]]:
                output[row[5]][row[-2]].add(row[-1])
            else:
                output[row[5]][row[-2]] = {row[-1]}
        return output
