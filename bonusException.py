def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("Welcome to our program")
        temperatureInput = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'), type exit to exit: ")
        if temperatureInput == "exit":
            print("Good bye")
            break
        try:
            temperatureInput = temperatureInput.split(' ')
            temperature, unit = float(temperatureInput[0]), temperatureInput[1].upper()
         
            if unit == "C":
                c = round(celsius_to_fahrenheit(temperature),2)
                print(f"Temperature in Fahrenheit: {c} F ")

            elif unit == "F":
                f = round(fahrenheit_to_celsius(temperature),2)
                print(f"Temperature in Fahrenheit: {f} C")

            elif unit not in ["C", "F"]:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

            
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
    
         

            
            
main()

