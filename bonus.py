def celsius_to_fahrenheit(celsius):
 return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():

    while True:
        userInput = input('Enter a temperature and unit (e.g., "30 C" or "80 F"): ')

        try:
            temp, unit = userInput.split(maxsplit=1)

            if unit.upper() == "C":
                print(f"Temperature in Fahrenheit: {round(celsius_to_fahrenheit(float(temp)), 2)} C")
            elif unit.upper() == "F":
                print(f"Temperature in Celsius: {round(fahrenheit_to_celsius(float(temp)), 2)} C")
            else:
                raise TypeError("Please provide a valid Unit (F, C)")
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)

print("Welcome")

main()