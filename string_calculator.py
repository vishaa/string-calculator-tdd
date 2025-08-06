class StringCalculator:
    def add(self, numbers: str) -> int:

        if not numbers:
            return 0

        number_list = self._parse_numbers(numbers)
        return sum(number_list)

    def _parse_numbers(self, numbers: str):
        """Parse numbers with various delimiters into a list of integers."""

        delimiter = ','
        if numbers.startswith('//'):
            delimiter, numbers = numbers[2:].split('\n', 1)

        numbers = numbers.replace('\n', ',')
        if delimiter != ',':
            numbers = numbers.replace(delimiter, ',')

        return [int(num) for num in numbers.split(',')]
