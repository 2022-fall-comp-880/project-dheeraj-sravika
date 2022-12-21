class Ranges:
    """List of job roles that fall between the given salary range of a city."""

    def __init__(self, dataset) -> None:
        self.dataset = dataset

    def roles(self, city_name: str, low: int, high: int) -> set:
        output = set()
        for row in self.dataset:
            if (row[5] == city_name) and (low < int(row[3]) < high):
                output.add(row[-1])
        return output