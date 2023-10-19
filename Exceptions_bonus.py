def celsius_to_fahrenheit(celsius): 
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

value= 0
unit= ""

def main (temp):
  for x in temp.split(" " , 1):
    if x.isdigit():
           value+=x

    if x.upper() == "c":
          celsius_to_fahrenheit(value)

    if x.upper() == "f":
        fahrenheit_to_celsius(value)


try:
    main(temp_input)
except ValueError:
    print("enters an invalid temperature value")
except TypeError:
    print("enters an invalid temperature value")




temp_input = input("Enter a temperature and its unit: ")
main(temp_input)



