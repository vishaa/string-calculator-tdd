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
