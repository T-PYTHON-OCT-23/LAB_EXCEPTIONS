def celsius_to_fahrenheit(celsius):
     fahrenheit = round((celsius * 9/5) + 32,2)
     return fahrenheit
    

def fahrenheit_to_celsius(fahrenheit):
    celsius = round((fahrenheit - 32) * 5/9,2)
    return celsius
   





def main ():
    while True:
        temperature_and_unit=input('enter a temperature and its unit (either "C" for Celsius or "F" for Fahrenheit): ')
        try:
            list=temperature_and_unit.split()
            if list[1].upper()=='F':
                print(f'Temperature in celsiu{fahrenheit_to_celsius(int(list[0]))}')
            elif list[1].upper()=='C':
                print(f'Temperature in Fahrenheit{celsius_to_fahrenheit(int(list[0]))}')
            else:
                raise TypeError('invalid unit,try again')
        except ValueError as e:
                print(e)
        except TypeError as e:
                print(e)
        except Exception as e:
             print(e)

main()



