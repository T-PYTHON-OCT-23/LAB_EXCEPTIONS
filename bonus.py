def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

user_input = input("either 'C' for Celsius or 'F' for Fahrenheit, Note: (e.g., '25 C' or '77 F'): ")