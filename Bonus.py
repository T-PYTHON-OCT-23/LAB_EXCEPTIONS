
def celsius_to_fahrenheit(celsius):

    fahrenheit = (celsius * 9/5) + 32
    result = str(fahrenheit)+" F"

    return result

def fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9

    result = str(celsius)+" C"

    return result



def main():
    
    while True:
        temp_and_unit = input("Enter a temperature and its unit (e.g., 25 C or 77 F):->if you want to exit write exit: ")
        if temp_and_unit=="exit":
            break

        split = temp_and_unit.split(" ")
    
        try:
            temperature = float(split[0])
            unit = split[1]

            if unit.upper() == "C":
                
                print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temperature)}")
            elif unit.upper() == "F":
                print(f"Temperature in Celsius: {fahrenheit_to_celsius(temperature)}")
            else:
                raise TypeError("only accept valid unit F , C")
            
        except TypeError:
            print("only accept valid unit F , C")
            print("!!try agine!!")
        except IndexError:
            print("Enter like this format 25 C or 77 F:")
            print("!!try agine!!")
        except ValueError:
            print("ValueError")
            print("Enter like this format 25 C or 77 F:")
            print("!!try agine!!")
        



main()


