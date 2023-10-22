def additoin(x, y):
      
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError:
    print("name of varible don't true please check it")
except Exception as e:
    print("something went wrong")  
else:
    print("The operation is successful")      
