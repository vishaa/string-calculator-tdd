import pytest
from string_calculator import StringCalculator


class TestStringCalculator:
    
    def setup_method(self):
        self.calculator = StringCalculator()
    
    def test_empty_string_returns_zero(self):
        """Test that empty string returns 0."""
        result = self.calculator.add("")
        assert result == 0

    def test_single_number_returns_number(self):
        """Test that single number returns the number itself."""
        result = self.calculator.add("7")
        assert result == 7

    def test_two_numbers_returns_sum(self):
        """Test that two comma-separated numbers return their sum."""
        result = self.calculator.add("4,5")
        assert result == 9

    def test_multiple_numbers_returns_sum(self):
        """Test that any amount of numbers can be handled."""
        result = self.calculator.add("1,2,3")
        assert result == 6

        result = self.calculator.add("1,2,3,4,5")
        assert result == 15

    def test_newlines_between_numbers(self):
        """Test that new lines between numbers are handled."""
        result = self.calculator.add("1\n2,3")
        assert result == 6

    def test_custom_delimiter(self):
        """Test support for different delimiters."""
        result = self.calculator.add("//;\n3;4")
        assert result == 7

    def test_negative_number_throws_exception(self):
        """Test that negative numbers throw an exception."""
        with pytest.raises(ValueError, match="negative numbers not allowed -1"):
            self.calculator.add("-1")
