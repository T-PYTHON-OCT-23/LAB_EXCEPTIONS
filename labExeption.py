
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError:
    print("operation failed")
    print("Undefined variable ")
else:
    print("operation successful")
finally:
    pass