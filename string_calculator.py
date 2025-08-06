class StringCalculator:
    def add(self, numbers: str) -> int:

        if not numbers:
            return 0

        if ',' in numbers:
            number_list = self._parse_numbers(numbers)
            return sum(number_list)

        return int(numbers)

    def _parse_numbers(self, numbers: str):
        """Parse comma or newline-separated numbers into a list of integers."""
        numbers = numbers.replace('\n', ',')
        return [int(num) for num in numbers.split(',')]
