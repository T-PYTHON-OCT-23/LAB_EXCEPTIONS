def celsius_to_fahrenheit(celsius):
   return (celsius * 9/5) + 32
     


def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9
  


def main():
    while True:
        try:
            input_temperature=input("Enter a temperature and its unit: ").split()
            temperature,unit =float(input_temperature[0]),(input_temperature[1]).upper()
            if unit=="C":
            # print(f"Temperature in Celsius: {temperature} {unit}")
                print(f"Temperature in fahrenheit: {celsius_to_fahrenheit(temperature)} F")
            elif unit=="F":
            # print(f"Temperature in fahrenheit: {temperature} {unit}")
                print(f"Temperature in Celsius: {fahrenheit_to_celsius(temperature)} C ")
            else:
                print("Enter the correct temperature , unit F or C")
        except ValueError:
            print("invalid temperature value , please try agine")
        except TypeError:
            print(" an invalid unit, please try agine ")
        except Exception as e:
            print(e)

main()

