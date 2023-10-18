'''def celsius_to_fahrenheit(celsius):
   
   return (celsius * 9/5) + 32.
    

   def fahrenheit_to_celsius(fahrenheit):
     return (fahrenheit - 32) * 5/9

   
   def main():
    while True:
        user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
        try:
            
            temperature, unit = user_input.split()
            temperature = float(temperature)
            
            if unit == 'C':
                converted_temperature = celsius_to_fahrenheit()
                print(f"Temperature in Fahrenheit: {converted_temperature} F")
            elif unit == 'F':
                converted_temperature = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius: {converted_temperature} C")
            else:
                print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature value. Please enter a valid numeric value.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

    print("Welcome to our temperature converter")
    main()
'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
        try:
            temperature, unit = user_input.split()
            temperature = float(temperature)
            
            if unit == 'C':
                converted_temperature = celsius_to_fahrenheit(temperature)
                print(f"Temperature in Fahrenheit: {round(celsius_to_fahrenheit(float(temperature)), 2)} F")
            elif unit == 'F':
                converted_temperature = fahrenheit_to_celsius(temperature)
                print(f"Temperature in Celsius:{round(fahrenheit_to_celsius(float(temperature)), 2)} C")
            else:
                print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature value. Please enter a valid numeric value.")
        except TypeError:
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
 
    print("wellcome to our converter  ")
    main()
