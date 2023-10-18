def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError as e:
    print(type(e))
    print(f"{e} is the Error we find")
except Exception as e:
    print(f"The Error we found is {e}")
else:
    print("the operation is successful")
finally:
    print("All try and exceot is handle the specific excepting")
