# potential code before try catch

try:
    # code to try to execute
except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception

try:
    10/0
except:
    print("Division error")

try:
    10/0
except ZeroDivisionError:
    print("Division error")
except NameError:
    print("Name error")
