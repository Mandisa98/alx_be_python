def safe_divide(numerator, denominator):
    try:
        # Try to turn the inputs into numbers
        num = float(numerator)
        den = float(denominator)

        # If the bottom number is zero, don't divide
        if den == 0:
            return "Error: Cannot divide by zero."

        # If everything is okay, divide
        result = num / den
        return f"The result of the division is {result}"

    # If the user typed letters like "ten", show this:
    except ValueError:
        return "Error: Please enter numeric values only."
