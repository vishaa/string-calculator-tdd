# String Calculator TDD

This is a TDD (Test-Driven Development) implementation of the String Calculator

## Problem Statement
Create a simple String calculator with a method signature: `int add(string numbers)`

## Requirements Implemented
1. ✅ Empty string returns 0
2. ✅ Single number returns the number itself
3. ✅ Two comma-separated numbers return their sum
4. ✅ Handle any amount of numbers
5. ✅ Handle new lines between numbers instead of commas
6. ✅ Support different delimiters (//[delimiter]\n[numbers...])
7. ✅ Throw exception for negative numbers
8. ✅ Show all negative numbers in exception message

## How to Run

### Prerequisites
- Python 3.7 or higher
- pytest (for running tests)

### Installation
```bash
cd string-calculator-tdd
pip install -r requirements.txt