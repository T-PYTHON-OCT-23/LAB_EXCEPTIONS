def celsius_to_fahrenheit(celsius:float)-> float:
    fahernheit =  (float(celsius) * 9/5) + 32
    return fahernheit
    

def fahrenheit_to_celsius(fahrenheit:float)->float:
    celsius = (float(fahrenheit) - 32) * 5/9
    return round(celsius,2)
    

def main():
    while True:
        value,unit = input("Enter a temperature and its unit (e.g., 25 C or 77 F):").split()
        try:
            if unit.upper() == "C":
                conversion = celsius_to_fahrenheit(float(value))
                print(f"Temperature in fahrenheit: {conversion} F")
            elif unit.upper() == "F":
                conversion = fahrenheit_to_celsius(float(value))
                print(f"Temperature in celsius: {conversion} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)


print("Program of temperature  converter")   
main()