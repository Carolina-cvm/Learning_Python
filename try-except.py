#  try =  test a block of code for errors
#  except = handle the error
#  else = execute code when there is no error
#  finally = execute code, regardless of the result of the try- and except blocks.

# error
try:
  print(x)
except:
  print("An exception occurred") # x is not defined
except:
  print("Something else went wrong")  # x is not defined
  
# no error
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# finally
try:
  print(y)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
