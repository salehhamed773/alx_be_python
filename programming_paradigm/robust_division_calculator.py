def safe_divide(numerator, denominator):
    try:
        num=float(numerator)
        denom=float(denominator)
        if denom == 0:
            return "Error: Cannot divide by zero."
        result = num / denom
        return f"The result of the division is {result:.2f}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
