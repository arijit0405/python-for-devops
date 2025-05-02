x = 10
y = 20

def my_function():
    z = 30
    final = x + y + z
    print(final)          # prints 60

    # nested function (only visible inside my_function)
def my_function_2():
     print(x + y)      # prints 30

          # call the nested function

# call the outer function
my_function()
my_function_2() 
