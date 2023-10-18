def additoin(x, y):
    print("Addition:", x + b)
    
while True:
    try: 
        if agine == "exit":
            break
        num1 = int(input(" enter first num: ")) 
        
        num2 = int(input(" enter scound num: ")) 
        additoin(num1, num2)
    except NameError :
        print("the name input can not found !")
    except Exception as e :
        print(e)
        print("something worng went on")
    else:
        print("the operation is successful")
    finally:
        agine = input("if you want run agine enter A and if you want exit input other: ")