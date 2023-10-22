def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def main():
    while True:
        try:
            user = input("Enter a temperature and its unit (e.g., 25 C or 77 F): ")
            temp, unit = user.split(maxsplit=1)
            if unit.upper() == "C":
                print(f"Temperature in Fahrenheit: {round(celsius_to_fahrenheit(float(temp)), 2)} F")
            elif unit.upper() == "F":
                print(f"Temperature in Celsius: {round(fahrenheit_to_celsius(float(temp)), 2)} C")
            else:
                raise TypeError("vaild unit")
        except ValueError as e:
            print(e) 
        except TypeError as e:
            print(e) 
        else:
            print("The operation is successful")    
          
print("Welcome to our temperature converter")
main()
    