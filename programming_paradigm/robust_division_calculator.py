# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs safe division between two numbers with error handling.
    """
    try:
        # Try to convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Check for zero division
        try:
            result = numerator / denominator
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        # Non-numeric input
        return "Error: Please enter numeric values only."
