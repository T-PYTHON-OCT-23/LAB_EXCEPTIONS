def additoin(x, y):
    
    x = 10
    y = 20
    print("Addition:", x + b)

try:
  additoin(10, 20)
except (NameError) as e :
  print(e)
else:
  print("the operation is successful")
finally:
  print("The problem was that the letter b had no value or was not defined, so the error in the naming appeared to us")


