class StringCalculator:
    def add(self, numbers: str) -> int:

        if not numbers:
            return 0
        
        if ',' in numbers:
            number_list = numbers.split(',')
            return sum(int(num) for num in number_list)

        return int(numbers)
