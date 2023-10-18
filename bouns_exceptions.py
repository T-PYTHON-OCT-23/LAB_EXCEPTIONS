def celsius_to_fahrenheit(celsius:int)->int:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit:int) ->int:
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    before_transformation = input("Enter a temperature and its unit (e.g., 25 C or 77 F): ")
    value , unit = before_transformation.split(" ") 
    value = float(value)
    
    if value == str:
        raise ValueError("The temperature is incorrect, please try again")
    if unit == "C":
        print(f"You entered a temperature {value} C, Temperature after conversion {celsius_to_fahrenheit(value)} F")
    elif unit == "F":
        print(f"You entered a temperature {value} F, Temperature after conversion {celsius_to_fahrenheit(value)} C")
    else:
        raise TypeError("The unit is incorrect, please try again")


while True:
    try:    
        if agine == "exit":
            break
        main()
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e :
        print(e)
        print("something worng went on")
    finally:
        agine = input("if you want run agine enter A and if you want exit input other: ")


            
            
        
        
        
        
        
    
    

