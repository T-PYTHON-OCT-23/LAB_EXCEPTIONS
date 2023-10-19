def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
     
try:
 additoin(10, 20)
except NameError as e:
   print(e)
except Exception as e:
   print(e)

   #bonus

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            temperature, unit = user_input.split()
            temperature = float(temperature)

            if unit == 'C':
                converted_temperature = celsius_to_fahrenheit(temperature)
                converted_unit = 'Fahrenheit'
            elif unit == 'F':
                converted_temperature = fahrenheit_to_celsius(temperature)
                converted_unit = 'Celsius'
            else:
                raise TypeError

            print(f"{temperature} {unit} is equal to {converted_temperature:.2f} {converted_unit}")
            break
        except ValueError:
            print("Invalid temperature value. Please try again.")
        except TypeError:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__": main()
