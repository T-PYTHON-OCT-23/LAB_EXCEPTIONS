def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit,2)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius,2)
def main():
    temp= input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')
    if temp.count(" ")==0:
        raise ValueError("Invalid input. Please make sure to input a space between the number and the unit")
    _degre , _type =temp.split(" ")
    if _type.upper() == "F" and _degre.isnumeric():
        result=fahrenheit_to_celsius(float(_degre))
        print(f"Temperature in Celsius: {result} C")
    elif _type.upper() == "C" and _degre.isnumeric():
        result=celsius_to_fahrenheit(float(_degre))
        print(f"Temperature in Fahrenheit: {result} F")
    elif _type.upper() != "C" and _type.upper() != "F" and _degre.isnumeric():
        raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    else:
        raise ValueError("Invalid input. please use numbers at the begining followed by unit separated by a space")

while True:
    try:
        main()
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        break