def celsius_to_fahrenheit(celsius): 
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius  # return (fahrenheit - 32) * 5/9 | both correct

def main () :
   while True: 
     
     user_input= print ("Enter a temperature and its unit: ")
     if user_input =="exit":
        break
try:

     temp, unit =user_input.split(" " , maxsplit = 1)

     if unit.upper()=="C":
        print (f"temperature in Fahrenhiet: {celsius_to_fahrenheit(temp)} C")

     if unit.upper()=="F":
        print (f"temperature in Celsuis: {fahrenheit_to_celsius(temp)} F")
     else:
        print("please try agian")


except ValueError as e :
   print(e)
except TypeError as e:
   print(e)
except Exception as e:
   print(e)


print("welcom to our program")
main()

