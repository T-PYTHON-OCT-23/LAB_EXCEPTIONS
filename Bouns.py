    
def celcius_to_fahrenheit(temp):
    return round((9/5 * temp) + 32,2)

def fahrenheit_to_celcius(temp):
    return round((temp - 32) * 5/9,2)



def main():
    try:
        temp = float(input("Enter temperature value: "))
        unit = input("Enter temperature unit (C or F): ")
        unit=unit.upper()
        if unit == "C":
            converted_temp = celcius_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        elif unit == "F":
            converted_temp = fahrenheit_to_celcius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        else:
            raise TypeError("Invalid unit of measurement. Please enter C or F.")
    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")

        
        
main()