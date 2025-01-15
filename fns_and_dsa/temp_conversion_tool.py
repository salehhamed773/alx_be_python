CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main Program
if __name__ == "__main__":
    try:
        # Prompt the user to enter a temperature
        temperature_input = input("Enter the temperature to convert: ").strip()
        
        # Validate numeric temperature input
        temperature = float(temperature_input)
        
        # Prompt the user to specify the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            # Convert Fahrenheit to Celsius
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted_temperature:.8f}°C")
        elif unit == "C":
            # Convert Celsius to Fahrenheit
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted_temperature:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid numeric temperature and unit.")
